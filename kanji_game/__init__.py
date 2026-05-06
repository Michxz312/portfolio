from flask import Blueprint

kanji_game_bp = Blueprint(
    'kanji',
    __name__,
    template_folder = "../../templates",
    url_prefix="/kanji"
)

from . import routes