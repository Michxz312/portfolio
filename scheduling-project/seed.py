from config import skill_levels, tasks_with_min_levels, distribution, salary_weight, days, demand_distribution, day_label, shift_label, enumerate_shift
from utils import generate_employee_data_custom_distribution, generate_customer_data_custom_distribution
from db import insert_employees, insert_customer



if __name__ == "__main__":
    num_employees = 10
    employees_data = generate_employee_data_custom_distribution(num_employees, skill_levels, tasks_with_min_levels, salary_weight, distribution)
    #insert_employees(employees_data)

    num_customer = 5
    customer_data = generate_customer_data_custom_distribution(num_customer, days, demand_distribution)
    #insert_customer(customer_data)
    first_five = customer_data[:5]
    last_five = customer_data[-5:]
