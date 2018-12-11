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


@db_transaction
def execute_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()
    

@db_transaction
def execute_scalar(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()[0][0]


# end of file
