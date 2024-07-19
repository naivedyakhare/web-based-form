from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://naivedya1:qwertyuioa123@cluster0.asq3g2k.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# uri = r"mongodb+srv://naivedya:qwertyuioa123@cluster0.asq3g2k.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0&tlsCAFile=C:\Users\rohit\OneDrive\Desktop\MEDTEK\Web-based form\testing\isrgrootx1.pem"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    database = client["Medtek"]
    collection = database["FormData"]
    
    d = {"name": "navi", "age": 21}
    collection.insert_one(d)
    print("Data inserted!")
    client.close()

except Exception as e:
    print(e)
