from flask import render_template
from . import assignment_bp

@assignment_bp.route('/')
def intro_page():
    return render_template('projects/assignment/intro.html')
