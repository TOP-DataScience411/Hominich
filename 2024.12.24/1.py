from math import sqrt


class Point:
    def __init__(self, x: float, y: float):
        self._x = x
        self._y = y

    @property
    def x(self) -> float:
        return self._x

    @x.setter
    def x(self, value):
        raise TypeError("'Point' object does not support coordinate assignment")

    @property
    def y(self) -> float:
        return self._y

    @y.setter
    def y(self, value):
        raise TypeError("'Point' object does not support coordinate assignment")

    def __eq__(self, other) -> bool:
        return isinstance(other, Point) and self.x == other.x and self.y == other.y

    def __repr__(self) -> str:
        return f"({self.x},{self.y})"

    def __str__(self) -> str:
        return self.__repr__()


class Line:
    def __init__(self, start: Point, end: Point):
        if not isinstance(start, Point) or not isinstance(end, Point):
            raise TypeError("'start' and 'end' must be instances of Point")
        self._start = start
        self._end = end
        self._length = self._length_calc(start, end)

    @staticmethod
    def _length_calc(point1: Point, point2: Point) -> float:
        return sqrt((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2)

    @property
    def start(self) -> Point:
        return self._start

    @start.setter
    def start(self, value: Point):
        if not isinstance(value, Point):
            raise TypeError("'start' attribute of 'Line' object supports only 'Point' object assignment")
        self._start = value
        self._length = self._length_calc(self._start, self._end)

    @property
    def end(self) -> Point:
        return self._end

    @end.setter
    def end(self, value: Point):
        if not isinstance(value, Point):
            raise TypeError("'end' attribute of 'Line' object supports only 'Point' object assignment")
        self._end = value
        self._length = self._length_calc(self._start, self._end)

    @property
    def length(self) -> float:
        return self._length

    @length.setter
    def length(self, value):
        raise TypeError("'Line' object does not support length assignment")

    def __repr__(self) -> str:
        return f"{self.start}———{self.end}"

    def __str__(self) -> str:
        return self.__repr__()


class Polygon(list):
    def __init__(self, side1: Line, side2: Line, side3: Line, *sides: Line):
        super().__init__([side1, side2, side3, *sides])
        if len(self) < 3:
            raise ValueError("A polygon must have at least three sides")

    @property
    def perimeter(self) -> float:
        if not self._is_closed():
            raise ValueError("line items doesn't form a closed polygon")
        return sum(line.length for line in self)

    def _is_closed(self) -> bool:
        return all(self[i].end == self[i + 1].start for i in range(len(self) - 1)) and self[-1].end == self[0].start

# python3 -i 1.py
# >>> p1 = Point(0, 3)
# >>> p2 = Point(4, 0)
# >>> p3 = Point(8, 3)
# >>> p1
# (0,3)
# >>> repr(p1) == str(p1)
# True
# >>> p1 == Point(0, 3)
# True
# >>> p1.x, p1.y
# (0, 3)
# >>> p2.y = 5
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "/home/margarita/Документы/DataScience411/Hominich/2024.12.24/1.py", line 23, in y
#     raise TypeError("'Point' object does not support coordinate assignment")
# TypeError: 'Point' object does not support coordinate assignment
# >>> l1 = Line(p1, p2)
# >>> l2 = Line(p2, p3)
# >>> l3 = Line(p3, p1)
# >>> l1
# (0,3)———(4,0)
# >>> repr(l1) == str(l1)
# True
# >>> l1.length
# 5.0
# >>> l1.length = 10
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "/home/margarita/Документы/DataScience411/Hominich/2024.12.24/1.py", line 75, in length
#     raise TypeError("'Line' object does not support length assignment")
# TypeError: 'Line' object does not support length assignment
# >>> l3.start = 12
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "/home/margarita/Документы/DataScience411/Hominich/2024.12.24/1.py", line 54, in start
#     raise TypeError("'start' attribute of 'Line' object supports only 'Point' object assignment")
# TypeError: 'start' attribute of 'Line' object supports only 'Point' object assignment
# >>> pol1 = Polygon(l1, l2, l3)
# >>> pol1.perimeter
# 18.0
# >>> pol1.perimeter = 20
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: property 'perimeter' of 'Polygon' object has no setter
# >>> l3.end = Point(-10, -10)
# >>> pol1.perimeter
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "/home/margarita/Документы/DataScience411/Hominich/2024.12.24/1.py", line 93, in perimeter
#     raise ValueError("line items doesn't form a closed polygon")
# ValueError: line items doesn't form a closed polygon
# >>>
#
