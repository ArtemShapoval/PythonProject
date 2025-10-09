def input_employees():
    employees = {}
    while True:
        name = input("Введіть ім'я співробітника (або 'stop' для завершення): ")
        if name.lower() == "stop":
            break
        try:
            salary = float(input("Введіть місячну зарплату співробітника: "))
            days = int(input("Введіть кількість відпрацьованих днів: "))
        except ValueError:
            print("__X__ Неправильний формат даних! Спробуйте ще раз. __X__")
            continue

        employees[name] = {
            "salary": salary,
            "days": days
        }
    return employees
