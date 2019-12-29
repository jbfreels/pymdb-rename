install:
		python3 -m pip install --user -r requirements.txt

test:
		python3 -m unittest discover -s tests