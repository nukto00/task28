# Сапунов Андрей Сергеевич
# группа 44-22-122
# вариант 28, см. task.png

import sys
from calc import Calc


def main(args):

    for arg in args[1:]:
        try:
            res = Calc(arg)
            print(f'Для значения x={arg} - результат y={res.y:.10}')
        except Exception as e:
            print(f'Для значения x={arg} - ошибка: {e.args[0]}')


if __name__ == '__main__':
    main(sys.argv)
