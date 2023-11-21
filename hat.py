import random

class Hat:
    houses = ["underG", "stadium", "yoaco", "adenike"]
        
    @classmethod
    def sort(cls, name):
        house = random.choice(cls.houses)
        print(name, "is in", house)


Hat.sort("Tonia")
