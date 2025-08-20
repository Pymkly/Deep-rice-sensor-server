import psycopg2
from pymongo import MongoClient

from config import *


def get_connection():
    return psycopg2.connect(
        host=HOST,
        database=DATABASE,
        user=USER,
        password=PASSWORD
    )

def get_mongo_db_connection():
    client = MongoClient("mongodb://root:root@127.0.0.1:27017/")
    # Création d'une base et d'une collection
    db = client[MONGODB_DATABASE]
    return client, db