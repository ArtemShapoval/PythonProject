from input_module import input_employees
from salary_module import show_salaries


def print_names_recursive(names, index=0):
    if index < len(names):
        print(names[index])
        print_names_recursive(names, index + 1)


if __name__ == "__main__":
    employees = input_employees()

    print("\n -*- Зарплати співробітників: -*-")
    show_salaries(employees)

    print("\n -*- Імена співробітників (рекурсивно): -*-")
    print_names_recursive(list(employees.keys()))
