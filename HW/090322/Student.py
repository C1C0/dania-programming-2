import Person

class Student(Person):
    def __init__(self, grade) -> None:
        super().__init__()
        
        self.grade = grade