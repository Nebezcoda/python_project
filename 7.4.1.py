'''
Функция custom_filter()

Реализуйте функцию custom_filter(), которая на вход принимает список some_list, с любыми типами данных, находит в этом списке целые числа, отбирает из них те, что делятся нацело на 7, суммирует их, а затем проверяет превышает эта сумма 83 или нет. Если НЕ превышает - функция должна вернуть True, если превышает - False.

Примечание. В тестирующую систему сдайте программу, содержащую только необходимую функцию custom_filter(), но не код, вызывающий ее.


Sample Input 1:
some_list = [7, 14, 28, 32, 32, 56]
print(custom_filter(some_list))
Sample Output 1:
False

Sample Input 2:
some_list = [7, 14, 28, 32, 32, '56']
print(custom_filter(some_list))
Sample Output 2:
True

'''
def custom_filter(slist):
    new_list = list(filter(lambda x: type(x) is int and (x%7 == 0), slist))
    return False if sum(i for i in new_list) > 83 else True

# some_list = [7, 14, 28, 32, 32, 56]
some_list = [7, -14, 28, 32, -32, '56', True, 'dsds']
print(custom_filter(some_list))