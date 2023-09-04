class MyClass:
    def __init__(self) -> None:
        pass

my_class_1 = MyClass()
my_class_2 = MyClass()

print(my_class_1)
print(my_class_2)

# <__main__.MyClass object at 0x0000023666C70450>
# <__main__.MyClass object at 0x0000023666C70490>


class MyClass2:
    def __init__(self) -> None:
        pass

    def __call__(self) -> str:
        return 'Результат вызова экземпляра класса'


my_class_1 = MyClass2()
my_class_2 = MyClass2()

print(my_class_1())
print(my_class_2())

# Результат вызова экземпляра класса
# Результат вызова экземпляра класса