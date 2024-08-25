import pymongo
import boto3
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Function to connect Python to MongoDB using Lambda
def connect_python_to_mongodb():
   

    print("connecting.....")
    uri = "mongodb://localhost:27017/"

    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))


    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
    db = client.get_database('NewDb')  # Replace with your database name
    collection = db['Data']  # Replace with your collection name
    
    # Example operation
    document = {'hello': 'kaise ho'}
    collection.insert_one(document)
    
    print("Document inserted into MongoDB.") 
connect_python_to_mongodb()