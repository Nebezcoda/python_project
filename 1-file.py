def get_string(string: str, times: int, sep: str='') -> str:
    return sep.join([string] * times)

# Ко встроенным типам данных относятся:

#     int
#     float
#     str
#     bytes
#     list
#     dict
#     set
#     frozenset
#     ...

def some_function(number: int | float) -> None:
    pass

def another_some_function(number: int | float | complex = 0) -> None:
    pass

lst_1: list[int]                # Все элементы списка lst_1 типа int
tpl_2: tuple[bool]              # Все элементы кортежа tpl_2 типа bool
tpl_3: tuple[int, bool, float]  # Кортеж tpl_3 состоит из трех элементов
                                # Первый типа int, второй типа bool, а третий типа float
set_4: set[int | float]         # Элементы множества set_4 либо int, либо float типов

def get_tuple(lst: list[float | bool]) -> tuple[int]:
    return tuple(int(num) for num in lst)

get_tuple([True,False])