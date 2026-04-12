from flask import render_template, request
from . import scheduling_bp

@scheduling_bp.route('/')
def intro():
    # TODO: add explanation from jupyter notebook
    return render_template('intro.html')

@scheduling_bp.route('/input')
def input():
    # get user input/process data
    return render_template('input.html')

@scheduling_bp.route('/result')
def result():
    # TODO: solve and show result
    return render_template('result.html')