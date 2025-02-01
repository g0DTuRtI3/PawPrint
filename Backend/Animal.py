import datetime

class Animal:
    instance = 0

    def __init__(self,breed, age, weight, height, gender):
        Animal.instance += 1
        self._ID = Animal.instance
        self._breed = breed
        self._age = age
        self._weight = weight
        self._height = height
        self._gender = gender
        self._medication = []
        self._vaccination_date = []
        self._checkup_date = []

        # Missing default pic
        self._pic = None
        self._is_lost = False

    def add_medication(self, medication):
        """Accepts medication as a string or a list of string"""
        if isinstance(medication, list):
            lowercase_med = [med.lower() for med in medication]
            self._medication.extend(lowercase_med)
        else:
            self._medication.append(medication.lower())

    def remove_medication(self, medication):
        """Accepts medication as a string or a list of string. Raises a ValueError when value not found so catch it"""
        if isinstance(medication, list):
            for med in medication:
                while med in self._medication:
                    self._medication.remove(med)
        else:
            for med in self._medication:
                self._medication.remove(med.lower())

    def update_vaccination_date(self):
        """Removes any past date or repeated date"""
        # Remove out of date
        for date in self._vaccination_date.copy():
            if date < datetime.datetime.now():
                self._vaccination_date.remove(date)

        # Remove duplicate
        seen = set()
        result = []
        for date in self._vaccination_date:
            if date not in seen:
                result.append(date)
                seen.add(date)

        self._vaccination_date = result

    def add_vaccination_date(self, year, month, day, hour, minute):
        """All param should be in number
        Adds a date to the checkup list and remove any expired date"""
        self._vaccination_date.append(datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute))
        self._vaccination_date.sort()

        self.update_vaccination_date()

    def remove_vaccination_date(self, year, month, day, hour, minute):
        """Return 'Success' if successful and 'Failed' if not"""
        self.update_vaccination_date()

        to_remove = datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute)
        for date in self._vaccination_date.copy():
            if date == to_remove:
                self._vaccination_date.remove(date)
                return "Success"

        return "Failed"

    def update_checkup_date(self):
        """Removes any past date or repeated date"""
        # Remove out of date
        for date in self._checkup_date.copy():
            if date < datetime.datetime.now():
                self._checkup_date.remove(date)

        # Remove duplicate
        seen = set()
        result = []
        for date in self._checkup_date:
            if date not in seen:
                result.append(date)
                seen.add(date)

        self._checkup_date = result

    def add_checkup_date(self, year, month, day, hour, minute):
        """All param should be in number
        Adds a date to the checkup list and remove any expired date"""
        self._checkup_date.append(datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute))
        self._checkup_date.sort()

        self.update_checkup_date()

    def remove_checkup_date(self, year, month, day, hour, minute):
        """Return 'Success' if successful and 'Failed' if not"""
        self.update_checkup_date()

        to_remove = datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute)
        for date in self._checkup_date.copy():
            if date == to_remove:
                self._checkup_date.remove(date)
                return "Success"

        return "Failed"

    def is_lost(self):
        self._is_lost = True

    @property
    def ID(self):
        return self._ID

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        self._breed = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if value < 0:
            raise ValueError("Weight cannot be negative")
        self._weight = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value < 0:
            raise ValueError("Height cannot be negative")
        self._height = value

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value

    @property
    def medication(self):
        return self._medication

    @medication.setter
    def medication(self, value):
        if isinstance(value, str) or isinstance(value, list):
            self._medication = value

    def set_picture(self, pic):
        self._pic = pic

    @property
    def vaccination_date(self):
        """Returns the date as a list of string of format (Sat 01 Feb 2025, at 12:00PM)"""
        date_list = []
        for date in self._vaccination_date:
            date_list.append(date.strftime('%a %d %b %Y, at %I:%M%p'))
        return date_list

    @vaccination_date.setter
    def vaccination_date(self, value):
        """The value should be of format datetime.datetime"""
        self._vaccination_date = value

    @property
    def checkup_date(self):
        """Returns the date as a list of string of format (Sat 01 Feb 2025, at 12:00PM)"""
        date_list = []
        for date in self._checkup_date:
            date_list.append(date.strftime('%a %d %b %Y, at %I:%M%p'))
        return date_list

    @checkup_date.setter
    def checkup_date(self, value):
        """The value should be of format datetime.datetime"""
        self._vaccination_date = value
