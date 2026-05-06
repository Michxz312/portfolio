from flask import render_template
from . import kanji_game_bp

@kanji_game_bp.route('/')
def kanji():
    return render_template('projects/kanji/kanji.html')