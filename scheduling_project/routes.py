from flask import render_template, request
from . import scheduling_bp

@scheduling_bp.route('/')
def intro_page():
    # TODO: add explanation from jupyter notebook
    return render_template('projects/scheduling/intro.html')

@scheduling_bp.route('/input')
def input_page():
    # get user input/process data
    return render_template('projects/scheduling/input.html')

@scheduling_bp.route('/result')
def result_page():
    # TODO: solve and show result
    return render_template('projects/scheduling/result.html')