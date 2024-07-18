from flask import Flask, render_template, url_for, request
from dotenv import load_dotenv, find_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
# GLOBAL VARIABLE
uri = "mongodb+srv://naivedya1:qwertyuioa123@cluster0.asq3g2k.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

ATTRIBUTES = ["username", "email", "password", "confirm_password"]
NUM_OF_ATTRIBUTES = len(ATTRIBUTES)



app = Flask(__name__)

# Index page
@app.route("/")
def home_page():
    return render_template("index.html")

# Handling post request for form data
@app.route("/form_data", methods = ["POST"])
def handle_form_data():
    
    status = upload_data(request.form)
    
    return render_template("index.html", status="The data was inserted!")


# Helping functions
# Uploading data to mongo
def upload_data(form_data):
    # Create a new client and connect to the server
    # client = MongoClient(uri, server_api=ServerApi('1'))

    # Trying to insert data
    try:
        # connecting to the specific database and collection
        # database = client["Medtek"]
        # collection = database["FormData"]
        
        # storing the form value into a dictionary
        data_dict = {}
        i = 0
        for attribute in ATTRIBUTES:
            data_dict[attribute] = dict(form_data.lists())['data'][i]
            i += 1

        # Inserting one value
        status = None
        if data_dict["password"] == data_dict["confirm_password"]:
            del data_dict["confirm_password"]
            # status = collection.insert_one(data_dict)
        


        # Closing connection
        # client.close()

        # Returning status
        return status
    
    except Exception as e:
        return e



if __name__ == "__main__":
    app.run(debug=True)