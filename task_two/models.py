from collections import UserDict
from errors import *


class Field:
    def __init__(self, value: str):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        if isinstance(other, Field):
            return self.value == other.value
        return False

    def __hash__(self):
        return hash(self.value)


class Name(Field):
    def __init__(self, name: str):
        super().__init__(name)

    def __eq__(self, other):
        if isinstance(other, Name):
            return self.value == other.value
        return False

    def __hash__(self):
        return hash(self.value)


class Phone(Field):
    def __init__(self, phone_number: str):
        cleared_phone_number = phone_number.strip()
        if not phone_number.isdigit() or len(cleared_phone_number) != 10:
            raise InvalidPhoneNumberError()
        super().__init__(cleared_phone_number)

    def __eq__(self, other):
        if isinstance(other, Phone):
            return self.value == other.value
        return False

    def __hash__(self):
        return hash(self.value)


class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number: str):
        phone = Phone(phone_number)
        if not phone in self.phones:
            self.phones.append(phone)

    def remove_phone(self, phone_number: str):
        phone = Phone(phone_number)
        if phone in self.phones:
            self.phones.remove(phone)

    def edit_phone(self, old_phone_number: str, new_phone_number: str):
        old_phone = Phone(old_phone_number)
        for index, phone in enumerate(self.phones):
            if phone == old_phone:
                self.phones[index] = Phone(new_phone_number)
                return

    def find_phone(self, phone_number: str):
        phone = Phone(phone_number)
        if phone in self.phones:
            return phone
        else:
            return None

    def __eq__(self, other):
        if isinstance(other, Record):
            return self.name == other.name and self.phones == other.phones
        return False

    def __hash__(self):
        return hash((self.name, tuple(self.phones)))

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):

    def add_record(self, record: Record):
        self.data[record.name] = record

    def find(self, name: str):
        return self.data.get(Name(name))

    def delete(self, name: str):
        self.data.pop(Name(name), None)
