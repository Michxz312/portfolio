skill_levels = {"entry-level": 0, "junior": 1, "senior": 2, "manager": 3}

tasks_with_min_levels = {
    "Account opening": 0,
    "Credit card application": 0,
    "Loan Application": 1,
    "Mortgage Consultation": 2,
    "Retirement planning": 2,
    "Financial advising": 2,
    "Wealth management": 3
}

distribution = {
    "entry-level": 0.4,
    "junior": 0.3,
    "senior": 0.2,
    "manager": 0.1
}

salary_weight = {
    "K": 1000,
    "a": 3,
    "b": 5,
    "c": 10,
    "d": 35,
}

days = {"Monday": 0, 
        "Tuesday": 1, 
        "Wednesday": 2, 
        "Thursday": 3,
        "Friday": 4
}

demand_distribution = {
    "Account opening": 0.2,
    "Credit card application": 0.15,
    "Loan Application": 0.2,
    "Mortgage Consultation": 0.1,
    "Retirement planning": 0.2,
    "Financial advising": 0.1,
    "Wealth management": 0.05
}

day_label = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

shift_label = ['Account opening', 'Credit card application', 'Loan Application', 'Mortgage Consultation', 
               'Retirement planning', 'Financial advising', 'Wealth management']

enumerate_shift = {
    'Account opening': 0, 
    'Credit card application': 1, 
    'Loan Application': 2, 
    'Mortgage Consultation': 3, 
    'Retirement planning': 4, 
    'Financial advising': 5, 
    'Wealth management': 6
}