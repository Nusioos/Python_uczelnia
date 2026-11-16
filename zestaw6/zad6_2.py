import math


class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstruktor
        self.x = x
        self.y = y

    def __str__(self):  # "(x, y)"
        return "({}, {})".format(self.x, self.y)

    def __repr__(self):  # "Point(x, y)"
        return "Point({}, {})".format(self.x, self.y)

    def __eq__(self, other):  # obsługa point1 == point2
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):  # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):  # v1 + v2
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):  # v1 - v2
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):  # v1 * v2
        return self.x * other.x + self.y * other.y

    def cross(self, other):  # v1 x v2
        return self.x * other.y - self.y * other.x

    def length(self):  
        return math.hypot(self.x, self.y)

    def __hash__(self):
        return hash((self.x, self.y))  # bazujemy na tuple immutable points



import unittest


class TestPoint(unittest.TestCase):

    def setUp(self):
        self.p1 = Point(3, 4)
        self.p2 = Point(1, -2)

    def test_init(self):
        self.assertEqual(self.p1.x, 3)
        self.assertEqual(self.p1.y, 4)

    def test_str(self):
        self.assertEqual(str(self.p1), "(3, 4)")
        self.assertEqual(str(self.p2), "(1, -2)")

    def test_repr(self):
        self.assertEqual(repr(self.p1), "Point(3, 4)")
        self.assertEqual(repr(self.p2), "Point(1, -2)")

    def test_eq(self):
        self.assertTrue(Point(3, 4) == self.p1)
        self.assertFalse(self.p1 == self.p2)
        self.assertFalse(Point(3, 5) == self.p1)
        self.assertFalse(self.p1 == (3, 4))  # inny typ

    def test_ne(self):
        self.assertTrue(self.p1 != self.p2)
        self.assertFalse(self.p1 != Point(3, 4))

    def test_add(self):
        self.assertEqual(self.p1 + self.p2, Point(4, 2))
        self.assertEqual(self.p1 + Point(0, 0), self.p1)

    def test_sub(self):
        self.assertEqual(self.p1 - self.p2, Point(2, 6))
        self.assertEqual(self.p1 - self.p1, Point(0, 0))

    def test_mul(self): 
        self.assertEqual(self.p1 * self.p2, 3 * 1 + 4 * (-2))
        self.assertEqual(Point(1, 0) * Point(0, 1), 0)  # prostopadłe

    def test_cross(self):  
        self.assertEqual(self.p1.cross(self.p2), 3 * (-2) - 4 * 1)
        self.assertEqual(Point(1, 0).cross(Point(0, 1)), 1)
        self.assertEqual(Point(0, 1).cross(Point(1, 0)), -1)
        self.assertEqual(self.p1.cross(self.p1), 0)  # równoległe

    def test_length(self):
        self.assertEqual(self.p1.length(), 5.0)
        self.assertEqual(Point(0, 0).length(), 0.0)
        self.assertAlmostEqual(Point(1, 1).length(), math.sqrt(2))

    def test_hash(self):
        self.assertEqual(hash(Point(3, 4)), hash(self.p1))
        self.assertEqual(len({Point(1, 2), Point(1, 2), Point(2, 1)}), 2)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()