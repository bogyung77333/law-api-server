from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

LAW_OC = os.environ.get("LAW_OC")

@app.route("/")
def home():
    return {"status": "ok"}

@app.route("/law")
def get_law():
    params = {
        "OC": LAW_OC,
        "target": "eflaw",
        "type": "JSON",
        "ID": request.args.get("ID"),
        "MST": request.args.get("MST"),
        "efYd": request.args.get("efYd"),
        "JO": request.args.get("JO")
    }

    # None 값 제거
    params = {k: v for k, v in params.items() if v}

    url = "https://www.law.go.kr/DRF/lawService.do"

    res = requests.get(url, params=params)
    return jsonify(res.json())

if __name__ == "__main__":
    app.run()
