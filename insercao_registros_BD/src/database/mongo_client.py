import pymongo
from config.settings import MONGO_URI, DB_NAME

client = pymongo.MongoClient(MONGO_URI)
db = client[DB_NAME]