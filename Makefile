all:

clean_all: rm_database rm_logs
	rm -rf task01/venv
	rm -rf task01/__pycache__
	rm -rf task01/*.pyc
	rm -rf task02/venv
	rm -rf task02/__pycache__
	rm -rf task02/*.pyc
	rm -rf task03/venv
	rm -rf task03/__pycache__
	rm -rf task03/*.pyc
	rm -rf .pytest_cache
	rm -rf task03/.pytest_cache
	rm -rf task03/tests/__pycache__
	rm -rf task03/src/__pycache__

rm_database:
	rm -rf task02/db/*.sqlite

rm_logs:
	rm -rf task03/log
