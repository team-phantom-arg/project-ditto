VERSION := local

compile c:
	rm -fr build dist *.spec
	
	pyinstaller app.py \
		--onefile \
		--add-data logic/:logic/ \
		-n base
	
	mv dist/* .
	rm -fr build dist *.spec


build b:
	docker build . -t docker.io/brianwolf94/python3-flask:$(VERSION)


push p:
	docker push docker.io/brianwolf94/python3-flask:$(VERSION)


run r:
	docker run -it --rm -p 5000:5000 docker.io/brianwolf94/python3-flask:$(VERSION)