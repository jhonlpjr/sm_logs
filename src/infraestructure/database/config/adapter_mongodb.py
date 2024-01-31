import os
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from src.shared.enums.config_enum import CONFIG

class MongoDBAdapter:
    def get_client():
        print('>>>>>>>>>>MUESTRAAA CONF MONGO>>>>>>>>', os.getenv(CONFIG.MONGO_URL.value))
        try:
            client = MongoClient(os.getenv(CONFIG.MONGO_URL.value), server_api=ServerApi('1'))
            client.admin.command('ping')
            print('>>>>>>>>>>PINGUEADASO>>>>>>>>')
        except Exception as e:
            print('>>>>>>>>>>ERRORSASO>>>>>>>>', e)
        return client
    
    def get_db():
        client = MongoDBAdapter.get_client()
        db = client[os.getenv(CONFIG.MONGO_DB.value)]
        return db
    
    def get_collection(collection_name):
        db = MongoDBAdapter.get_db()
        collection = db[collection_name]
        return collection