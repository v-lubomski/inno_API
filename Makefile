lint:
	@flake8 --max-line-length=120 tests model api

pytest:
	@pytest -s -v