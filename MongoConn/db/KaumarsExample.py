import pymongo
import certifi
# from pymongo import MongoClient

# Crea una instancia de cliente MongoDB
connection = 'mongodb+srv://amatest:Kanito24@cluster01.9pcaq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster01'

client = pymongo.MongoClient(connection, tlsCAFile=certifi.where())
# client = pymongo.MongoClient(connection, ssl_ca_certs=certifi.where())

# Selecciona la base de datos
db = client['db1']

collection = db['test_collect']

document = {"name":"Arnold", "city":"Hollywood"}

insert_doc = collection.insert_one(document)

print(f"inserted Document ID:  {insert_doc.inserted_id}")
client.close()

