"""Iteratory nieskończone (zadanie 7.6)."""

import random
from itertools import cycle, islice


class AlternatingBits:
    """(a) Iterator zwracający 0, 1, 0, 1, ..."""

    def __init__(self):
        self.value = 1  # pierwsze wywołanie next() da 0

    def __iter__(self):
        return self

    def __next__(self):
        self.value = 1 - self.value
        return self.value


class RandomWalk:
    """(b) Iterator zwracający losowo "N", "E", "S" lub "W"."""

    DIRECTIONS = ("N", "E", "S", "W")

    def __iter__(self):
        return self

    def __next__(self):
        return random.choice(self.DIRECTIONS)


class WeekDays:
    """(c) Iterator zwracający 0, 1, ..., 6, 0, 1, ... (numery dni tygodnia)."""

    def __init__(self):
        self.day = -1  # pierwsze wywołanie next() da 0

    def __iter__(self):
        return self

    def __next__(self):
        self.day = (self.day + 1) % 7
        return self.day



def alternating_bits_gen():
    while True:
        yield 0
        yield 1


def random_walk_gen():
    while True:
        yield random.choice(("N", "E", "S", "W"))


def weekdays_gen():
    return cycle(range(7))


if __name__ == "__main__":
    print("(a)", list(islice(AlternatingBits(), 10)))
    print("(b)", list(islice(RandomWalk(), 10)))
    print("(c)", list(islice(WeekDays(), 15)))

  
    x = y = 0
    for step in islice(RandomWalk(), 1000):
        if step == "N":
            y += 1
        elif step == "S":
            y -= 1
        elif step == "E":
            x += 1
        else:
            x -= 1
    print("Pozycja po 1000 krokach:", (x, y))