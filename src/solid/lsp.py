# LSP - Liskov Substitution Principle
# Objects in a program should be replaceable with instances of their
# subtypes without altering the correctness of that program.
# In other words, subclasses should be substitutable for their base classes.

# To understand more about property decorators, see:
# https://www.programiz.com/python-programming/property


class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    def area(self):
        return self._width * self._height

    def __str__(self):
        return f'width: {self._width}, height: {self._height}'


class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._width = self._height = value


def use_it(rc):
    w = rc.width
    rc.height = 10
    expected = int(w * 10)
    print(f'Expected an area of {expected}, got {rc.area()}')


if __name__ == '__main__':
    rc = Rectangle(2, 3)
    print(rc)
    use_it(rc)
    print(rc)

    sq = Square(5)
    print(sq)
    use_it(sq)
    print(sq)

    # rc.height = 10 causes the error, because we inherit from Rectangle which
    # and that class works only for a rectangle, not a square.
    # The setters violate the LSP principle.