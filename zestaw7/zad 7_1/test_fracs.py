import unittest

from fracs import Frac


class TestFrac(unittest.TestCase):

    def setUp(self):
        self.half = Frac(1, 2)
        self.third = Frac(1, 3)

    def test_init_and_normalization(self):
        self.assertEqual((Frac(2, 4).x, Frac(2, 4).y), (1, 2))
        self.assertEqual((Frac(1, -2).x, Frac(1, -2).y), (-1, 2))
        self.assertEqual((Frac(-1, -2).x, Frac(-1, -2).y), (1, 2))
        self.assertEqual(Frac(), Frac(0, 1))
        self.assertEqual(Frac(5), Frac(5, 1))

    def test_zero_denominator(self):
        with self.assertRaises(ValueError):
            Frac(1, 0)

    def test_invalid_type(self):
        with self.assertRaises(ValueError):
            Frac("a", 2)

    def test_float_init(self):
        self.assertEqual(Frac(0.5), Frac(1, 2))
        self.assertEqual(Frac(0.4).limit_denominator(1000), Frac(2, 5))
        self.assertEqual(Frac(3.14159).limit_denominator(1000), Frac(355, 113))
        self.assertEqual(Frac(0.4), Frac(3602879701896397, 9007199254740992))

    def test_float_invalid(self):
        with self.assertRaises(ValueError):
            Frac(float("inf"))
        with self.assertRaises(ValueError):
            Frac(float("nan"))

    # Napisy
    def test_str(self):
        self.assertEqual(str(Frac(1, 2)), "1/2")
        self.assertEqual(str(Frac(-3, 6)), "-1/2")
        self.assertEqual(str(Frac(4, 2)), "2")
        self.assertEqual(str(Frac(0)), "0")

    def test_repr(self):
        self.assertEqual(repr(Frac(1, 2)), "Frac(1, 2)")
        self.assertEqual(repr(eval(repr(Frac(3, 7)))), "Frac(3, 7)")

    # Porównywanie
    def test_eq_ne(self):
        self.assertTrue(Frac(1, 2) == Frac(2, 4))
        self.assertTrue(Frac(2) == 2)
        self.assertTrue(2 == Frac(2))
        self.assertTrue(Frac(1, 2) == 0.5)
        self.assertTrue(Frac(1, 2) != Frac(1, 3))
        self.assertTrue(Frac(1, 2) != 1)
        self.assertFalse(Frac(1, 2) == "x")

    def test_ordering(self):
        self.assertTrue(self.third < self.half)
        self.assertTrue(self.third <= self.half)
        self.assertTrue(self.half <= Frac(2, 4))
        self.assertTrue(self.half > self.third)
        self.assertTrue(self.half >= self.third)
        self.assertTrue(Frac(-1, 2) < Frac(1, 3))
        self.assertTrue(Frac(1, 2) < 1)
        self.assertTrue(1 > Frac(1, 2))
        self.assertTrue(0 < Frac(1, 2))
        self.assertTrue(Frac(1, 2) > 0.25)

    def test_ordering_invalid(self):
        with self.assertRaises(TypeError):
            Frac(1, 2) < "a"

    # Dodawanie
    def test_add(self):
        self.assertEqual(self.half + self.third, Frac(5, 6))
        self.assertEqual(self.half + 1, Frac(3, 2))
        self.assertEqual(1 + self.half, Frac(3, 2))
        self.assertEqual(self.half + 0.5, Frac(1))
        self.assertEqual(0.5 + self.half, Frac(1))

    # Odejmowanie
    def test_sub(self):
        self.assertEqual(self.half - self.third, Frac(1, 6))
        self.assertEqual(self.half - 1, Frac(-1, 2))
        self.assertEqual(1 - self.half, Frac(1, 2))
        self.assertEqual(2 - Frac(1, 3), Frac(5, 3))
        self.assertEqual(0.5 - self.half, Frac(0))

    # Mnożenie
    def test_mul(self):
        self.assertEqual(self.half * self.third, Frac(1, 6))
        self.assertEqual(self.half * 4, Frac(2))
        self.assertEqual(4 * self.half, Frac(2))
        self.assertEqual(self.half * 0.5, Frac(1, 4))
        self.assertEqual(self.half * 0, Frac(0))

    # Dzielenie
    def test_truediv(self):
        self.assertEqual(self.half / self.third, Frac(3, 2))
        self.assertEqual(self.half / 2, Frac(1, 4))
        self.assertEqual(2 / self.half, Frac(4))
        self.assertEqual(1 / Frac(-2, 3), Frac(-3, 2))
        self.assertEqual(self.half / 0.5, Frac(1))

    def test_div_by_zero(self):
        with self.assertRaises(ValueError):
            self.half / 0
        with self.assertRaises(ValueError):
            self.half / Frac(0)
        with self.assertRaises(ValueError):
            1 / Frac(0)

    def test_unsupported_operand(self):
        with self.assertRaises(TypeError):
            Frac(1, 2) + "a"
        with self.assertRaises(TypeError):
            "a" * Frac(1, 2)

    # Operatory jednoargumentowe
    def test_unary(self):
        self.assertEqual(+self.half, self.half)
        self.assertEqual(-self.half, Frac(-1, 2))
        self.assertEqual(-Frac(-1, 2), Frac(1, 2))
        self.assertEqual(~Frac(2, 3), Frac(3, 2))
        self.assertEqual(~Frac(-2, 3), Frac(-3, 2))
        self.assertEqual(abs(Frac(-1, 2)) if hasattr(Frac, "__abs__")
                         else Frac(1, 2), Frac(1, 2))

    def test_invert_zero(self):
        with self.assertRaises(ValueError):
            ~Frac(0)

    def test_float(self):
        self.assertEqual(float(Frac(1, 2)), 0.5)
        self.assertAlmostEqual(float(Frac(1, 3)), 1 / 3)
        self.assertEqual(float(Frac(-5, 4)), -1.25)

    # Hash
    def test_hash(self):
        self.assertEqual(hash(Frac(1, 2)), hash(Frac(2, 4)))
        self.assertEqual(hash(Frac(2)), hash(2))
        self.assertEqual(set([2]), set([Frac(2)]))
        self.assertEqual(len({Frac(1, 2), Frac(2, 4), Frac(3, 6)}), 1)

    # limit_denominator
    def test_limit_denominator(self):
        self.assertEqual(Frac(3.14159).limit_denominator(1000), Frac(355, 113))
        self.assertEqual(Frac(1, 3).limit_denominator(10), Frac(1, 3))
        with self.assertRaises(ValueError):
            Frac(1, 3).limit_denominator(0)


if __name__ == "__main__":
    unittest.main()