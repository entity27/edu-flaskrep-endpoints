from flask import Flask, request, url_for, render_template, redirect
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("representation.html", pagename="Index page", endpoint=url_for("index"))

@app.route("/some_static_endpoint")
def static_endpoint():
    return render_template("representation.html", pagename="Static endpoint", endpoint=url_for("static_endpoint"))

@app.route("/form_handler", methods=["POST"])
def form_handler():
    value = request.form["inputname"] if request.form["inputname"] else "none"
    url = url_for("dynamic_endpoint", value=value)
    return redirect(url)

@app.route("/dynamic/<value>")
def dynamic_endpoint(value):
    return render_template("representation.html", pagename="Dynamic endpoint", endpoint=url_for("dynamic_endpoint", value=value))