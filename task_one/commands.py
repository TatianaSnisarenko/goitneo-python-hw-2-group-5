from error_handling import *


@input_error(error_messages_parse_input)
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error(error_messages_add_contact)
def add_contact(args, contacts):
    name, phone = args
    if contacts.get(name) != None:
        raise KeyError
    contacts[name] = phone
    return 'Contact added.'


@input_error(error_messages_change_contact)
def change_contact(args, contacts):
    name, phone = args
    existing_phone = contacts[name]
    contacts[name] = phone
    return 'Contact updated.'


@input_error(error_messages_show_phone)
def show_phone(args, contacts):
    if (len(args) != 1):
        raise ValueError
    return contacts[args[0]]


@input_error(error_messages_show_all)
def show_all(contacts):
    if contacts:
        return ', '.join(': '.join(item) for item in contacts.items())
    else:
        raise ValueError
