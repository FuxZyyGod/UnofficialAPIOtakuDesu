from flask import Flask, jsonify, render_template
from flask_cors import CORS
from s.ongoingHandler import OngoingAnimeDat
from s.completeHandler import CompleteAnimeDat
from s.subtitleHandler import SubtitleAnimeDat
from s.searchHandler import SearchAnimeDat

api = Flask(__name__)
CORS(api)

@api.route("/")
def index():
 return render_template("index.html")
 
@api.route("/api/v1/ongoing-anime/page/<int:page>")
def ongoingAnime(page):
    return jsonify({
        "status": "OK",
        "data": OngoingAnimeDat(page),
    })

@api.route("/api/v1/complete-anime/page/<int:page>")
def completeAnime(page):
    return jsonify({
        "status": "OK",
        "data": CompleteAnimeDat(page),
    })

@api.route("/api/v1/anime/<string:sub_title>")
def subTitleAnime(sub_title):
    return jsonify({
        "status": "OK",
        "data": SubtitleAnimeDat(sub_title),
    })

if __name__ == '__main__':
 api.run(debug=True)

@api.route("/api/v1/anime-search/<string:keyword>")
def searchAnime(keyword):
    return jsonify({
        "status": "OK",
        "data": SearchAnimeDat(keyword),
    })
