from pymongo_get_database import get_database

# For testing
from Animal import Animal, str_to_date
from Owner import Owner

dbname = get_database()

def insert(obj, database_name):
    database = dbname[database_name]
    if isinstance(obj, list):
        print("Sending...")
        database.insert_many(obj)
    else:
        print("Sending...")
        database.insert_one(obj)


# def retrieve(database, ID):
#     """Retrives from database based on ID and returns the/all the owner"""
#     owners_dict = []
#     animal_dict = []
#     for convert in database.find({"ID" : ID}, {"_id": 0}):
#         owner_obj = Owner(
#             name=convert["Name"],
#             phone_number=convert["Phone Number"],
#             gender=convert["Gender"],
#             email=convert["Email"],
#             address=convert["Address"]
#         )
#
#         for convert_animal in convert["Animals"]:
#             animal_obj = Animal(
#                 name=convert_animal["Name"],
#                 breed=convert_animal["Breed"],
#                 age=convert_animal["Age"],
#                 weight=convert_animal["Weight"],
#                 gender=convert_animal["Gender"],
#                 allergy=convert_animal["Allergy"],
#                 medication=convert_animal["Medication"],
#                 vaccination= convert_animal["Vaccination Date"],
#                 checkup=convert_animal["Checkup Date"],
#                 # picture=convert_animal["Picture"],
#             )
#             animal_dict.append(animal_obj)
#
#         owner_obj.add_animal(animal_dict)
#         print(owner_obj.to_dict())
#         owners_dict.append(owner_obj)
#         return owners_dict

def retrieve_dict(database_name, ID):
    database = dbname[database_name]
    # return [convert for convert in database.find({"ID" : ID}, {"_id": 0})]
    return database.find_one({"ID" : ID}, {"_id": 0})

testAnimal = dbname["AniTest"]

a1 = Animal("Gab", "smelly feet", 14, 211, "dude", "Bombaclat", "Sleep"
            , "Sat 01 Feb 2025, at 12:00PM", "Sat 04 Feb 2025, at 12:00PM")
a2 = Animal("Amir", "Old", 211, 23, "Idk what is this", "Bombaclat", "Red bull"
            , "Sat 01 Feb 2025, at 12:00PM", "Sat 04 Feb 2025, at 12:00PM")
owner1 = Owner("Zeyu", 1234567891, "m", "zeze", "123asd")
owner2 = Owner("beha", 1231231231, "a", "b", "c")

a1.add_owner(owner1)
#
# stuff = [a1, a2]

testAnimal.drop()
insert(a1.to_dict(), "AniTest")
# insert(owner2.to_dict(), testAnimal)
print(retrieve_dict("AniTest", 1))