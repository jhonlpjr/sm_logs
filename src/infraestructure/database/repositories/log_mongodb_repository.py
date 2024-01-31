from src.domain.interfaces.log_interface import ILog
from src.domain.repository.log_repository import LogRepository
from src.infraestructure.database.config.adapter_mongodb import MongoDBAdapter

class LogMongoDBRepository(LogRepository):
    
    def __init__(self, collectionName: str):
        
        if not collectionName:
            raise Exception('The collection name is required for MongoDBRepository')
        
        self.collectionName = collectionName
        self.collection = MongoDBAdapter.get_collection(collectionName)

    def save(self, log: ILog):
        # Lógica para guardar el log en la base de datos MongoDB
        logDict = log.__dict__
        collection = self.collection.insert_one(logDict)
        return log

    def findAll(self, query: ILog):
        # Lógica para obtener los logs de la base de datos MongoDB
        dataCollections = self.collection.find(query)
        collections = list(dataCollections)
        print('>>>>>>>>>>>Collections', collections)
        return collections
    
    def findById(self, id: int):
        # Lógica para obtener un log por id de la base de datos MongoDB
        collection = self.collection.find_one(id)
        return collection