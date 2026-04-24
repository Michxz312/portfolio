from scheduling_project.config import enumerate_shift, days, tasks_with_min_levels, skill_levels
import random
import numpy as np
import pulp
import csv

def generate_employee_data_custom_distribution(num_employees, skill_levels, tasks_with_min_levels, salary_weight, distribution):
    employees_data = []
    # Calculate the number of employees in each skill level based on the distribution
    num_employees_distribution = {level: int(pct * num_employees) for level, pct in distribution.items()}
    
    # Adjust for any rounding differences to ensure the total count matches num_employees
    while sum(num_employees_distribution.values()) < num_employees:
        num_employees_distribution[random.choice(list(num_employees_distribution.keys()))] += 1
        
    # Generate data for each employee based on the distribution
    for skill_level_label, count in num_employees_distribution.items():
        skill_level = skill_levels[skill_level_label]
        for _ in range(count):
            training_level_array = []
            for task, min_level in tasks_with_min_levels.items():
                if skill_level >= min_level:
                    training_level = random.randint(1, 100)  # Training levels range from 1 to 100
                else:
                    training_level = 0
                training_level_array.append(training_level)
            salary = salary_weight["K"] + salary_weight["a"] * (training_level_array[0]+training_level_array[1]) \
            + salary_weight["b"] * (training_level_array[2]) \
            + salary_weight["c"] * (training_level_array[3]+training_level_array[4]+training_level_array[5]) \
            + salary_weight["d"] * (training_level_array[6])
            employees_data.append((skill_level_label, training_level_array, salary))
    
    # Shuffle the data to mix skill levels
    random.shuffle(employees_data)
    
    return employees_data

def generate_customer_data_custom_distribution(max, days, distribution):
    customer_data = []

    for day, index in days.items():
        # we would have a different number of customers demanded for each day from 0 to num_customer
        num_customer = np.random.randint(0, max)

        # calculate the number of customer in shifts based on the distribution
        num_customer_distribution = {shift: int(pct * num_customer) for shift, pct in distribution.items()}
        
        # Adjust for any rounding differences to ensure the total count matches num_employees
        while sum(num_customer_distribution.values()) < num_customer:
            num_customer_distribution[random.choice(list(num_customer_distribution.keys()))] += 1

        # for each shift, get the distribution
        for shift_label, count in num_customer_distribution.items():
            customer_data.append((day, shift_label, count))
    
    return customer_data

def solve(employees_data, customers):
    prob = pulp.LpProblem("Shift_Assignment", pulp.LpMinimize)

    employees = employees_data
    e_id = [e["id"] for e in employees]
    salaries = {e["id"]: e['salary'] for e in employees_data}
    skill_level = {e["id"]: e['skill_level'] for e in employees_data}
    training_levels = {
        e["id"]: list(map(int, e['training'].split(','))) 
        for e in employees_data
    }

    # Create variable X_ijd
    x = pulp.LpVariable.dicts("x", [(i, j, d) for i in e_id for j in range(7) for d in range(5)], cat="Binary")
    
    prob += pulp.lpSum(
        x[i, j, d] * salaries[i] 
        for i in e_id
        for j in range(7) 
        for d in range(5)
    )
    add_constraint1(prob, x, e_id)
    add_constraint2(prob, customers, x, e_id)
    add_constraint3(prob, x, skill_level, e_id)
    add_constraint4(prob, training_levels, salaries, x, e_id)

    prob.solve()
    total_salary = sum(
        salaries[i]*x[i,j,d].value()
        for i in e_id
        for j in range(7)
        for d in range(5)
    ) 
    
    result = []
    index_shift = {v:k for k,v in enumerate_shift.items()}
    index_day = {v:k for k,v in days.items()}
    for i in e_id:
        for j in range(7):
            for d in range(5):
                if x[(i,j,d)].varValue == 1:
                    result.append({
                        "id": i,
                        "day": index_day[d],
                        "shift": index_shift[j]
                    })

    return {
        "status": pulp.LpStatus[prob.status],
        "assignments": result,
        "optimal": total_salary
    }

def get_result(employees_data, customers_data):
    result = solve(employees_data, customers_data)
    status = result["status"]
    if status != "Optimal":
        return {
            "status": status,
            "data": None,
            "objective": None
        }
    return {
        "status": status,
        "data": result["assignments"],
        "objective": result["optimal"]
    }

# constraint 1: An employee can be assigned to at most one shift for each day
def add_constraint1(prob, x, e_id):
    for i in e_id:
        for d in range(5):
            prob += pulp.lpSum(x[i, j, d] for j in range(7)) <= 1

# constraint 2: Each shifts has the required number of employees at day d
def add_constraint2(prob, customer, x, e_id):
    d_jw = np.zeros((5,7))
    for row in customer:
        day = row['day_label']
        shift = row['shift']
        demand = row['shift_demand']
        d = days[day]
        s = enumerate_shift[shift]
        d_jw[d,s] = demand
    for d in range(5):
        for j in range(7):
            prob += pulp.lpSum(x[i, j, d] for i in e_id) == d_jw[d,j]

# constraint 3: Ensure that only employees with the required skill level can be assigned to shifts
def add_constraint3(prob, x, skill_level, e_id):
    required = {}
    for a,l in enumerate_shift.items():
        required[l] = tasks_with_min_levels[a]

    for i in e_id:
        employee_level = skill_levels[skill_level[i]]
        for j in range(7):
            if employee_level < required[j]:
                for d in range(5):
                    prob += x[i,j,d] == 0
            
# constaint 4: For each shift, select the employee with the highest training level, as possible
def add_constraint4(prob, training_levels, salaries, x, e_id):
    big_value = 10000;
    prob += pulp.lpSum(
        (big_value*training_levels[i][j]-salaries[i])*x[i,j,d]
        for i in e_id
        for j in range(7)
        for d in range(5)
    )

             
def save_to_csv(customer_data):
    csv_file_path = "customer_data.csv"
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Day", "Shift", "Shift Demand"])
        for day, shift, shift_demand in customer_data:
            writer.writerow([day, shift, shift_demand])