from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age, prac_score=0, prac_count=0, exam_scr=0):
        self.name = name
        self.age = age
        self.prac_score = prac_score
        self.prac_count = prac_count
        self.exam_scr = exam_scr

    def avg_practice_score(self):
        if self.prac_count != 0:
            return self.prac_score / self.prac_count
        return 0

    @abstractmethod
    def total_score(self):
        pass

    @abstractmethod
    def display_info(self):
        pass
