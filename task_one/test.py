import unittest
from commands import *


class TestContactFunctions(unittest.TestCase):
    def setUp(self):
        self.contacts = {}

    def tearDown(self):
        self.contacts.clear()

    def test_add_contact_correct_flow(self):
        result = add_contact(['John', '123456789'], self.contacts)
        self.assertEqual(result, 'Contact added.')
        self.assertEqual(self.contacts['John'], '123456789')

    def test_add_contact_index_error(self):
        result = add_contact(['John'], self.contacts)
        self.assertEqual(
            result, error_messages_add_contact.get('FormatError'))

    def test_add_contact_value_error(self):
        result = add_contact(['John', '123456789', 'skdfjl'], self.contacts)
        self.assertEqual(
            result, error_messages_add_contact.get('FormatError'))

    def test_add_contact_name_already_present(self):
        self.contacts['John'] = '987654321'
        result = add_contact(['John', '123456789'], self.contacts)
        self.assertEqual(
            result, error_messages_add_contact.get('KeyError'))

    def test_change_contact_correct_flow(self):
        self.contacts['Cher'] = '987654321'
        result = change_contact(['Cher', '3334444555'], self.contacts)
        self.assertEqual(result, 'Contact updated.')
        self.assertEqual(self.contacts['Cher'], '3334444555')

    def test_change_contact_index_error(self):
        result = change_contact(['Cher'], self.contacts)
        self.assertEqual(
            result, error_messages_change_contact.get('FormatError'))

    def test_change_contact_value_error(self):
        result = change_contact(['Cher', '123456789', 'skdfjl'], self.contacts)
        self.assertEqual(
            result, error_messages_change_contact.get('FormatError'))

    def test_change_contact_name_is_apsent(self):
        result = change_contact(['Kyle', '123456789'], self.contacts)
        self.assertEqual(
            result, error_messages_change_contact.get('KeyError'))

    def test_show_phone_correct_flow(self):
        self.contacts['John'] = '123456789'
        result = show_phone(['John'], self.contacts)
        self.assertEqual(result, '123456789')

    def test_show_phone_index_error(self):
        result = show_phone([], self.contacts)
        self.assertEqual(
            result, error_messages_show_phone.get('FormatError'))

    def test_show_phone_value_error(self):
        result = show_phone(['John', 'skdfl'], self.contacts)
        self.assertEqual(
            result, error_messages_show_phone.get('FormatError'))

    def test_show_phone_name_not_found(self):
        result = show_phone(['Kuki'], self.contacts)
        self.assertEqual(result, error_messages_show_phone.get('KeyError'))

    def test_show_all_correct_flow(self):
        self.contacts['John'] = '123456789'
        self.contacts['Cher'] = '112233445'
        result = show_all(self.contacts)
        self.assertEqual(result, 'John: 123456789, Cher: 112233445')

    def test_show_all_value_error(self):
        result = show_all(self.contacts)
        self.assertEqual(
            result, error_messages_show_all.get('FormatError'))

    def test_parse_input_correct_flow(self):
        result = parse_input('add')
        self.assertEqual(result, ('add',))

    def test_parse_input_value_error(self):
        result = parse_input('')
        self.assertEqual(
            result, error_messages_parse_input.get('FormatError'))


if __name__ == '__main__':
    unittest.main()
