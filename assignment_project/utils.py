import numpy as np
import random
import cvxpy as cp

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
    n = len(students)
    m = len(courses)
    x = cp.Variable((n,m), integer = True)
    pref = [list(map(int, s['preference'].split(","))) for s in students]
    constraints = [] 

    constraints += constraint1(x, constraints, n, pref)
    constraints += [x >= 0, x <= 1]
    
    a = 2
    objective = cp.Minimize(cp.sum([cp.sum([x[i, pref[i][0]]  + a*x[i, pref[i][1]] + a**2*x[i,pref[i][2]] + a**3*x[i,pref[i][3]]for i in range(n)])]))

    prob = cp.Problem(objective, constraints)
    status = prob.solve()

    # results
    students_in_course = {course['id']: sum(x.value[:,i]) for i,course in enumerate(courses)}
    preferences_count = [[0]*4 for _ in range(n)]
    for i in range(n):
        for j in range(4):
            if x.value[i,pref[i][j]] > 0.5 :
                preferences_count[i][j] = 1
                break
    preference_assignment_count = [sum([preferences_count[i][j] for i in range(n)]) for j in range(4)]
    print(preference_assignment_count)
    return {
        "status": status,
        "students_in_course": students_in_course,
        "preferences_count": preferences_count,
        "preference_assignment_count": preference_assignment_count
    }

# Each student gets exactly one course j in preference of student i
def constraint1(x, constraints, n, pref): 
    for i in range(n):
        constraints += [cp.sum([x[i,j] for j in pref[i]]) == 1]
    return constraints

def constraint2(x, constraints, n, courses):
    for course in courses:
        id = course['id']
        max = course['max']
        constraints += [cp.sum([x[i,id] for i in range(n)]) <= max]
    return constraints