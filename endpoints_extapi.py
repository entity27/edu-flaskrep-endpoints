from app import *

@app.route("/extapi")
def index_extapi():
    return render_template("extapi_repr.html", pagename="Index page", endpoint=url_for("index"))