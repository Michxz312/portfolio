from flask import Blueprint

assignment_bp = Blueprint(
    'assignment',
    __name__,
    template_folder = "../../templates",
    url_prefix="/assignment"
)

from . import routes