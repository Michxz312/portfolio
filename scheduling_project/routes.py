from flask import render_template, request, jsonify
from . import scheduling_bp
from scheduling_project.db import get_customer, get_employee, insert_customer, insert_employees, reset_all
from scheduling_project.utils import get_result, generate_customer_data_custom_distribution, generate_employee_data_custom_distribution
from scheduling_project.config import tasks_with_min_levels, skill_levels, salary_weight, distribution, demand_distribution, days

@scheduling_bp.route('/')
def intro_page():
    # TODO: add explanation from jupyter notebook
    return render_template('projects/scheduling/intro.html')

@scheduling_bp.route('/input', methods=["GET", "POST"])
def input_page():
    if request.method == "POST":
        num_employees = int(request.form.get("employees") or 1)
        num_customers = int(request.form.get("customers") or 1)
        employees = generate_employee_data_custom_distribution(num_employees, skill_levels, tasks_with_min_levels, salary_weight, distribution)
        customers = generate_customer_data_custom_distribution(num_customers, days, demand_distribution)   
        reset_all()
        insert_employees(employees)
        insert_customer(customers)
    # get current DB
    employees_data = get_employee()
    customers_data = get_customer()
    return render_template('projects/scheduling/input.html', employees=employees_data, customers=customers_data)

@scheduling_bp.route('/result', methods=["POST"])
def result_api():
    data = request.get_json()
    employees = data.get("employees_data")
    customers = data.get("customers_data")
    
    result = get_result(employees, customers)
    status = result.get("status")
    print(result)

    if status != "Optimal":
        return jsonify({
            "status": status,
            "data": None
        })

    return jsonify({
        "status": status,
        "data": result.get("data")
    })

@scheduling_bp.route('/result_page')
def result_page():
    return render_template('projects/scheduling/result.html')