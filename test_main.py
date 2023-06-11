# Сапунов Андрей Сергеевич
# группа 44-22-122
# вариант 28, см. task.png

from unittest import TestCase
from main import Calc


class Test(TestCase):

    def test_0(self):
        res = Calc(0)
        self.assertEqual(res.y, 0)

    def test_1(self):
        res = Calc(1)
        self.assertEqual(res.y, 1)

    def test_s375(self):
        with self.assertRaises(Exception):
            Calc('3,75')

    def test_m1(self):
        res = Calc(-1)
        self.assertEqual(res.y, 0)

    def test_m25(self):
        res = Calc(-2.5)
        self.assertEqual(res.y, 0.9162907318741551)

    def test_AAA(self):
        with self.assertRaises(Exception):
            Calc('AAA')
