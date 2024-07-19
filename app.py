from flask import Flask, render_template, url_for, request
from dotenv import load_dotenv, find_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from hashlib import blake2s

# GLOBAL VARIABLE
URI = "mongodb+srv://naivedya1:qwertyuioa123@cluster0.asq3g2k.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
ENCRYPTION_KEY = b"naivedyakhare"
ATTRIBUTES = ["username", "email", "password", "confirm_password"]

# Creating app object
app = Flask(__name__)

# Index page
@app.route("/")
def home_page():
    return render_template("index.html")

# Handling post request for form data
@app.route("/form_data", methods = ["POST"])
def handle_form_data():
    
    # Using help function for data upload
    status = upload_data(request.form)
    
    return render_template("index.html", status=status)


# Helping functions
# Uploading data to mongo
def upload_data(form_data):
    
    # storing the form value into a dictionary
    data_arr = dict(form_data.lists())["data"]
    data_dict = {}
    i = 0
    for attribute in ATTRIBUTES:
        data_dict[attribute] = data_arr[i]
        i += 1
    
    # Password Check 
    if data_dict["password"] != data_dict["confirm_password"]:
        return "The passwords should match!"

    # Converting email to lower
    data_dict["email"] = data_dict["email"].lower()

    # Hashing the password
    data_dict["password"] = blake2s(bytes(data_dict["password"], encoding="utf-8"), key=ENCRYPTION_KEY).digest()
    
    # Removing confirm_password from dict
    del data_dict["confirm_password"]

    # Create a new client and connect to the server
    client = MongoClient(URI, server_api=ServerApi('1'))

    # Trying to insert data
    try:
        # connecting to the specific database and collection
        database = client["Medtek"]
        collection = database["FormData"]

        # Inserting one value
        collection.insert_one(data_dict)

        # Closing connection
        client.close()

        # Returning status
        return "The data was uploaded!"
    
    except Exception as e:
        return e



if __name__ == "__main__":
    app.run(debug=True)