from collections import UserDict
'''
Написати клас Zoo, який буде тримати в собі тварин 
иа сортувати їх по вальерах
'''

'''
{
    'fish': [...],
    'lions': [...],
    'zebras': [...]
}

'''


class Mammal:

    def walk(self):
        print("Walking")


class Fish:

    def swim(self):
        print("Swimming")


# class Dolphin(Mammal, Fish):
class Dolphin(Fish):

    def __init__(self, name) -> None:
        super().__init__()
        self.name = name

    def walk(self):
        raise TypeError
    

class Lion(Mammal):
    pass


class Duck(Mammal, Fish):
    pass



class Zoo(UserDict):
    # def __init__(self) -> None:
    #     super().__init__()

    def put_animal_in_enclosure(self, enclosure_name: str, animal):
        if enclosure_name in self:
            self[enclosure_name].append(animal)
            # return
        else:
            self[enclosure_name] = [animal]

    def add_animal(self, animal):
        # self.data['fish'].append(animal)
        # self['fish'].append(animal)

        # if type(animal) == Fish:
        #     pass
        # elif type(animal) == Lion:
        #     pass
        # elif type(animal) == Duck:
        #     pass

        # if isinstance(animal, Duck)

        match animal:
            case Lion():
                self.put_animal_in_enclosure('lion', animal)
                print('Added to Lion')
            case Mammal():
                self.put_animal_in_enclosure('mammal', animal)
                print('Added to Mammal')
            case Dolphin():
                self.put_animal_in_enclosure('dolphin', animal)
                print('Added to Dolphin')
            case _:
                self.put_animal_in_enclosure('general', animal)
                print('Added to General')





# zoo = UserDict()
# my_dict = dict()

# zoo["fish"] = []
# my_dict["fish"] = []

# print(zoo)
# print(my_dict)

lion = Lion()
fish = Fish()

zoo = Zoo()
zoo.add_animal(lion)

zoo.add_animal(fish)

print(zoo)
# zoo.put_animal_in_enclosure('fish', fish)
# zoo.put_animal_in_enclosure('lion', lion)
# print(zoo)
