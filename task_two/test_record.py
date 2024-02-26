import unittest
from models import *


class TestRecord(unittest.TestCase):

    def test_record(self):
        john_record = Record('John')
        self.assertEqual(type(john_record), Record)
        self.assertEqual(john_record.name, Name('John'))
        self.assertEqual(john_record, Record('John'))
        self.assertEqual(len(john_record.phones), 0)

    def test_add_phone(self):
        john_record = Record('John')
        john_record.add_phone('1234567890')
        self.assertEqual(len(john_record.phones), 1)
        self.assertTrue(Phone('1234567890') in john_record.phones)

    def test_add_phone_with_duplication(self):
        john_record = Record('John')
        john_record.add_phone('1234567890')
        john_record.add_phone('1234567890')
        self.assertEqual(len(john_record.phones), 1)
        self.assertTrue(Phone('1234567890') in john_record.phones)

    def test_remove_phone(self):
        john_record = Record('John')
        john_record.add_phone('1234567890')
        self.assertEqual(len(john_record.phones), 1)
        self.assertTrue(Phone('1234567890') in john_record.phones)
        john_record.remove_phone('1234567890')
        self.assertFalse(Phone('1234567890') in john_record.phones)

    def test_remove_phon_with_no_such_phone(self):
        john_record = Record('John')
        john_record.add_phone('1234567890')
        self.assertEqual(len(john_record.phones), 1)
        self.assertTrue(Phone('1234567890') in john_record.phones)
        self.assertFalse(Phone('2222267890') in john_record.phones)
        john_record.remove_phone('2222267890')
        self.assertEqual(len(john_record.phones), 1)

    def test_edit_phone(self):
        john_record = Record('John')
        john_record.add_phone('1234567890')
        self.assertEqual(len(john_record.phones), 1)
        self.assertTrue(Phone('1234567890') in john_record.phones)
        self.assertFalse(Phone('2222267890') in john_record.phones)
        john_record.edit_phone('1234567890', '2222267890')
        self.assertEqual(len(john_record.phones), 1)
        self.assertFalse(Phone('1234567890') in john_record.phones)
        self.assertTrue(Phone('2222267890') in john_record.phones)

    def test_edit_phone_with_no_old_phone(self):
        john_record = Record('John')
        john_record.add_phone('1234567890')
        self.assertEqual(len(john_record.phones), 1)
        self.assertTrue(Phone('1234567890') in john_record.phones)
        self.assertFalse(Phone('3333367890') in john_record.phones)
        self.assertFalse(Phone('2222267890') in john_record.phones)
        john_record.edit_phone('3333367890', '2222267890')
        self.assertEqual(len(john_record.phones), 1)
        self.assertTrue(Phone('1234567890') in john_record.phones)
        self.assertFalse(Phone('3333367890') in john_record.phones)
        self.assertFalse(Phone('2222267890') in john_record.phones)

    def test_find_phone_with_no_old_phone(self):
        john_record = Record('John')
        john_record.add_phone('1234567890')
        self.assertEqual(len(john_record.phones), 1)
        self.assertTrue(Phone('1234567890') in john_record.phones)
        self.assertFalse(Phone('3333367890') in john_record.phones)
        found = john_record.find_phone('1234567890')
        self.assertEqual(found, Phone('1234567890'))
        not_found = john_record.find_phone('3333367890')
        self.assertIsNone(not_found)

    def test_str(self):
        john_record = Record('John')
        john_record.add_phone('1234567890')
        john_record.add_phone('1234567890')
        expected_str = f"Contact name: {john_record.name.value}, phones: {
            '; '.join(p.value for p in john_record.phones)}"
        self.assertEqual(str(john_record), expected_str)


if __name__ == '__main__':
    unittest.main()
