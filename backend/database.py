from pymongo import MongoClient
import certifi
import os
from dotenv import load_dotenv


load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")

client = MongoClient(
    MONGO_URL,
    tls=True,
    tlsCAFile=certifi.where(),
    tlsAllowInvalidCertificates=True
    )
db = client["ai_agile_db"]

users_collection= db["users"]
projects_collection=db["projects"]