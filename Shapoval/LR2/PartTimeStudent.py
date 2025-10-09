from Person import Person

class PartTimeStudent(Person):
    def __init__(self, name, age, prac_score, prac_count, exam_scr):
        super().__init__(name, age, prac_score, prac_count, exam_scr)

    def total_score(self):
        S_pr = self.avg_practice_score()
        S_ex = self.exam_scr
        return round(S_pr * 0.5 + S_ex * 0.5, 2)

    def display_info(self):
        print(f"Форма навчання: заочна")
        print(f"Ім'я: {self.name}, Вік: {self.age}")
