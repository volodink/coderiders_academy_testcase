# -*- coding: utf-8 -*-
"""
    Coderiders academy Task 2 utility functions.
"""

import os
import sys
import random
import sqlite3
from typing import List

from faker import Faker
from pony import orm

orm.set_sql_debug(False)

db = orm.Database()

# Create fakes generator data and fixed seed for test purposes
fake = Faker()
Faker.seed(0)

# Fix random seed for test purposes
random.seed(123)

# System constants
DB_PATH = f'{os.path.dirname(sys.argv[0])}/db/state_library.sqlite'


# Create database file by path
def create_database_file(db_path) -> None:
    """
        Creates database file by given database path.

    Args:
        db_path: path to the database to be created

    Returns:
        None
    """
    if not os.path.exists(db_path):
        with open(db_path, 'w', encoding='utf-8') as file:
            file.close()


# Create publishers and books test data
def get_test_data() -> tuple:
    """
        Generates random data of books and publishers.

    Returns:
        Tuple: publishers list and books list
    """
    publishers_list = [(i, fake.company(), fake.city()) for i in range(1, 6)]

    genres_list = ['tech', 'cyberpunk', 'manga', 'novel', 'fantasy']
    books_list = [(i,
                   fake.sentence(nb_words=4).split('.')[0],
                   fake.sentence(ext_word_list=genres_list, nb_words=1).split('.')[0].lower(),
                   random.randint(2000, 2050),
                   random.randint(1, 5)) for i in range(1, 100)]

    return publishers_list, books_list


def prepare_test_data_sqlite(library) -> None:
    """
        Creates and populates database with given random data.

    Args:
        library: random data to insert to database

    Returns:
        None
    """
    publishers_list, books_list = library

    create_database_file(DB_PATH)

    with sqlite3.connect(DB_PATH) as con:
        # Getting cursor
        cur = con.cursor()

        # Drop table for sake of education :)
        cur.execute('''DROP TABLE IF EXISTS publishers''')
        cur.execute('''DROP TABLE IF EXISTS books''')

        # Create table 'publishers' and 'books'
        sql_query = '''CREATE TABLE publishers
                       (id int, name text, city text)'''
        cur.execute(sql_query)
        sql_query = '''
            CREATE TABLE books
                (id int,
                 name text,
                 genre text,
                 year text,
                 publisher_id int)
        '''
        cur.execute(sql_query)

        # Execute inserts for list in one batch
        sql_query = "insert into publishers values (?, ?, ?)"
        cur.executemany(sql_query, publishers_list)

        # Create books list as test data
        cur.executemany("insert into books values (?, ?, ?, ?, ?)", books_list)


def query_data_sqlite(query_string):
    """
        Queries database by given SQL query string

    Args:
        query_string: SQL string to be executed

    Returns:
        List of data
    """
    with sqlite3.connect(DB_PATH) as con:
        cur = con.cursor()
        result = cur.execute(query_string)
    return result


class Publisher(db.Entity):
    """
        Publisher entity class.
    """
    name = orm.Required(str)
    city = orm.Required(str)
    books = orm.Set("Book")


class Book(db.Entity):
    """
        Book entity class.
    """
    name = orm.Required(str)
    genre = orm.Required(str)
    year = orm.Required(int)
    publisher_id = orm.Required(Publisher)


def prepare_test_data_ponyorm(library) -> None:
    """
        Prepares database using Pony ORM library

    Args:
        library: random data to insert to database

    Returns:
        None
    """
    publishers_list_simple, books_list_simple = library

    create_database_file(DB_PATH)

    orm.show(Publisher)
    orm.show(Book)

    db.bind(provider='sqlite', filename=DB_PATH, create_db=True)

    db.generate_mapping(create_tables=True)

    @orm.db_session
    def populate_database():
        for publisher in publishers_list_simple:
            Publisher(name=publisher[1], city=publisher[2])
        db.commit()

        for book in books_list_simple:
            Book(name=book[1], genre=book[2], year=book[3], publisher_id=book[4])

    populate_database()


def query_data_ponyorm() -> List:
    """
        Queries database in ORM way

    Returns:
        Query result
    """
    @orm.db_session
    def get_data():
        return orm.select((b.name, p.name)
                          for b in Book for p in Publisher
                          if (2009 <= b.year <= 2018) and (b.genre in ['tech', 'cyberpunk']) and p.id == b.publisher_id.id)[:]
    return get_data()
