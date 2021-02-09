# my_list = ['ana', 1, 3+2j, [1, 2, 'a']]
# print(type(my_list))
# print(type(my_list).__name__)
# print(my_list)
# print(len(my_list))  # returns number of elements - real number! does not count from 0 ;)
# print(my_list[0])
# print(my_list[1])
# print(my_list[2])
# print(my_list[3])

# my_strings = ['ana', 'are', 'mere']
# #               0      1      2
# #              -3     -2     -1
# # print(type(my_strings))
# # print(type(my_strings).__name__)
# # print(my_strings)
# # print(len(my_strings))
# # print(my_strings[0])
# # print(my_strings[1])
# # print(my_strings[2])
# print(my_strings[len(my_strings) - 1])
# # print(my_strings[len(my_strings) - 2])
# # print(my_strings[len(my_strings) - 3])
# print(my_strings[len(my_strings) - 4])
# print(my_strings[len(my_strings) - 5])
# print(my_strings[len(my_strings) - 6])
# # # print(my_strings[len(my_strings) - 7])  # error

# list_inside = [1, ['a', 'b', 'c', ['a', 'p', 'a']], 3]
# # print(list_inside[1][-1][-2])
# # list_inside = [1, ['a', 'b', 'c']]
# list_inside_list = list_inside[1]
# print(list_inside_list)  # ['a', 'b', 'c', ['a', 'p', 'a']]
# print(list_inside_list[-1])  # ['a', 'p', 'a']
# print(list_inside_list[-1][1])  # p
# print(list_inside_list[-2])  # c
# print(list_inside_list[-1][0])  # a

# my_string = 'ana'
# print(len(my_string))
# print(my_string[0])

# my_fruits = ['banane', 'mere', 'gutui', 'pere']
# print(my_fruits)
#
# new_list = my_fruits[::]  # start_index : end_index : step
# # new_list = my_fruits[2::]  # ['gutui', 'pere']
# # new_list = my_fruits[3::]  # ['pere']
# new_list = my_fruits[1:3:]  # ['gutui', 'pere']  start_index (+) este inclusiv : end_index (-) exclusiv
# print(new_list)

# my_fruits = ['banane', 'mere', 'gutui', 'pere', 'capsuni', 'pomelo', 'lubenita']
#               0         1      2        3         4           5         6
#              -7        -6     -5       -4        -3          -2         -1

# new_list = my_fruits[1:3:]  # ['mere', 'gutui']
# new_list = my_fruits[2:5:]  # ['gutui', 'pere', 'capsuni']
# new_list = my_fruits[1:len(my_fruits) - 1:]  # ['mere', 'gutui', 'pere', 'capsuni', 'pomelo']
# new_list = my_fruits[1:-1:]  # ['mere', 'gutui', 'pere', 'capsuni', 'pomelo']
# new_list = my_fruits[1:-1:2]  # ['mere', 'pere', 'pomelo']
# new_list = my_fruits[1:-1:3]  # ['mere', 'capsuni']
# new_list = my_fruits[-3::]  # ['capsuni', 'pomelo', 'lubenita']
# new_list = my_fruits[:3:]  # ['banane', 'mere', 'gutui']
# new_list = my_fruits[::2]  # ['banane', 'gutui', 'capsuni', 'lubenita']
# new_list = my_fruits[:-5:]  # ['banane', 'mere']
# new_list = my_fruits[::-2]  # ['lubenita', 'capsuni', 'gutui', 'banane']
# new_list = my_fruits[::-1]  # ['lubenita', 'pomelo', 'capsuni', 'pere', 'gutui', 'mere', 'banane']

# my_list_from_string = list('ana are mere')  # ['a', 'n', 'a', ' ', 'a', 'r', 'e', ' ', 'm', 'e', 'r', 'e']
# print(my_list_from_string)

# a = 256
# b = 256
#
# print('1: ', a is b)  # true
# print('2: ', id(a) == id(b))  # true
# print(id(a))
# print(id(b))
#
# print('3: ', id('a') == id('b'))  # false
#
# c = 257
# d = 257
#
# print('4 ', c is d)  # true
# print('5 ', id(c) == id(d))  # true

# a = [1, 2, 3]
# b = [1, 2, 3]
# print(a is b)  # false
# print(a == b)  # true

# a = [1, 2, 3]
# a_length_condition = len(a) == 3  # true
# print(a_length_condition is True)
# print(a_length_condition is not True)
# # print(not(a_length_condition is True))

# a = [1, 2, 3]
# # a.pop()
# # a.pop(1)  # [1, 3]
# b = a.count(1)
# print(b)

# a = [1, 2, 3]
# b = [4, 5, 6]
# # c = a + b
# a.extend(b)
# print(a)

a = [1, 2, 3]
b = a
print(a is b)
b.append(4)
print(a)
print(b)





