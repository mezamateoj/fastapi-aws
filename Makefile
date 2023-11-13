install:
	#install commands
	pip install -r requirements.txt
format:
	#format code
	black *.py my_lib/*.py
lint:
	#pylynt or flake8
test:
	#tests
deploy:
	#deploy
all: install lint test deploy