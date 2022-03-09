import Person

class Employee(Person):
    def __init__(self, workingArea) -> None:
        super().__init__()
        
        self.workingArea = workingArea