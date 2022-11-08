python -m ensurepip
python -m pip install PEP517 PIP SetUpTools Wheel --upgrade

python -m pip install -e ".[build, doc, lint, publish, test]" --upgrade --user
