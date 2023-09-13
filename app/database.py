from pymongo import MongoClient
import os

client = MongoClient(str(os.getenv("MONGODB_URL")))

db = client[str(os.getenv("MONGODB_NAME"))]