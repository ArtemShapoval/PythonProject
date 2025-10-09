def calculate_salary(salary, days):
    return (salary / 30) * days


def show_salaries(employees):
    for name, data in employees.items():
        monthly_salary = calculate_salary(data["salary"], data["days"])
        print(f"{name}: {monthly_salary:.2f} грн")
