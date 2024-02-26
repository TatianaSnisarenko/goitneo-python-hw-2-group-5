generic_error = 'Something went wrong, please try again.'
generic_invalid_command_format = '''Invalid "command" format. Available commands: 
    - <add Name phone_namber> - to add contact, 
    - <change Name new_phone_number> - to update contact,
    - <phone Name> - to show phone for the person
    - <all> - to show all contacts,
    - <hello> - to show assistance message,
    - <exit> - to exit the bot
    - <close> - to close the bot'''

error_messages_add_contact = {
    'FormatError': 'Invalid "add" format. Command "add" must have 3 arguments: <add Name phone_number>.',
    'KeyError': 'Such name is already present, please, use "change" command instead.'
}

error_messages_change_contact = {
    'FormatError': 'Invalid "change" format. Command "change" must have 3 arguments: <change Name new_phone_number>.',
    'KeyError': 'Such name is not found, please, use "add" command instead.'
}

error_messages_show_phone = {
    'FormatError': 'Invalid "phone" format. Command "phone" must have 2 arguments: <phone Name>.',
    'KeyError': 'Such name is not found, please, try again.'
}

error_messages_show_all = {
    'FormatError': 'Contacts are empty. Please, use add command to add new contacts',
    'KeyError': generic_error
}

error_messages_parse_input = {
    'FormatError': generic_invalid_command_format,
    'KeyError': generic_error
}


def input_error(error_messages):
    def decorator(func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except (IndexError, ValueError):
                return error_messages.get('FormatError')
            except KeyError:
                return error_messages.get('KeyError')
            except Exception:
                return generic_error
        return inner
    return decorator
