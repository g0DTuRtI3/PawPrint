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
        # self.animals = []

    def to_dict(self):
        """Translate the obj into a dictionary format"""
        # animal_dict = []
        # for animal in self.animals:
        #     animal_dict.append(animal.to_dict())

        return {
            "ID": self._ID,
            "Name": self._name,
            "Phone Number": self._phone_number,
            "Gender": self._gender,
            "Email": self._email,
            "Address": self._address,
            # "Animals": animal_dict,
        }

    # def add_animal(self, new_animal):
    #     """Adds new animals to the owner.
    #     new_animal can be one animal or a list of them"""
    #     if isinstance(new_animal, list):
    #         self.animals.extend(new_animal)
    #     else:
    #         self.animals.append(new_animal)

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
