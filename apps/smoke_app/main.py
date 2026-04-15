# apps/smoke_app/main.py
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Smoke Test OK 🚀"