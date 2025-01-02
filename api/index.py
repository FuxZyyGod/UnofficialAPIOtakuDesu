from flask import Flask, render_template
from flask_cors import CORS
from s.ongoingHandler import OngoingAnimeDat
from s.completeHandler import CompleteAnimeDat
from s.subtitleHandler import SubtitleAnimeDat
from s.searchHandler import SearchAnimeDat

api = Flask(__name__)
CORS(api)

@api.route("/")
def index():
 return "<h1>ENDPOINTS</h1>"
 
@api.route("/api/v1/ongoing-anime/page/<int:page>")
def ongoingAnime(page):
    return {
        "status": "OK",
        "data": OngoingAnimeDat(page),
    }

@api.route("/api/v1/complete-anime/page/<int:page>")
def completeAnime(page):
    return {
        "status": "OK",
        "data": CompleteAnimeDat(page),
    }

@api.route("/api/v1/anime/<string:sub_title>")
def subTitleAnime(sub_title):
    return {
        "status": "OK",
        "data": SubtitleAnimeDat(sub_title),
    }

@api.route("/api/v1/anime-search/<string:keyword>")
def searchAnime(keyword):
    return {
        "status": "OK",
        "data": SearchAnimeDat(keyword),
    }
 
if __name__ == '__main__':
 api.run(debug=True)
