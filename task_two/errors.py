class InvalidPhoneNumberError(Exception):
    def __init__(self, message='Invalid phone number: must be 10 digits value'):
        self.message = message
        super().__init__(self.message)
