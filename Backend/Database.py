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
    database_name.drop()
    if isinstance(obj, list):
        print("Sending...")
        database_name.insert_many(obj)
    else:
        print("Sending...")
        database_name.insert_one(obj)

def retrieve():
    pass

testAnimal = dbname["AniTest"]
a1 = Animal("Gab", "smelly feet", 14, 211, "dude", "Bombaclat", "Sleep"
            , "Sat 01 Feb 2025, at 12:00PM", "Sat 04 Feb 2025, at 12:00PM")
a2 = Animal("Amir", "Old" , 211, 23, "Idk what is this", "Bombaclat", "Red bull"
            , "Sat 01 Feb 2025, at 12:00PM", "Sat 04 Feb 2025, at 12:00PM")
owner = Owner("Zeyu", 1234567891, "m", "zeze", "123asd")

owner.add_animal(a1)
owner.add_animal(a2)

stuff = [a1, a2]

insert(owner.to_dict(), testAnimal)