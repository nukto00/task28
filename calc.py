# Сапунов Андрей Сергеевич
# группа 44-22-122
# вариант 28, см. task.png

import math


class Calc:

    def __init__(self, x):
        try:
            xf = float(x)
            if xf >= 0:
                y = math.sqrt(pow(xf, 3))
            else:
                y = math.log(abs(xf))
            self.y = y
        except Exception as e:
            raise e
