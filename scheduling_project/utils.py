from config import enumerate_shift, tasks_with_min_levels, skill_levels
import numpy as np
import random
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

def solve(employees_data, num_employees, customers, skill_levels, tasks_with_min_levels):
    prob = pulp.LpProblem("Shift_Assignment", pulp.LpMinimize)

    # Create variable X_ijd
    x = pulp.LpVariable.dicts("x", [(i, j, d) for i in range(num_employees) for j in range(7) for d in range(5)], cat="Binary")
    salaries = [employee[2] for employee in employees_data]
    training_levels = [e[1] for e in employees_data]

    prob += pulp.lpSum(
        x[i, j, d] * salaries[i] 
        for i in range(num_employees) 
        for j in range(7) 
        for d in range(5)
    )

    add_constraint1(prob, x, num_employees)
    add_constraint2(prob, customers, x, num_employees)
    add_constraint3(prob, employees_data, customers, num_employees, x, skill_levels, tasks_with_min_levels)

    prob.solve()
    print("Status:", pulp.LpStatus[prob.status])

# constraint 1: An employee can be assigned to at most one shift for each day
def add_constraint1(prob, x, num_employees):
    for i in range(num_employees):
        for d in range(5):
            prob += pulp.lpSum(x[i, j, d] for j in range(7)) <= 1

# constraint 2: Each shifts has the required number of employees at day d
def add_constraint2(prob, customer, x, num_employees):
    d_jw = np.zeros((5,7))
    for day, shift, demand in customer:
        d_jw[day, shift] = demand
    for d in range(5):
        for j in range(7):
            prob += pulp.lpSum(x[i, j, d] for i in range(num_employees)) == d_jw[d, j]

# constraint 3: Ensure that only employees with the required skill level can be assigned to shifts
def add_constraint3(prob, employees_data, customers, num_employees, x, skill_levels, tasks_with_min_levels):
    z = {} 
    for day, shift, demand in customers:
        z[(enumerate_shift[shift])] = tasks_with_min_levels[shift]
    for i in range(num_employees):
        for j in range(7):
            for d in range(5):
                    # if skill level of employee i is not as high as skill required to do shift j
                    if skill_levels[employees_data[i][0]] < z[(j)]:
                        # don't assign employee i to shift j at any day d
                        prob += x[i, j, d] == 0
             
def save_to_csv(customer_data):
    csv_file_path = "customer_data.csv"
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Day", "Shift", "Shift Demand"])
        for day, shift, shift_demand in customer_data:
            writer.writerow([day, shift, shift_demand])