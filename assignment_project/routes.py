from flask import render_template
from . import assignment_bp

@assignment_bp.route('/')
def intro_page():
    return render_template('projects/assignment/intro.html')

@assignment_bp.route('/input', methods=["GET", "POST"])
def input_page():
    return render_template('projects/assignment/input.html')

@assignment_bp.route('/result', methods=["GET", "POST"])
def result_page():
    return render_template('projects/assignment/result.html')