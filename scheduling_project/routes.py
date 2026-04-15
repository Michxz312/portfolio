from flask import render_template, request, jsonify
from . import scheduling_bp
from scheduling_project.db import get_customer, get_employee

@scheduling_bp.route('/')
def intro_page():
    # TODO: add explanation from jupyter notebook
    return render_template('projects/scheduling/intro.html')

@scheduling_bp.route('/input', methods=["GET", "POST"])
def input_page():
    # get user input/process data
    employees_data = get_employee()
    customers_data = get_customer()
    return render_template('projects/scheduling/input.html', employees=employees_data, customers=customers_data)

@scheduling_bp.route('/result', methods=["POST"])
def result_api():
    data = request.get_json()
    if not data:
        return jsonify({"error": "none"})
    
    employees = data.get("employees_data")
    print(employees)
    return jsonify(employees)

@scheduling_bp.route('/result_page')
def result_page():
    # TODO: solve and show result
    return render_template('projects/scheduling/result.html')