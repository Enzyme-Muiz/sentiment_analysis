python -m venv env
env\Scripts\activate.bat
pip install Flask
pip install textblob
pip install Flask-RESTful
pip install pre-commit
git init
have a file .pre-commit-config.yaml
pre-commit install
git status
git add -A
pre-commit run
pip install pytest