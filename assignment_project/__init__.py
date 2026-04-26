from flask import Blueprint

assignment_bp = Blueprint(
    'assignment',
    __name__,
    url_prefix="project/assignment"
)