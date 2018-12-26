import os
import sqlite3
import base64
import threading
import json

from functools import wraps
from settings import BASE_DIR
from settings import DB_CONFIG

# the following thread lock is used for the database access operations
# because sqlite3 isn't thread safe
DB_LOCK = threading.Lock()


def db_transaction(func):
    '''
    This decorator abstracts away sqlite3 database connection
    and transaction processing. The resultant function will
    be passed a cursor object that can be used in various db
    operations.
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        sql_file = os.path.join(BASE_DIR, '%s.sqlite' % DB_CONFIG['DB_NAME'])
        with DB_LOCK:
            conn = sqlite3.connect(sql_file, detect_types=sqlite3.PARSE_DECLTYPES)
            cursor = conn.cursor()
            result = func(cursor, *args, **kwargs)
            conn.commit()
            conn.close()
        return result
    return wrapper


@db_transaction
def init_database(cursor):
    # make sure the db file is writable
    sql_file = os.path.join(BASE_DIR, '%s.sqlite' % DB_CONFIG['DB_NAME'])
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

    # create history table
    query = '''
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY,
            location_id INTEGER NOT NULL,
            temperature TEXT,
            wind_speed TEXT,
            humidity TEXT,
            sample_time TIMESTAMP NOT NULL
        )
    '''
    cursor.execute(query)


@db_transaction
def execute_query(cursor, query, *args):
    cursor.execute(query, *args)
    return cursor.fetchall()


@db_transaction
def execute_scalar(cursor, query, *args):
    cursor.execute(query, *args)
    return cursor.fetchall()[0][0]


@db_transaction
def get_text_value(cursor, key):
    query = 'SELECT value FROM keyvalues WHERE key="%s";' % key
    cursor.execute(query)
    results = cursor.fetchall()
    value = results[0][0] if results else None
    return value


def get_json_value(key):
    value = get_text_value(key)
    if value:
        recovered = base64.b64decode(value.encode()[2:-1])
        result = json.loads(recovered)
    else:
        result = None
    return result


@db_transaction
def set_text_value(cursor, key, value):
    query = 'DELETE FROM keyvalues WHERE key="%s";' % key
    cursor.execute(query)
    query = 'INSERT INTO keyvalues (key, value) values ("%s", "%s");' % (key, value)
    cursor.execute(query)


def set_json_value(key, value):
    encoded = base64.b64encode(json.dumps(value).encode('utf-8'))
    set_text_value(key, encoded)


# end of file
