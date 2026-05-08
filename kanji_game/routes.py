from flask import render_template, request, jsonify
from . import kanji_game_bp
import requests

@kanji_game_bp.route('/', methods=["GET"])
def kanji():
    return render_template('projects/kanji/kanji.html')

@kanji_game_bp.route('/api', methods=["POST"])
def kanji_api():
    data = request.get_json()
    return jsonify(data)

@kanji_game_bp.route("/jisho/<kanji>", methods=["GET"])
def jisho_proxy(kanji):
    url = f"http://beta.jisho.org/api/v1/search/words?keyword={kanji}"
    res = requests.get(url)
    return jsonify(res.json())