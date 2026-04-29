from flask import Flask, request, Response
import requests
import os

app = Flask(__name__)

LAW_OC = os.environ.get("LAW_OC")

@app.route("/")
def home():
    return {
        "status": "ok",
        "message": "law api proxy server is running"
    }

@app.route("/law")
def get_law():
    if not LAW_OC:
        return {"error": "LAW_OC environment variable is missing"}, 500

    params = {
        "OC": LAW_OC,
        "target": "eflaw",
        "type": request.args.get("type", "JSON"),
        "ID": request.args.get("ID"),
        "MST": request.args.get("MST"),
        "efYd": request.args.get("efYd"),
        "JO": request.args.get("JO"),
        "chrClsCd": request.args.get("chrClsCd")
    }

    params = {k: v for k, v in params.items() if v}

    url = "https://www.law.go.kr/DRF/lawService.do"

    try:
        res = requests.get(url, params=params, timeout=20)
        return Response(
            res.text,
            status=res.status_code,
            content_type=res.headers.get("Content-Type", "application/json; charset=utf-8")
        )
    except Exception as e:
        return {"error": str(e)}, 500
