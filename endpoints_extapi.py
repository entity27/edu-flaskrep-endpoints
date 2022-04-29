import json
from app import *
import urllib.request
from flask import Response

API_REQUEST_BASE = "https://en.wikipedia.org/w/api.php?"

@app.route("/extapi", methods=["GET", "POST"])
def index_extapi(value = None):
    if request.args.keys():
        api_req = API_REQUEST_BASE + "&".join([f"{key}={value}" for key, value in request.args.items()])
        try:
            with urllib.request.urlopen(api_req) as response:
                data = json.loads(response.read().decode('utf8'))
        except:
            return redirect(url_for("index_extapi"))
        return Response(json.dumps(data), mimetype="application/json")
    return render_template("extapi_repr.html")