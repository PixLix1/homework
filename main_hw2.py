# def sum_numbers(*args, **kwargs):
#     sum_final = 0
#     for num in args:
#         if type(num) == int or type(num) == float:
#             sum_final += num
#     return sum_final


# print('add numbers 1st check: ', sum_numbers(1, 5, -3, 'abc', [12, 56, 'cad']))
# print('add numbers 2nd check: ', sum_numbers())
# print('add numbers 3rd check: ', sum_numbers(2, 4, 'abc', param_1=2))


# def read_int():
#     try:
#         num = int(input('enter a number: '))
#         if type(num) == int:
#             return num
#     except:
#         return 0


# print(read_int())


def sum_with_for_loop(num):
    even_list = []
    odd_list = []
    for i in range(num + 1):
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
    sum_even = 0
    sum_odd = 0
    sum_ttl = 0
    for i in even_list:
        sum_even = sum_even + i
    for i in odd_list:
        sum_odd = sum_odd + i
    for i in range(num + 1):
        sum_ttl += i
    return sum_ttl, sum_even, sum_odd


print(sum_with_for_loop(2))

# def check_modulo(n):
#     if n % 2 == 0:
#         print('even')
#     else:
#         print('odd')
#
#
# print(check_modulo(2))

# def sum_list_recursive(num_list):
#     if len(num_list) == 1:
#         return num_list[0]
#     else:
#         val = num_list[1:]
#         print('val = ', val)
#         print('num_list[0] = ', num_list[0])
#         return num_list[0] + sum_list_recursive(val)
#
#
# print(sum_list_recursive([5, 2, 3]))


# def sum_recursive(num, test_list=None):
#     print('upper call n = ', num)
#     if test_list is None:
#         test_list = []
#     if num == 0:
#         print('about to return 0')
#         return 0
#     if num % 2 == 0:
#         sum_even = num + sum_recursive(num - 1)
#         # print('even call n = ', num)
#         print('even sum = ', sum_even)
#         return sum_even
#     if num % 2 != 0:
#         sum_odd = num + sum_recursive(num - 1)
#         # print('odd call n = ', num)
#         print('odd sum = ', sum_odd)
#         return sum_odd
#     ttl = num + sum_recursive(num - 1)
#     print('lower call n = ', num, 'res = ', ttl)
#     print('ttl sum = ', ttl)
#     return ttl
#
#
# print(sum_recursive(3))

#
# def sum_recursive(num, test_list=None):
#     print('upper call n = ', num)
#     if test_list is None:
#         test_list = []
#     if num == 0:
#         print('about to return 0')
#         return 0
#     if num % 2 == 0:
#         sum_even = num + sum_recursive(num - 1)
#         # print('even call n = ', num)
#         print('even sum = ', sum_even)
#         return sum_even
#     else:
#         sum_odd = num + sum_recursive(num - 1)
#         # print('odd call n = ', num)
#         print('odd sum = ', sum_odd)
#         return sum_odd
#
#
# print(sum_recursive(3))

# def sum_recursive(num, test_list=None):
#     print('upper call n = ', num)
#     if test_list is None:
#         test_list = []
#     if num == 0:
#         print('about to return 0')
#         return 0
#     else:
#         sum_ttl = num + sum_recursive(num - 1)
#         print('total sum = ', sum_ttl)
#         return sum_ttl


# print(sum_recursive(3))

# def sum_recursive(num, test_list=None):
#     print('upper call n = ', num)
#     if test_list is None:
#         test_list = []
#     even_list = []
#     odd_list = []
#     if num == 0:
#         print('about to return 0')
#         return 0
#     for i in range(num):
#         print('for i = ', i)
#         if num % 2 == 0:
#             sum_even = num + sum_recursive(num - 1)
#             print('even sum = ', sum_even)
#             return sum_even
#         else:
#             sum_odd = num + sum_recursive(num - 1)
#             ttl = num + sum_recursive(num - 1)
#             print('odd sum = ', sum_odd, ttl)
#             return sum_odd


# def sum_recursive(num, test_list=None):
#     print('upper call n = ', num)
#     if test_list is None:
#         test_list = []
#     if num == 0:
#         print('about to return 0')
#         return 0
#     if num % 2 == 0:
#         sum_even = num + sum_recursive(num - 1)
#         print('even call n = ', num)
#         print('even sum = ', sum_even)
#         return sum_even
#     else:
#         sum_odd = num + sum_recursive(num - 1)
#         print('odd call n = ', num)
#         print('odd sum = ', sum_odd)
#         return sum_odd


# print(sum_recursive(3))


# if num % 2 == 0:
#     sum_even = num + sum_recursive(num - 1)
#     print('even call n = ', num)
#     print('even sum = ', sum_even)
#     return sum_even
# else:
#     sum_odd = num + sum_recursive(num - 1)
#     print('odd call n = ', num)
#     print('odd sum = ', sum_odd)
#     return sum_odd
