from enum import Enum, StrEnum, auto

# class Color(Enum):
#     RED = 1
#     GREEN = 2
#     BLUE = 3

# class Color(Enum):
#     RED = auto()
#     GREEN = auto()
#     BLUE = auto()

class Color(StrEnum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()

print(Color.BLUE.value)
