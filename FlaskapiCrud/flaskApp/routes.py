from flask import render_template, url_for, flash, redirect, jsonify
from flaskApp import app
# from flaskApp.models import User, Post

import requests

DUMMY_USERNAME = "Usmanflask1234"
DUMMY_PASSWORD = "Fawad123"


@app.route("/signup")
def signup():
    URL = "http://127.0.0.1:8000/user/signup"
    PARAMS = {
        "username":DUMMY_USERNAME,
        "password":DUMMY_PASSWORD
        }

    x = requests.post(URL, json = PARAMS)
    print(x.json())
    return jsonify (
        x.json()
    )

