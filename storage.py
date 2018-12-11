'''
Created on Dec 10, 2018

@author: rabihkodeih
'''

import os
from utils import db_transaction
from settings import BASE_DIR, DATABASE_NAME


@db_transaction
def init_database(cursor):
    # make sure the db file is writable
    sql_file = os.path.join(BASE_DIR, '%s.sqlite' % DATABASE_NAME)
    os.system('chmod 664 "%s"' % sql_file)
    
    # create locations table
    query = '''
        CREATE TABLE IF NOT EXISTS locations (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            latitude TEXT NOT NULL,
            longitude text NOT NULL
        );
    '''
    cursor.execute(query)
    
    # create keyvalues table
    query = '''
        CREATE TABLE IF NOT EXISTS keyvalues (
            key TEXT PRIMARY KEY,
            value TEXT NOT NULL
        );
    '''
    cursor.execute(query)


@db_transaction
def execute_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()
    

@db_transaction
def execute_scalar(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()[0][0]


@db_transaction
def get_value(cursor, key):
    query = 'SELECT value FROM keyvalues WHERE key="%s";' % key 
    cursor.execute(query)
    results = cursor.fetchall()
    value = results[0][0] if results else None
    return value
    
    
@db_transaction
def set_value(cursor, key, value):
    query = 'DELETE FROM keyvalues WHERE key="%s";' % key
    cursor.execute(query)
    query = 'INSERT INTO keyvalues (key, value) values ("%s", "%s");' % (key, value)
    cursor.execute(query)
    

# end of file
