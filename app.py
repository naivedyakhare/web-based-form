from flask import Flask, render_template, url_for, request, redirect, jsonify, json
from dotenv import load_dotenv, find_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from hashlib import blake2s
from models.profile import Profile
from models.query import Query

# GLOBAL VARIABLE
URI = "mongodb+srv://naivedya1:qwertyuioa123@cluster0.asq3g2k.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
ENCRYPTION_KEY = b"naivedyakhare"
USER = Profile()
QUERY = Query()
# Creating app object
app = Flask(__name__)


# ROUTING SECTION
# Welcome Page
@app.route("/")
def render_index():
    questions = create_questions()
    return render_template("index.html", questions=questions)


# Profile section
@app.route("/profile", methods=["GET", "POST"])
def render_profile():
    if request.method == "GET":
        return render_template("profile.html")
    
    if request.method == "POST":
        handle_profile(request)
        return redirect("/qna")


# QnA section
@app.route("/qna", methods = ["POST", "GET"])
def render_qna():
    
    # Using help function for data upload
    
    return render_template("qna.html")


#####################################################################################
# HELPING FUNCTIONS
# Uploading personal information to mongoDB
def handle_profile(request):
    global USER
    form_data = request.form

    client = MongoClient(URI, server_api=ServerApi('1'))
    
    database = client["Medtek"]
    collection = database["FormData"]
    
    name = form_data.get("name")
    email = form_data.get("email")
    gender = form_data.get("gender")
    qna = {}
    exists = False

    search = QUERY.search_profile(email=email)
    update = QUERY.update_profile(name=name, gender=gender, email=email)

    mongo_data = collection.find_one(search)

    if mongo_data != None:
        collection.update_many(search, update)
        qna = mongo_data["data"]["QnA"]
        exists = True
    
    create_local_profile(name=name, email=email, gender=gender, qna=qna, exists=exists)
    
    return 


def create_local_profile(name, email, gender, qna, exists):
    USER.set_profile(name=name, email=email, gender=gender, exists=exists)
    USER.set_qna(qna)


def create_questions():
    
    with open("./static/data/questions.txt") as f:
        questions = f.read().split("\n")
    return questions


if __name__ == "__main__":
    app.run(debug=True)