install:
	#install commands
	
	pip install -r requirements.txt
unistall:
	pip uninstall -r requirements.txt
format:
	#format code
lint:
	#pylynt or flake8
test:
	#tests
deploy:
	#deploy
all: install lint test deploy