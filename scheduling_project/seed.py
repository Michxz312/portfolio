import pymysql
from config import skill_levels, tasks_with_min_levels, distribution, salary_weight, days, demand_distribution, day_label, shift_label, enumerate_shift
from utils import generate_employee_data_custom_distribution, generate_customer_data_custom_distribution
from db import create_connection, insert_employees, insert_customer

def reset_data():
    con = create_connection()
    cursor = con.cursor()
    cursor.execute("DELETE FROM employees")
    cursor.execute("DELETE FROM customers")
    con.commit()
    cursor.close()
    con.close()

def seed():
    num_employees = 10
    employees_data = generate_employee_data_custom_distribution(num_employees, skill_levels, tasks_with_min_levels, salary_weight, distribution)
    num_customer = 5
    customer_data = generate_customer_data_custom_distribution(num_customer, days, demand_distribution)

    reset_data()
    
    insert_employees(employees_data)
    insert_customer(customer_data)
    

if __name__ == "__main__":
    seed()
