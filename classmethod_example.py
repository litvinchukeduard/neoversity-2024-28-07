

class Parent:
    property = 1

    my_str = "Hello"
    
    @classmethod
    def some_method(cls):
        print(cls.property)
        
class Child(Parent):
    property = 2

    @classmethod
    def some_method(cls):
        # print(super().property)
        print(cls.__bases__)

Child.some_method()

# parent_one = Parent()
# parent_two = Parent()

# child_one = Child()

