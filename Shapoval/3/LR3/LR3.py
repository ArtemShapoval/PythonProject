class Person:
    def __init__(self, name, surname, grade=1):
        self.name = name
        self.surname = surname
        self.grade = grade

    def info(self):
        return f"Студент: {self.name} {self.surname}, оцінка: {self.grade}"

    def __del__(self):
        print(f"Ви отримали стипендію {self.name} {self.surname}")

# Створення об'єктів
student1 = Person("Артем", "Шаповал", 95)
student2 = Person("Денис", "Руденок", 96)
student3 = Person("Роман", "Шаров", 90)

# Виведення інформації
print(student1.info())
print(student2.info())
print(student3.info())

# Очікування натискання Enter
input("\nНатисніть Enter для завершення програми...")
