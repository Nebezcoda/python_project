# print('Это основной модуль main.py, его имя в процессе выполнения программы:', __name__)


# from pack_1.file_11 import a
# from pack_2.pack_21.file_211 import b


# print('a =', a)
# print('b =', b)


# print('Это основной модуль main.py, его имя в процессе выполнения программы:', __name__)


# from pack_1 import file_11
# from pack_2.pack_21 import file_211


# print('a =', file_11.a)
# print('b =', file_211.b)
# print('Словарь some_dict:', file_211.some_dict)


# print('Это основной модуль main.py, его имя в процессе выполнения программы:', __name__)


# from pack_2 import pack_21


# print('b =', pack_21.file_211.b)



# print('Это основной файл main.py, его имя в процессе выполнения программы:', __name__)


# from pack_1.file_11 import result

# print('result =', result)


# print('Это основной файл main.py, его имя в процессе выполнения программы:', __name__)


# import pack_1
# import pack_2
# from pack_2 import pack_21


# print(dir())
# print(dir(pack_1))
# print(dir(pack_2))
# print(dir(pack_21))


# print('Это основной файл main.py, его имя в процессе выполнения программы:', __name__)


# import pack_2


# print(dir())
# print(dir(pack_2))



# print('Это основной файл main.py, его имя в процессе выполнения программы:', __name__)


# import pack_1


# print(dir())
# print(dir(pack_1))


# from pack_1.file_11 import func_1
# from pack_1.file_12 import a


# print(func_1(a))


from .pack_1.file_11 import func_1


print(func_1(3))