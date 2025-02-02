import datetime

def str_to_date(date_string):
    if isinstance(date_string, list):
        return [datetime.datetime.strptime(date, '%a %d %b %Y, at %I:%M%p') for date in date_string]
    else:
        return [datetime.datetime.strptime(date_string, '%a %d %b %Y, at %I:%M%p')]

def date_to_str(date_list):
    return [date.strftime('%a %d %b %Y, at %I:%M%p') for date in date_list]

class Animal:
    instance = 0

    def __init__(self, name, breed, age, weight, gender, allergy=None, medication=None, vaccination=None, checkup=None):
        Animal.instance += 1
        self._ID = Animal.instance
        self._name = name
        self._breed = breed
        self._age = age
        self._weight = weight
        self._gender = gender

        if allergy is None:
            self._allergy = []
        else:
            if isinstance(allergy, list):
                self._allergy = [aller.lower() for aller in allergy]
            else:
                self._allergy = [allergy.lower()]

        if medication is None:
            self._medication = []
        else:
            if isinstance(medication, list):
                self._medication = [med.lower() for med in medication]
            else:
                self._medication = [medication.lower()]

        if vaccination is None:
            self._vaccination_date = []
        else:
            if isinstance(vaccination, list):
                self._vaccination_date = [str_to_date(vacc) for vacc in vaccination]
            else:
                self._vaccination_date = [str_to_date(vaccination)]

        if checkup is None:
            self._checkup_date = []
        else:
            if isinstance(checkup, list):
                self._checkup_date = [str_to_date(check) for check in checkup]
            else:
                self._checkup_date = [str_to_date(checkup)]

        # Missing default pic
        self._pic = None
        self._is_lost = False

    def to_dict(self):
        vaccination_date_str = [date_to_str(this_date) for this_date in self._vaccination_date]
        checkup_date_str = [date_to_str(this_date) for this_date in self._checkup_date]
        return {
            "ID": self._ID,
            "Name": self._name,
            "Breed": self._breed,
            "Age": self._age,
            "Weight": self._weight,
            "Gender": self._gender,
            "Allergy": self._allergy,
            "Medication": self._medication,
            "Vaccination Date": vaccination_date_str,
            "Checkup Date": checkup_date_str,
            "Picture": self._pic,
            "Lost Status": self._is_lost,
        }

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

    def add_allergy(self, allergy):
        """Accepts medication as a string or a list of string"""
        if isinstance(allergy, list):
            lowercase_allergy = [aller.lower() for aller in allergy]
            self._allergy.extend(lowercase_allergy)
        else:
            self._allergy.append(allergy.lower())

    def remove_allergy(self, allergy):
        """Accepts medication as a string or a list of string. Raises a ValueError when value not found so catch it"""
        if isinstance(allergy, list):
            for med in allergy:
                while med in self._allergy:
                    self._allergy.remove(med)
        else:
            for aller in self._allergy:
                self._allergy.remove(aller.lower())

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
    def name(self):
        return self._breed

    @name.setter
    def name(self, value):
        self._breed = value

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
        return [date.strftime('%a %d %b %Y, at %I:%M%p') for date in self._vaccination_date]

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
