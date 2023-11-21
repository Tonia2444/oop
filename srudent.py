class Student:
    def __init__(self, name, house, course):
        self.name = name
        self.house = house
        self.course = course


    def __str__(self):
        return (f"{self.name} from {self.house} studying {self.course}")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("missing name")
        self._name = name
    
    @property
    def house(self):
        return self._house
    
    @house.setter
    def house(self, house):
        if house not in ["underG", "adenike", "yoaco", "stadium"]:
            raise ValueError("invalid house")
        self._house = house

    @property
    def course(self):
        return self._course

    @course.setter
    def course(self, course):
        if not course:
            raise ValueError("missing course")
        self._course = course
        

def main():
    student = get_student()
    print(student)

def get_student():
    name = input("name: ")
    house = input("house: ")
    course = input("course: ")
    return Student(name, house, course)


if __name__ == "__main__":
    main()









