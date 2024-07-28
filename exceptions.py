


class NameNotValidError(ValueError):
    def __init__(self, name) -> None:
        super().__init__(f'Name not valid for name {name}')


try:
    1 / 0
except ZeroDivisionError as e:
    raise ExceptionGroup('We have some problems', [NameNotValidError(), e])

name = 'Igor'
# raise NameNotValidError(name)

# raise ExceptionGroup('We have some problems', [NameNotValidError(name), ])