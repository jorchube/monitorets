install-test-requirements:
	pip install -r test_requirements.txt

test:
	pytest .

update-external-dependencies-manifest:
	python ./build_helper/flatpak-pip-generator.py --requirements-file=./requirements.txt --output pypi-dependencies
