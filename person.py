from datetime import datetime

'''
Створити помилку для випадку, коли імʼя приходить пусте
'''
class NameNotValidError(ValueError):
    pass


'''
Створити клас для людини, де ми будемо зберігати імʼя та вік
'''

# Person('Igor', '21.04.2000')

class Person:
    '''A class for a person'''
    def __init__(self, name: str, date_of_birth: str) -> None:
        if len(name) == 0:
            raise NameNotValidError("Name should not be blank")
        self.name = name
        # self.date_of_birth = date_of_birth
        today = datetime.today()
        self.age = today.year - datetime.strptime(date_of_birth, '%d.%m.%Y').year

    def say_name(self):
        print(self.name)

    # def __dir__(self):
    #     return ['name']
    

'''
Тепер створити підклас для людини, який буде зберігати інформацію про працівника
'''
class Employee(Person):
    def __init__(self, name:str, date_of_birth: str, workplace: str, salary: float) -> None:
        super().__init__(name, date_of_birth)

        self.workplace = workplace
        self.salary = salary

# person_one = Person('Igor', '21.04.2000')
# print(dir(person_one))
# # print(person_one)
# print(person_one.age)

employee_one = Employee('', '21.04.2000', 'Kyiv', 2000)
print(dir(employee_one))
employee_one.say_name()
