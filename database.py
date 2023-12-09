from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://rithin:076ecHwHg60yETd9@cluster0.ctrleyy.mongodb.net/?retryWrites=true&w=majority")
db = client.megatronUser

client_admin = MongoClient(
    "mongodb+srv://rithin:076ecHwHg60yETd9@cluster0.ctrleyy.mongodb.net/?retryWrites=true&w=majority")
db_admin = client_admin.megatronDB

class mongo_connection:

    def db_connection(self):
        return db, db_admin