from pymongo_get_database import get_database

# For testing
from Animal import Animal, str_to_date
from Owner import Owner

dbname = get_database()


# collection_name = dbname["TestDatabase"]
#
# item_1 = {
#   "_id" : "U1IT00001",
#   "item_name" : "Blender",
#   "max_discount" : "10%",
#   "batch_number" : "RR450020FRG",
#   "price" : 340,
#   "category" : "kitchen appliance"
# }
#
# item_2 = {
#   "_id" : "U1IT00002",
#   "item_name" : "Egg",
#   "category" : "food",
#   "quantity" : 12,
#   "price" : 36,
#   "item_description" : "brown country eggs"
# }
# collection_name.insert_many([item_1,item_2])

def insert(obj, database_name):
    if isinstance(obj, list):
        print("Sending...")
        database_name.insert_many(obj)
    else:
        print("Sending...")
        database_name.insert_one(obj)


def retrieve(database, ID):
    owners_dict = []
    for convert in database.find({"ID" : ID}, {"_id": 0}):
        animal_dict = []
        owner_obj = Owner(
            name=convert["Name"],
            phone_number=convert["Phone Number"],
            gender=convert["Gender"],
            email=convert["Email"],
            address=convert["Address"]
        )
        owners_dict.append(owner_obj)

        for convert_animal in convert["Animals"]:
            animal_obj = Animal(
                name=convert_animal["Name"],
                breed=convert_animal["Breed"],
                age=convert_animal["Age"],
                weight=convert_animal["Weight"],
                gender=convert_animal["Gender"],
                allergy=convert_animal["Allergy"],
                medication=convert_animal["Medication"],
                vaccination= convert_animal["Vaccination Date"],
                checkup=convert_animal["Checkup Date"],
                # picture=convert_animal["Picture"],
            )
            animal_dict.append(animal_obj)
            print(animal_obj.to_dict())

def translate_owner(owners_dict):
    owners = []
    for owner in owners_dict:
        pass


testAnimal = dbname["AniTest"]

a1 = Animal("Gab", "smelly feet", 14, 211, "dude", "Bombaclat", "Sleep"
            , "Sat 01 Feb 2025, at 12:00PM", "Sat 04 Feb 2025, at 12:00PM")
a2 = Animal("Amir", "Old", 211, 23, "Idk what is this", "Bombaclat", "Red bull"
            , "Sat 01 Feb 2025, at 12:00PM", "Sat 04 Feb 2025, at 12:00PM")
owner1 = Owner("Zeyu", 1234567891, "m", "zeze", "123asd")
owner2 = Owner("beha", 1231231231, "a", "b", "c")

owner1.add_animal(a1)
owner1.add_animal(a2)
#
# stuff = [a1, a2]

# testAnimal.drop()
# insert(owner1.to_dict(), testAnimal)
# insert(owner2.to_dict(), testAnimal)
retrieve(testAnimal, 1)
print()