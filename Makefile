install:
	#install commands
	pip install -r requirements.txt
post-install:
	python -m textblob.download_corpora
format:
	# starting formating of the code...
	black *.py my_lib/*.py
lint:
	# lint usinng pylynt
	pylint --disable=R,C,broad-except *.py my_lib/*.py
	
test:
	# Starting tests for the server
	python -m pytest -vv  test.py test_main.py
build:
	#build container
	docker build -t mezamateoj/wikifast .
push:
	# push the image to docker hub
	docker push mezamateoj/wikifast
run:
	#docker run
	docker run -p 127.0.0.1:8080:8080 mezamateoj/wikifast
deploy:
	#deploy
	aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 188288001838.dkr.ecr.us-east-1.amazonaws.com
	docker build -t wikifast .
	docker tag wikifast:latest 188288001838.dkr.ecr.us-east-1.amazonaws.com/wikifast:latest
	docker push 188288001838.dkr.ecr.us-east-1.amazonaws.com/wikifast:latest
all: install post-install lint test deploy