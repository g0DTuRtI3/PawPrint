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
