import os
import sys
import unittest
from settings import DB_CONFIG, BASE_DIR
import gi
gi.require_version('Gtk', '3.0')
import storage  # @IgnorePep8
from storage import init_database  # @IgnorePep8


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        DB_CONFIG['DB_NAME'] = 'testdb'
        init_database()
        unittest.TestCase.setUp(self)

    def tearDown(self):
        sql_file = os.path.join(BASE_DIR, '%s.sqlite' % DB_CONFIG['DB_NAME'])
        os.remove(sql_file)
        unittest.TestCase.tearDown(self)

    def test_storage_execute_query(self):
        query = '''
            INSERT INTO locations (id, name, latitude, longitude) VALUES
            (1, "NAME_1", "LAT_1", "LONG_1"),
            (2, "NAME_2", "LAT_2", "LONG_2"),
            (3, "NAME_3", "LAT_3", "LONG_3");
        '''
        storage.execute_query(query)
        rows = storage.execute_query('SELECT id, name, latitude, longitude FROM locations ORDER BY id;')
        self.assertEqual(
            rows,
            [(1, 'NAME_1', 'LAT_1', 'LONG_1'),
             (2, 'NAME_2', 'LAT_2', 'LONG_2'),
             (3, 'NAME_3', 'LAT_3', 'LONG_3')]
        )
        sys.stdout.write('\nTest "storage_execute_query" passed')

    def test_storage_execute_scalar(self):
        query = '''
            INSERT INTO locations (id, name, latitude, longitude) VALUES
            (1, "NAME_1", "LAT_1", "LONG_1"),
            (2, "NAME_2", "LAT_2", "LONG_2"),
            (3, "NAME_3", "LAT_3", "LONG_3");
        '''
        storage.execute_query(query)
        count = storage.execute_scalar('SELECT COUNT(*) FROM locations;')
        self.assertEqual(count, 3)
        sys.stdout.write('\nTest "storage_execute_scalar" passed')

    def test_storage_set_txt_value(self):
        data = {
            'KEY_1': 'VALUE_1',
            'KEY_2': 'VALUE_2',
            'KEY_3': 'VALUE_3'
        }
        for key, value in data.items():
            storage.set_text_value(key, value)
            self.assertEqual(storage.get_text_value(key), value)
        storage.set_text_value('KEY_1', 'MODIFIED')
        self.assertEqual(storage.get_text_value('KEY_1'), 'MODIFIED')
        self.assertEqual(storage.get_text_value('MISSING'), None)
        sys.stdout.write('\nTest "storage_set_txt_value" passed')

    def test_storage_set_json_value(self):
        data = {
            'KEY_1': {'name': 'NAME_1', 'data': 'DATA_1'},
            'KEY_2': {'name': 'NAME_2', 'data': 'DATA_2'},
            'KEY_3': {'name': 'NAME_3', 'data': 'DATA_3'}
        }
        for key, value in data.items():
            storage.set_json_value(key, value)
            self.assertEqual(storage.get_json_value(key), value)
        modified = {'name': 'MOD_NAME_1', 'data': 'MOD_DATA_1'}
        storage.set_json_value('KEY_1', modified)
        self.assertEqual(storage.get_json_value('KEY_1'), modified)
        self.assertEqual(storage.get_json_value('MISSING'), None)
        sys.stdout.write('\nTest "storage_set_json_value" passed')


if __name__ == '__main__':
    unittest.main()


# end of file
