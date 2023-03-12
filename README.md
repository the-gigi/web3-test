# web3-test

Learn web3 with Python. This is a simple beginners project for managing your MetaMask wallet with Infura using Python.

The code displays your balance, then sends a little test ETH to a sepolia faucet and then displays your balance after
the transaction.


# Setup

- Get an account with [Infura](https://infura.io)
- Get a wallet with [MetaMask](https://metamask.io)
- Get some testnet ETH for the [Sepolia](https://ethereum.org/en/developers/docs/networks/#sepolia) testnet.

Configure your infura project to use API key secret and then store the key and its secret as environment variables:

- INFURA_API_KEY 
- INFURA_API_KEY_SECRET

Also, get from MetaMask your Sepolia testnet account and private key and store them in the following environment 
variables. 

- SEPOLIA_ACCOUNT
- METAMASK_PRIVATE_KEY

The code reads these env variables to generate a basic authentication token.

# Code Requirements

This is a Python 3 program.

Make sure you have Python 3 installed:

```
$ brew install python
```  

Install `pyenv`:

```
brew install pyenv
```

Install `poetry`:

```
curl -sSL https://install.python-poetry.org | python3 -
```

Set up a virtual environment for the project:

```
. ./init.sh
```

# Usage

Make sure your account has some test ETH (e.g from )

Then, just run the program...

```
$ poetry run python main.py
balance before transaction: 2.1259894454
send 20,000 gwei to 0x987d2f1736F8737d530Bdc7C29fD62B0b9a5A893 (Sepolia faucet account)
balance after transaction: 2.1257594454
```
