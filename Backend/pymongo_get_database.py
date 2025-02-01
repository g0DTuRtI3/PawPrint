from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

def get_database():

    CONNECTION = os.getenv("MONGO_URI")

    if not CONNECTION:
        raise ValueError("The url is not in the .env")

    client = MongoClient(CONNECTION)

    return client["ConU"]

# if __name__ == "__main__":
#     # Call get_database() and store the database object in dbname
#     dbname = get_database()
#
#     # You can now interact with the database `dbname`
#     print(f"Connected to database: {dbname.name}")