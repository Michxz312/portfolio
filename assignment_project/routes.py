from flask import render_template, request, jsonify
from . import assignment_bp
from assignment_project.utils import create_courses, create_students, get_results
from assignment_project.db import init, reset_all, get_courses, get_students, insert_courses, insert_students

@assignment_bp.route('/')
def intro_page():
    return render_template('projects/assignment/intro.html')

@assignment_bp.route('/input', methods=["GET", "POST"])
def input_page():
    if request.method == "POST":
        num_students = int(request.form.get("students") or 1)
        num_courses = int(request.form.get("courses"))
        if num_courses < 4:
            num_courses = 4
        max = int(request.form.get("max") or 1)
        min = int(request.form.get("min") or 1)
        init()
        students = create_students(num_students, num_courses)
        courses = create_courses(num_courses, min, max)
        reset_all()
        insert_students(students)
        insert_courses(courses)
    students = get_students()
    courses = get_courses()
    return render_template('projects/assignment/input.html', students=students, courses=courses)

@assignment_bp.route('/result', methods=["POST"])
def result_api():
    data = request.get_json()
    students = data.get("student_data")
    courses = data.get("course_data")
    result = get_results(students, courses)
    return jsonify(result)

@assignment_bp.route('/result_page')
def result_page():
    return render_template('projects/assignment/result.html')