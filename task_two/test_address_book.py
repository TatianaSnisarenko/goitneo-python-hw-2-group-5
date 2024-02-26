import unittest
from models import *


class TestAddressBook(unittest.TestCase):
    def setUp(self):
        self.book = AddressBook()

    def test_add_record(self):
        john_record = Record('John')
        self.book.add_record(john_record)
        self.assertEqual(len(self.book.data), 1)

    def test_add_record_when_record_is_present(self):
        john_record = Record('John')
        self.book.add_record(john_record)
        self.assertEqual(len(self.book.data), 1)
        self.book.add_record(Record('John'))
        self.assertEqual(len(self.book.data), 1)

    def test_delete(self):
        john_record = Record('John')
        self.book.add_record(john_record)
        self.book.delete('John')
        self.assertEqual(len(self.book.data), 0)

    def test_delete_when_record_is_apsent(self):
        john_record = Record('John')
        self.book.add_record(john_record)
        self.assertEqual(len(self.book.data), 1)
        self.book.delete('Jane')
        self.assertEqual(len(self.book.data), 1)

    def test_find(self):
        john_record = Record('John')
        self.book.add_record(john_record)
        self.assertEqual(len(self.book.data), 1)
        found = self.book.find('John')
        self.assertEqual(found, john_record)
        not_found = self.book.find('Jane')
        self.assertIsNone(not_found)


if __name__ == '__main__':
    unittest.main()
