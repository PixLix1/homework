def sum_numbers(*args, **kwargs):
    sum_final = 0
    for num in args:
        if type(num) == int or type(num) == float:
            sum_final += num
    return sum_final


print('add numbers 1st check: ', sum_numbers(1, 5, -3, 'abc', [12, 56, 'cad']))
# print('add numbers 2nd check: ', sum_numbers())
# print('add numbers 3rd check: ', sum_numbers(2, 4, 'abc', param_1=2))
#
#
# def read_int():
#     num = input('enter a number: ')
#     try:
#         int(num)
#         # if type(num) == int:
#         return num
#     except ValueError:
#         return 0
#
#
# print(read_int())


# def sum_with_for_loop(num):
#     sum_even = 0
#     sum_odd = 0
#     sum_ttl = 0
#     for i in range(num + 1):
#         sum_ttl += i
#         if i % 2 == 0:
#             sum_even += i
#         else:
#             sum_odd += i
#     return 'sum ttl:', sum_ttl, 'sum_odd:', sum_odd, 'sum_even: ', sum_even
#
#
# print(sum_with_for_loop(4))


# def sum_recursive(num):
#     if num == 0:
#         return 0, 0
#     sum_ttl = sum_recursive(num - 1)
#     if num % 2 == 0:
#         sum_even += num
#     return sum_ttl, sum_even
#
#
# # expected for 4: 10, 4, 6
# print(sum_recursive(4))
