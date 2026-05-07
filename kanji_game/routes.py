from flask import render_template, request, jsonify
from . import kanji_game_bp

@kanji_game_bp.route('/', methods=["GET"])
def kanji():
    return render_template('projects/kanji/kanji.html')

@kanji_game_bp.route('/api', methods=["POST"])
def kanji_api():
    data = request.get_json()
    return jsonify(data)