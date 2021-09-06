.PHONY: clean rm_database

clean:
	rm -rf task01/venv
	rm -rf task01/__pycache__
	rm -rf task01/*.pyc
	rm -rf task02/venv
	rm -rf task02/__pycache__
	rm -rf task02/*.pyc
	rm -rf task03/venv
	rm -rf task03/__pycache__
	rm -rf task03/*.pyc

rm_database:
	rm -rf task02/db/*.sqlite