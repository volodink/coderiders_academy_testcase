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
	rm -rf venv

rm_database:
	rm -rf task02/db/*.sqlite

rm_logs:
	rm -rf task03/log

pep8:
	@echo "PEP8 checking..."
	python3 -m pycodestyle --show-source --show-pep8 --ignore=E501 task01/sort.py task01/task01.py
	python3 -m pycodestyle --ignore=E501 task02/test_data.py task02/task02.py
	python3 -m pycodestyle --ignore=E501 task03/src/elevator.py task03/src/building.py task03/app.py task03/task03.py
	@echo "\nFlake8 checker..."
	python3 -m flake8 --ignore E501 task01/
	python3 -m flake8 --ignore E501 task02/
	python3 -m flake8 --ignore E501 task03/src task03/app.py task03/task03.py
	@echo "\nPylint linter checking..."
	python3 -m pylint task01/task01.py task01/sort.py
	python3 -m pylint task02/test_data.py task02/task02.py
	python3 -m pylint task03/app.py task03/setup.py task03/task03.py task03/src/elevator.py task03/src/building.py
