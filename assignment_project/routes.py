from flask import render_template, request
from . import assignment_bp
from assignment_project.utils import create_courses, create_students

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
        students = create_students(num_students, num_courses)
        courses = create_courses(num_courses, min, max)
        print(num_students,num_courses,max,min)
        print(students)
        print(courses)
    return render_template('projects/assignment/input.html')

@assignment_bp.route('/result', methods=["GET", "POST"])
def result_page():
    return render_template('projects/assignment/result.html')