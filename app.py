from dotenv import load_dotenv
import os
from flask import Flask, render_template, request
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import utils as ut

import matplotlib.pyplot as plt

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['MAX_CONTENT_LENGTH'] = 64 * 1024 * 1024
UPLOAD_FOLDER = '/tmp'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

uri = f"mongodb+srv://{os.getenv('USER')}:{os.getenv('PASSWORD')}@cluster0.vultpjd.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri, server_api=ServerApi('1'))

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        db = client["MusicCatalog"]
        collection = db["MusicCatalog"]

        file = request.files['midi']
        file.save('midi.mid')

        title = request.form['title']
        album = request.form['album']
        singer = request.form['singer']
        composer = request.form['composer']
        lyricist = request.form['lyricist']
        link = request.form['link']

        melody = ut.midi_sequence()

        data = {
            "title": title,
            "album": album,
            "singer": singer,
            "composer": composer,
            "lyricist": lyricist,
            "link": link,
            "melody": melody
        }

        collection.insert_one(data)

    return render_template('index.html')