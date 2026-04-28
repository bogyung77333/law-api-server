import os
import requests
from flask import Flask, request, Response

app = Flask(__name__)
LAW_OC = os.environ.get("LAW_OC")

@app.route("/")
def home():
    return {"status": "ok", "law_oc_exists": bool(LAW_OC)}

@app.route("/search-precedents")
def search_precedents():
    try:
        query = request.args.get("query", "덤핑")
        display = request.args.get("display", "5")
        page = request.args.get("page", "1")

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
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "ko-KR,ko;q=0.9",
            "Referer": "https://www.law.go.kr/",
            "Connection": "keep-alive"
        }

        r = requests.get(url, params=params, headers=headers, timeout=15)
        return Response(
            r.text,
            status=200,
            content_type="text/plain; charset=utf-8"
        )
    except Exception as e:
        return Response(
            f"SERVER ERROR: {str(e)}",
            status=500,
            content_type="text/plain; charset=utf-8"
        )
