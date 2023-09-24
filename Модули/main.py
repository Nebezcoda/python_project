print(dir())

from functions import get_double_number as f
from data import my_dict
from classes import *


print('Это исполняемый файл')

new_variable: int = 15


if __name__ == '__main__':
    print('Код ниже не выполнится, если этот файл будет импортируемым модулем в другой исполняемый файл')
    print(f(100))
    print(my_dict)
    MyClass()
    print(dir())

    import sys
    print(sys.builtin_module_names)
    print(sys.stdlib_module_names)
    print(sys.path)