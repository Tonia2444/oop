class Wizard:
    def __init__(self, name, house):
        if not name:
            raise ValueError("missing name")
        self.name = name



class Student(Wizard):
    def __init__(self, name, house):
        supper().__init__(name)
        self.house = house

        ...


class Proffesor(Wizard):
    def __init__(self, name, subject):
        supper().__init__(name)
        self.subject = subject

    ...


wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defense Against the Dark Arts")

            
