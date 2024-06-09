from unittest import TestCase

from dataStructures.hash_table.hashtable import HashTables


class TestHashTables(TestCase):
    def test_set_item(self):
        hash_table = HashTables()
        hash_table.set_item("grapes", 10000)
        hash_table.set_item("apples", 20000)
        hash_table.set_item("oranges", 30000)
        self.assertEqual(str(hash_table),
                         '[None, [[\'oranges\', 30000]], None, None, [[\'apples\', '
                         '20000]], None, [[\'grapes\', 10000]]]')

    def test_get_item(self):
        hash_table = HashTables()
        hash_table.set_item("grapes", 10000)
        hash_table.set_item("apples", 20000)
        hash_table.set_item("oranges", 30000)
        print(str(hash_table))
        self.assertEqual(hash_table.get_item("grapes"), 10000)
        self.assertEqual(hash_table.get_item("apples"), 20000)
        self.assertEqual(hash_table.get_item("oranges"), 30000)

    def test_get_keys(self):
        hash_table = HashTables()
        hash_table.set_item("grapes", 10000)
        hash_table.set_item("apples", 20000)
        hash_table.set_item("oranges", 30000)
        self.assertEqual(hash_table.get_keys(), ['oranges', 'apples', 'grapes'])
    def test_str(self):
        hash_table = HashTables()
        hash_table.set_item("grapes", 10000)
        self.assertEqual(str(hash_table),
                         '[None, None, None, None, None, None, [[\'grapes\', '
                         '10000]]]')
