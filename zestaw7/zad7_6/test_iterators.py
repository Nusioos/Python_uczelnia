import unittest
from itertools import islice

from iterators import (AlternatingBits, RandomWalk, WeekDays,
                       alternating_bits_gen, random_walk_gen, weekdays_gen)


class TestIterators(unittest.TestCase):

    def test_alternating_bits(self):
        expected = [0, 1] * 5
        self.assertEqual(list(islice(AlternatingBits(), 10)), expected)
        self.assertEqual(list(islice(alternating_bits_gen(), 10)), expected)

    def test_random_walk(self):
        for it in (RandomWalk(), random_walk_gen()):
            steps = list(islice(it, 200))
            self.assertEqual(len(steps), 200)
            self.assertTrue(set(steps) <= {"N", "E", "S", "W"})
            self.assertEqual(set(steps), {"N", "E", "S", "W"})  # praktycznie pewne

    def test_weekdays(self):
        expected = list(range(7)) * 3
        self.assertEqual(list(islice(WeekDays(), 21)), expected)
        self.assertEqual(list(islice(weekdays_gen(), 21)), expected)

    def test_iterator_protocol(self):
        it = WeekDays()
        self.assertIs(iter(it), it)
        self.assertEqual(next(it), 0)
        self.assertEqual(next(it), 1)


if __name__ == "__main__":
    unittest.main()