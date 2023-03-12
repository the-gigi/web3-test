import base64
import os

import web3
from pprint import pprint as pp


class WalletManager:
    def __init__(self):
        """ """
        self.w3 = self.__create_web3_instance()
        self.account = os.environ['SEPOLIA_ACCOUNT']
        self.account_private_key = os.environ['METAMASK_PRIVATE_KEY']
        self.max_fee_per_gas = self.w3.toWei('250', 'gwei')
        self.max_priority_fee_per_gas = self.w3.eth.max_priority_fee
        self.chain_id = self.w3.eth.chain_id

    @property
    def instance(self):
        return self.w3

    @staticmethod
    def __create_web3_instance():
        """ """
        infura_api_key = os.environ['INFURA_API_KEY']
        infura_api_key_secret = os.environ['INFURA_API_KEY_SECRET']
        data = f'{infura_api_key}:{infura_api_key_secret}'.encode('ascii')
        basic_auth_token = base64.b64encode(data).strip().decode('utf-8')

        infura_sepolia_endpoint = f'https://sepolia.infura.io/v3/{infura_api_key}'

        headers = dict(Authorization=f'Basic {basic_auth_token}')
        return web3.Web3(web3.HTTPProvider(infura_sepolia_endpoint, request_kwargs=dict(headers=headers)))

    def get_balance(self, unit='wei'):
        balance = self.w3.eth.get_balance(self.account)
        if unit != 'wei':
            return self.w3.fromWei(balance, unit)

    def send_eth(self, target_account, amount, unit='wei'):
        """ """
        if unit != 'wei':
            amount = self.w3.toWei(amount, unit)

        nonce = self.w3.eth.get_transaction_count(self.account)

        tx = {'nonce': nonce,
              'maxFeePerGas': self.max_fee_per_gas,
              'maxPriorityFeePerGas': self.max_priority_fee_per_gas,
              'from': self.account,
              'to': target_account,
              'value': amount,
              'data': b'',
              'type': 2,
              'chainId': self.chain_id}
        tx['gas'] = self.w3.eth.estimate_gas(tx)

        signed_tx = self.w3.eth.account.sign_transaction(tx, self.account_private_key)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)

        result = self.w3.eth.wait_for_transaction_receipt(tx_hash)
        if result['status'] != 1:
            raise RuntimeError(f'transaction failed: {tx_hash}')


def main():
    """ """
    wm = WalletManager()
    # w3 = cli.instance

    sepolia_faucet_account = '0x987d2f1736F8737d530Bdc7C29fD62B0b9a5A893'

    balance = str(wm.get_balance('ether'))
    print(f'balance before transaction: {balance}')

    print(f'send 20,000 gwei to {sepolia_faucet_account} (Sepolia faucet account)')
    wm.send_eth(sepolia_faucet_account, 20000, 'gwei')

    balance = str(wm.get_balance('ether'))
    print(f'balance after transaction: {balance}')


if __name__ == '__main__':
    main()
