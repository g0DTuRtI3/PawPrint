from pymongo_get_database import get_database

#For testing
from Animal import Animal
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

def retrieve(database):
    owners_dict = []
    for x in database.find({}, {"_id" : 0}):
        print(x)
        owners_dict.append(x)

def translate(owners_dict):
    owners = []
    for owner in owners_dict:
        pass

testAnimal = dbname["AniTest"]

a1 = Animal("Gab", "smelly feet", 14, 211, "dude", "Bombaclat", "Sleep"
            , "Sat 01 Feb 2025, at 12:00PM", "Sat 04 Feb 2025, at 12:00PM")
a2 = Animal("Amir", "Old" , 211, 23, "Idk what is this", "Bombaclat", "Red bull"
            , "Sat 01 Feb 2025, at 12:00PM", "Sat 04 Feb 2025, at 12:00PM")
owner1 = Owner("Zeyu", 1234567891, "m", "zeze", "123asd")
owner2 = Owner("beha", 1231231231, "a", "b", "c")

owner1.add_animal(a1)
owner1.add_animal(a2)
#
# stuff = [a1, a2]

# testAnimal.drop()
# insert(owner.to_dict(), testAnimal)
# insert(owner2.to_dict(), testAnimal)
retrieve(testAnimal)