# -*- coding: utf-8 -*-
"""
    Coderiders Academy Task 2 implementation main file.
"""

import os

import test_data

# -----------------------------------------------
# Ответ на задание:
QUERY_STRING = """
    SELECT b.name, p.name
    FROM books AS b
    JOIN publishers AS p on p.id = b.publisher_id
    WHERE
        (b.year >= 2009 AND b.year <= 2018)
        AND
        (b.genre = 'tech' OR b.genre = 'cyberpunk');
"""
# -----------------------------------------------

print('Now, lets generate test data... ', end='', sep='')
library = test_data.get_test_data()
print('done')

print('Prepare data via Python SQLite library method... ', end='', sep='')
test_data.prepare_test_data_sqlite(library)
print('done.')

print('Querying using SQLite library:\n')
result = test_data.query_data_sqlite(QUERY_STRING)
print(*result, sep='\n')
print('\nDone.')

print('\nNow, via PonyORM :)')

print('Removing DB file ...', end='', sep='')
os.remove(test_data.DB_PATH)
print('done.')

print('Prepare data via PonyORM library method... ')
test_data.prepare_test_data_ponyorm(library)
print('done.')

print('Querying using SQLite library:\n')
result = test_data.query_data_ponyorm()
print(*result, sep='\n')
print('\nDone.')

print('\nHave a nice day :)')
