from flask import Flask,request,abort,render_template_string
from flask_cors import CORS
from bson.json_util import dumps,default
import pandas as pd
import json

app = Flask(__name__)
CORS(app)


@app.route("/api/getjson")
def getjson():
    query = request.args.get("query")
    if query :
        with open("./data/master_data/"+query) as f:
            df = json.load(f)
        return json.dumps(df)

if __name__ == "__main__":
    app.run(port=8000,debug=True)