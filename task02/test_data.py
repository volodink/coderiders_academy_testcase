# -*- coding: utf-8 -*-
import os
import sys
import random
import sqlite3
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
def create_database_file(DB_PATH):
        if not os.path.exists(DB_PATH):
            open(DB_PATH, 'w').close()


# Create publishers and books test data
def get_test_data():
    publishers_list = [(id, fake.company(), fake.city()) for id in range(1, 6)]

    genres_list = ['tech','cyberpunk','manga','novel', 'fantasy']
    books_list = [(id, 
                    fake.sentence(nb_words=4).split('.')[0], 
                    fake.sentence(ext_word_list=genres_list, nb_words=1).split('.')[0].lower(),
                    random.randint(2000, 2050),
                    random.randint(1, 5)) for id in range(1, 100)]
    
    return publishers_list, books_list


def prepare_test_data_sqlite(library):

    publishers_list, books_list = library

    create_database_file(DB_PATH)
    
    with sqlite3.connect(DB_PATH) as con:
        # Getting cursor
        cur = con.cursor()

        # Drop table for sake of education :)
        cur.execute('''DROP TABLE IF EXISTS publishers''')
        cur.execute('''DROP TABLE IF EXISTS books''')

        # Create table 'publishers' and 'books'
        cur.execute('''CREATE TABLE publishers
                    (id int, name text, city text)''')
        cur.execute('''CREATE TABLE books
                    (id int, name text, genre text, year text, publisher_id int)''')

        # Execute inserts for list in one batch
        cur.executemany("insert into publishers values (?, ?, ?)", publishers_list)

        # Create books list as test data
        cur.executemany("insert into books values (?, ?, ?, ?, ?)", books_list)


def query_data_sqlite(query_string):
    result = ''
    
    with sqlite3.connect(DB_PATH) as con:
        cur = con.cursor()
        result = cur.execute(query_string)
        
    return result


class Publisher(db.Entity):
    name = orm.Required(str)
    city = orm.Required(str)
    books = orm.Set("Book")


class Book(db.Entity):
    name = orm.Required(str)
    genre = orm.Required(str)
    year = orm.Required(int)
    publisher_id = orm.Required(Publisher)


def prepare_test_data_ponyorm(library):

    publishers_list_simple, books_list_simple = library

    create_database_file(DB_PATH)

    orm.show(Publisher)
    orm.show(Book)

    db.bind(provider='sqlite', filename=DB_PATH, create_db=True)

    db.generate_mapping(create_tables=True)

    @orm.db_session    
    def populate_database():
        for p in publishers_list_simple:
            Publisher(name=p[1], city=p[2])
        db.commit()
                
        for b in books_list_simple:
            Book(name=b[1], genre=b[2], year=b[3], publisher_id=b[4])

    populate_database()    


def query_data_ponyorm():

    @orm.db_session
    def get_data():
        return orm.select((b.name, p.name) 
        for b in Book for p in Publisher 
        if (b.year >= 2009 and b.year <= 2018) and (b.genre in ['tech', 'cyberpunk']) and p.id  == b.publisher_id.id)[:]
    
    return get_data()
