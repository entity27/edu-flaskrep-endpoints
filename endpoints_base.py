from functools import reduce
import re
from app import *

@app.route("/endpoints")
def index_endpoints():
    return render_template("endpoints_repr.html", pagename="Index page", endpoint=url_for("index"))

@app.route("/endpoints/some_static_endpoint")
def static_endpoint():
    return render_template("endpoints_repr.html", pagename="Static endpoint", endpoint=url_for("static_endpoint"))

@app.route("/form_handler", methods=["POST"])
def form_handler():
    rkeys = request.form.keys()
    if "inputname" in rkeys:
        value = request.form["inputname"] if request.form["inputname"] else "none"
        url = url_for("dynamic_endpoint", value=value)
        return redirect(url)
    elif "api_request" in rkeys:
        return redirect(url_for("index_extapi") + f"?{request.form['api_request']}")

@app.route("/endpoints/dynamic/<value>")
def dynamic_endpoint(value):
    return render_template("endpoints_repr.html", pagename="Dynamic endpoint", endpoint=url_for("dynamic_endpoint", value=value))