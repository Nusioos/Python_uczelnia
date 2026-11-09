from math import gcd


def _check(frac):
    """Sprawdza poprawność ułamka"""
    if len(frac) != 2:
        raise ValueError("ułamek musi mieć postać [licznik, mianownik]")
    if frac[1] == 0:
        raise ZeroDivisionError("mianownik nie może być zerem")


def normalize(frac):
    """Zwraca ułamek skrocony z dodatnim mianownikiem."""
    _check(frac)
    num, den = frac
    if num == 0:
        return [0, 1]
    if den < 0:
        num, den = -num, -den
    d = gcd(num, den)
    return [num // d, den // d]


def add_frac(frac1, frac2):        
    _check(frac1)
    _check(frac2)
    return normalize([frac1[0] * frac2[1] + frac2[0] * frac1[1],
                      frac1[1] * frac2[1]])


def sub_frac(frac1, frac2):        
    _check(frac1)
    _check(frac2)
    return normalize([frac1[0] * frac2[1] - frac2[0] * frac1[1],
                      frac1[1] * frac2[1]])


def mul_frac(frac1, frac2):      
    _check(frac1)
    _check(frac2)
    return normalize([frac1[0] * frac2[0], frac1[1] * frac2[1]])


def div_frac(frac1, frac2):        
    _check(frac1)
    _check(frac2)
    if frac2[0] == 0:
        raise ZeroDivisionError("dzielenie przez zero")
    return normalize([frac1[0] * frac2[1], frac1[1] * frac2[0]])


def is_positive(frac):            
    _check(frac)
    return frac[0] * frac[1] > 0


def is_zero(frac):              
    _check(frac)
    return frac[0] == 0


def cmp_frac(frac1, frac2):       
    _check(frac1)
    _check(frac2)
    left = frac1[0] * frac2[1] * frac1[1] * frac2[1]
    right = frac2[0] * frac1[1] * frac1[1] * frac2[1]

    return (left > right) - (left < right)


def frac2float(frac):              
    _check(frac)
    return frac[0] / frac[1]



import unittest


class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_normalize(self):
        self.assertEqual(normalize([6, 2]), [3, 1])
        self.assertEqual(normalize([1, -2]), [-1, 2])
        self.assertEqual(normalize([-1, -2]), [1, 2])
        self.assertEqual(normalize([0, 5]), self.zero)

    def test_invalid(self):
        with self.assertRaises(ZeroDivisionError):
            add_frac([1, 0], [1, 2])
        with self.assertRaises(ZeroDivisionError):
            div_frac([1, 2], [0, 3])
        with self.assertRaises(ValueError):
            add_frac([1, 2, 3], [1, 2])

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac([1, 2], [1, 2]), [1, 1])
        self.assertEqual(add_frac([-1, 2], [1, 2]), self.zero)
        self.assertEqual(add_frac([1, -2], [1, -2]), [-1, 1])
        self.assertEqual(add_frac([0, 2], [6, 2]), [3, 1])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(sub_frac([1, 3], [1, 2]), [-1, 6])
        self.assertEqual(sub_frac([1, 2], [1, 2]), self.zero)
        self.assertEqual(sub_frac([1, 2], [1, -2]), [1, 1])
        self.assertEqual(sub_frac([3, 1], [0, 2]), [3, 1])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([1, 2], [2, 3]), [1, 3])
        self.assertEqual(mul_frac([-1, 2], [1, -2]), [1, 4])
        self.assertEqual(mul_frac([3, 1], [0, 2]), self.zero)
        self.assertEqual(mul_frac([6, 2], [1, 3]), [1, 1])

    def test_div_frac(self):
        self.assertEqual(div_frac([1, 2], [1, 4]), [2, 1])
        self.assertEqual(div_frac([1, 2], [-1, 4]), [-2, 1])
        self.assertEqual(div_frac([0, 2], [3, 5]), self.zero)
        self.assertEqual(div_frac([6, 2], [3, 1]), [1, 1])

    def test_is_positive(self):
        self.assertTrue(is_positive([1, 2]))
        self.assertTrue(is_positive([-1, -2]))
        self.assertFalse(is_positive([-1, 2]))
        self.assertFalse(is_positive([1, -2]))
        self.assertFalse(is_positive([0, 1]))

    def test_is_zero(self):
        self.assertTrue(is_zero([0, 1]))
        self.assertTrue(is_zero([0, 2]))
        self.assertTrue(is_zero([0, -3]))
        self.assertFalse(is_zero([1, 2]))
        self.assertFalse(is_zero([-3, 1]))

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([1, 2], [1, 3]), 1)
        self.assertEqual(cmp_frac([1, 3], [1, 2]), -1)
        self.assertEqual(cmp_frac([-1, 2], [1, -2]), 0)
        self.assertEqual(cmp_frac([6, 2], [3, 1]), 0)
        self.assertEqual(cmp_frac([0, 1], [0, 2]), 0)
        self.assertEqual(cmp_frac([-1, 2], [0, 1]), -1)
        self.assertEqual(cmp_frac([1, -3], [1, -2]), 1)    # -1/3 > -1/2

    def test_frac2float(self):
        self.assertEqual(frac2float([1, 2]), 0.5)
        self.assertEqual(frac2float([1, -2]), -0.5)
        self.assertEqual(frac2float([0, 2]), 0.0)
        self.assertAlmostEqual(frac2float([1, 3]), 0.3333333333)
        self.assertEqual(frac2float([6, 2]), 3.0)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()     