rm -rf dist *.egg-info
python3 buildSetup.py
python3 setup.py sdist
twine upload dist/*
python3 upgrade.py
