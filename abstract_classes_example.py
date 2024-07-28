from abc import ABC, abstractmethod


class Quacker(ABC):

    my_property = 1
    
    def walk(self):
        print('Walking!')

    @abstractmethod
    def quack(self):
        raise NotImplementedError()


class Duck(Quacker):
    
    def quack(self):
        print("Quack!") 
    


# my_object = Quacker()
duck = Duck()
duck.quack()
duck.walk()

