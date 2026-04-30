import numpy as np
import random

def create_courses(m, l, u):
    courses = []
    for i in range(m):
        max_students = np.random.randint(l, u+1)
        courses.append({
            "course_id": i,
            "max": max_students
        })
    return courses

def create_students(n, m):
    course_id = range(0,m)
    students = []
    for i in range(n):
        # gender: 1 for female and 0 otherwise
        rand_gender = random.random()
        # international: 1 for international students and 0 otherwise
        rand_international = random.random()

        gender = 1 if (rand_gender > 0.6) else 0
        international = 1 if (rand_international < 0.11) else 0 
        preference = random.sample(course_id, 4)

        students.append({
            "student_id": i,
            "gender":gender,
            "international": international,
            "preference": preference
        })
    return students

def get_results(students, courses):
    data=[]
    return data