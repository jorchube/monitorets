install-test-requirements:
	pip install -r test_requirements.txt

test:
	pytest .
