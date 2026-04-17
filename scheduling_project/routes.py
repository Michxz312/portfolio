from flask import render_template, request, jsonify
from . import scheduling_bp
from scheduling_project.db import get_customer, get_employee
from scheduling_project.utils import solve
from scheduling_project.config import enumerate_shift, tasks_with_min_levels, skill_levels

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
    employees = data.get("employees_data")
    customers = data.get("customers_data")
    num_employees = len(employees)
    
    result = solve(employees, num_employees, customers, skill_levels, tasks_with_min_levels)

    return jsonify(result)

@scheduling_bp.route('/result_page')
def result_page():
    return render_template('projects/scheduling/result.html')