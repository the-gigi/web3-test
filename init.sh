VERSION=3.10.6
pyenv install "$VERSION"
pyenv local "$VERSION"
poetry init
poetry install