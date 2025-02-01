
class Owner:
    instances = 0

    def __init__(self, name, phone_number, gender, email, address):
        Owner.instances += 1
        self._ID = Owner.instances
        self._name = name
        self._phone_number = phone_number
        self._gender = gender
        self._email = email
        self._address = address

    @property
    def ID(self):
        return self._ID

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        if len(str(value)) != 10:
            self._phone_number = value
        else:
            print("Fun Fact: A phone number has 10 numbers")

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value