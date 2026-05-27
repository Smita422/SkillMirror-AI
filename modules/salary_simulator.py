import random

def salary_growth(role):

    base_salary = {
        'AI Engineer': 700000,
        'Data Scientist': 650000,
        'ML Engineer': 750000,
        'Backend Developer': 500000,
        'Frontend Developer': 450000,
        'Cloud Engineer': 800000,
        'AI Architect': 1200000
    }

    start = base_salary.get(role, 400000)

    growth = {
        'Year 1': start,
        'Year 3': start + random.randint(300000, 700000),
        'Year 5': start + random.randint(1000000, 2500000)
    }

    return growth