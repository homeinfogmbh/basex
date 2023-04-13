FILE_LIST = ./.installed_files.txt

.PHONY: build clean install publish pull push uninstall

default: | pull clean install

build:
	@ python ./setup.py sdist bdist_wheel

clean:
	@ rm -Rf ./build ./dist

install:
	@ ./setup.py install --record $(FILE_LIST)

publish:
	@ twine upload dist/*

pull:
	@ git pull

push:
	@ git push

pypi: | clean build publish

uninstall:
	@ while read FILE; do echo "Removing: $$FILE"; rm "$$FILE"; done < $(FILE_LIST)
