install:
	#install commands
	pip install -r requirements.txt
format:
	#format code
	black *.py my_lib/*.py
lint:
	#pylynt or flake8
	pylint --disable=R,C *.py my_lib/*.py
	
test:
	#tests
deploy:
	#deploy
all: install lint test deploy