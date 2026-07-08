from pymongo import MongoClient
from pymongo.server_api import ServerApi
from urllib.parse import quote_plus
username = "Atharva"
password = quote_plus("Atharva@1312")

uri = f"mongodb+srv://{username}:{password}@cluster0.liutbsa.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri, server_api=ServerApi("1"))

try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)