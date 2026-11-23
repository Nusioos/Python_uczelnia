"""Moduł z klasą Frac reprezentującą ułamki zwykłe."""

from math import gcd


class Frac:
    """Klasa reprezentująca ułamki (immutable)."""

    def __init__(self, x=0, y=1):
        """Tworzy ułamek x/y. Akceptuje int, float oraz Frac."""
        x = self._to_ratio(x)
        y = self._to_ratio(y)

        num = x[0] * y[1]
        den = x[1] * y[0]
        if den == 0:
            raise ValueError("Mianownik nie może być zerem.")
        if den < 0:
            num, den = -num, -den
        d = gcd(num, den)
        self.x = num // d
        self.y = den // d

    @staticmethod
    def _to_ratio(value):
        """Zamienia int/float/Frac na parę (licznik, mianownik)."""
        if isinstance(value, Frac):
            return value.x, value.y
        if isinstance(value, bool):
            return int(value), 1
        if isinstance(value, int):
            return value, 1
        if isinstance(value, float):
            try:
                return value.as_integer_ratio()
            except (OverflowError, ValueError):
                raise ValueError("Niedozwolona wartość float: {}".format(value))
        raise ValueError("Nieobsługiwany typ: {}".format(type(value).__name__))

    @classmethod
    def _coerce(cls, other):
        """Zamienia other na Frac lub zwraca None, gdy typ nieobsługiwany."""
        if isinstance(other, Frac):
            return other
        if isinstance(other, (int, float)):
            return cls(other)
        return None

    def __str__(self):
        """Zwraca "x/y" lub "x" dla y=1."""
        if self.y == 1:
            return str(self.x)
        return "{}/{}".format(self.x, self.y)

    def __repr__(self):
        """Zwraca "Frac(x, y)"."""
        return "Frac({}, {})".format(self.x, self.y)

    def __eq__(self, other):
        other = self._coerce(other)
        if other is None:
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        return not result

    def __lt__(self, other):
        other = self._coerce(other)
        if other is None:
            return NotImplemented
        return self.x * other.y < other.x * self.y

    def __le__(self, other):
        other = self._coerce(other)
        if other is None:
            return NotImplemented
        return self.x * other.y <= other.x * self.y

    def __gt__(self, other):
        other = self._coerce(other)
        if other is None:
            return NotImplemented
        return self.x * other.y > other.x * self.y

    def __ge__(self, other):
        other = self._coerce(other)
        if other is None:
            return NotImplemented
        return self.x * other.y >= other.x * self.y


    def __add__(self, other): 
        other = self._coerce(other)
        if other is None:
            return NotImplemented
        return Frac(self.x * other.y + other.x * self.y, self.y * other.y)

    __radd__ = __add__  

    def __sub__(self, other):
        other = self._coerce(other)
        if other is None:
            return NotImplemented
        return Frac(self.x * other.y - other.x * self.y, self.y * other.y)

    def __rsub__(self, other):  
    
        other = self._coerce(other)
        if other is None:
            return NotImplemented
        return Frac(other.x * self.y - self.x * other.y, self.y * other.y)

    def __mul__(self, other): 
        other = self._coerce(other)
        if other is None:
            return NotImplemented
        return Frac(self.x * other.x, self.y * other.y)

    __rmul__ = __mul__  

    def __truediv__(self, other): 
        other = self._coerce(other)
        if other is None:
            return NotImplemented
        if other.x == 0:
            raise ValueError("Dzielenie przez zero.")
        return Frac(self.x * other.y, self.y * other.x)

    def __rtruediv__(self, other):  # int/frac
        other = self._coerce(other)
        if other is None:
            return NotImplemented
        if self.x == 0:
            raise ValueError("Dzielenie przez zero.")
        return Frac(other.x * self.y, other.y * self.x)


    def __pos__(self):  
        return self

    def __neg__(self):  
        return Frac(-self.x, self.y)

    def __invert__(self):  
        if self.x == 0:
            raise ValueError("Odwrotność zera nie istnieje.")
        return Frac(self.y, self.x)

    def __float__(self):  
        return self.x / self.y

    def __hash__(self):
     
        if self.y == 1:
            return hash(self.x)
        return hash(float(self))

    def limit_denominator(self, max_denominator=1000000):
        """Zwraca najbliższy ułamek o mianowniku <= max_denominator."""
        if max_denominator < 1:
            raise ValueError("max_denominator musi być >= 1.")
        if self.y <= max_denominator:
            return Frac(self.x, self.y)

        p0, q0, p1, q1 = 0, 1, 1, 0
        n, d = self.x, self.y
        while True:
            a = n // d
            q2 = q0 + a * q1
            if q2 > max_denominator:
                break
            p0, q0, p1, q1 = p1, q1, p0 + a * p1, q2
            n, d = d, n - a * d
        k = (max_denominator - q0) // q1
        bound1 = Frac(p0 + k * p1, q0 + k * q1)
        bound2 = Frac(p1, q1)
        target = Frac(self.x, self.y)
        if abs(float(bound2 - target)) <= abs(float(bound1 - target)):
            return bound2
        return bound1