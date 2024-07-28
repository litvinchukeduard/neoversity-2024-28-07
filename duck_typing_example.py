from datetime import datetime


class NameNotValidError(ValueError):
    pass


class Person:
    def __init__(self, name: str, date_of_birth: str) -> None:
        if len(name) == 0:
            raise NameNotValidError("Name should not be blank")
        self.name = name
        # self.date_of_birth = date_of_birth
        today = datetime.today()
        self.age = today.year - datetime.strptime(date_of_birth, '%d.%m.%Y').year

    def quack(self):
        print("Quacking like a duck")


class Employee(Person):
    pass


class Duck:
    def quack(self):
        print("Quacking")


animals = [Person('Igor', '20.01.2000'), Employee("Mary", '01.01.2000'), Duck()]
for animal in animals:
    animal.quack()