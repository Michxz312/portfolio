import numpy as np
import random
import csv
import pandas as pd

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

def save_to_csv(customer_data):
    csv_file_path = "customer_data.csv"
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Day", "Shift", "Shift Demand"])
        for day, shift, shift_demand in customer_data:
            writer.writerow([day, shift, shift_demand])