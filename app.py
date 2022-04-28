from flask import Flask, request, url_for, render_template, redirect
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

import endpoints_base
import endpoints_extapi