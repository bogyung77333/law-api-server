import os
import requests
from flask import Flask, request, Response, jsonify

app = Flask(__name__)

LAW_OC = os.environ.get("LAW_OC")

@app.route("/")
def home():
    return {"status": "ok"}

@app.route("/search-precedents")
def search_precedents():
    query = request.args.get("query", "")
    display = request.args.get("display", 5)
    page = request.args.get("page", 1)

    url = "https://www.law.go.kr/DRF/lawSearch.do"

    params = {
        "OC": LAW_OC,
        "target": "prec",
        "type": "JSON",
        "query": query,
        "display": display,
        "page": page,
        "sort": "ddes"
    }

    r = requests.get(url, params=params)

    return Response(
        r.text,
        status=r.status_code,
        content_type=r.headers.get("Content-Type", "text/plain; charset=utf-8")
    )
