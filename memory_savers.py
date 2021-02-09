# a = lambda x, y: x + y  # warning do not assign lambda
# print(a(5, 7))

# def a(x, y):
#     return x + y

# print(lambda: 1)  # nothing happens
# print((lambda: 1)())  # function called, print 1
# print((lambda: 1)(5))  # error additional parameter

# print(id(lambda: 1))  # same
# print(id(lambda: 2))  # same
# print(id(lambda: 'a'))  # same
# # print(id(1))  # different
# # print(id(2))  # different

# my_list = [1, 6, -3, 5]
# print(my_list.sort())
# sorted_list = sorted(my_list)
# sorted_list = sorted(my_list, reverse=True)
# print(sorted_list)
# ---------------------------------------------------------------------- additional function, higher memory consumption
# def sort_my_students(my_student):
#     # print(my_student)
#     return my_student["grade"]


# my_students = [{
#     "first_name": "1",
#     "last_name": "1",
#     "grade": 7
# }, {
#     "first_name": "2",
#     "last_name": "2",
#     "grade": 6.55
# }, {
#     "first_name": "3",
#     "last_name": "3",
#     "grade": 8
# }, {
#     "first_name": "4",
#     "last_name": "4",
#     "grade": 10,
# }, {
#     "first_name": "5",
#     "last_name": "5",
#     "grade": 3.25
# }, {
#     "first_name": "6",
#     "last_name": "6",
#     "grade": 1.25
# }]


# # my_students.sort(key=sort_my_students)
# my_students.sort(key=sort_my_students, reverse=True)
# my_sorted_students = sorted(my_students, key=sort_my_students, reverse=True)
# print(my_students)

# def sort_my_cars(my_car):
#     return my_car["hp"]
#
#
# my_cars = [{
#     "hp": 10
# }, {
#     "hp": 15
# }, {
#     "hp": 8
# }]
#
# my_sorted_cars = sorted(my_cars, key=sort_my_cars, reverse=True)
# print(my_sorted_cars)

# -------------------------------------------------------------------------------------------------------- lambda
# my_students = [{
#     "first_name": "1",
#     "last_name": "1",
#     "grade": 7
# }, {
#     "first_name": "2",
#     "last_name": "2",
#     "grade": 6.55
# }, {
#     "first_name": "3",
#     "last_name": "3",
#     "grade": 8
# }, {
#     "first_name": "4",
#     "last_name": "4",
#     "grade": 10,
# }, {
#     "first_name": "5",
#     "last_name": "5",
#     "grade": 3.25
# }, {
#     "first_name": "6",
#     "last_name": "6",
#     "grade": 1.25
# }]
#
# my_sorted_students = sorted(my_students, key=lambda my_student: my_student['grade'], reverse=True)
# print(my_sorted_students)
#
#
# my_cars = [{
#     "hp": 10
# }, {
#     "hp": 15
# }, {
#     "hp": 8
# }, {
# }]
#
# # my_sorted_cars = sorted(my_cars, key=lambda my_car: my_car['hp'], reverse=True)  # error when dict without key 'hp'
# my_sorted_cars = sorted(my_cars, key=lambda my_car: my_car.get('hp', 0), reverse=True)  # corrected: get, else o
# print(my_sorted_cars)

# ------------------------------------------------------------------------------------------------------ inline if
# my_cars = [{
#     "real_hp": 10,
#     "original_hp": 15,
# }, {
#     "real_hp": 20,
#     "original_hp": 20,
# }, {
#     "original_hp": 40
# }]
# my_sorted_cars = sorted(my_cars, key=lambda a: a['real_hp'] if 'real_hp' in a else a['original_hp'], reverse=True)
# print(my_sorted_cars)


# ---------------------------------------------------------------- map function - modifies each element in an iterable
# def update_student(student):
#     student = student.copy()
#     # print('student', student)  # check
#     student['full_name'] = '%s %s' % (student['first_name'], student['last_name'])
#     # if student['grade'] >= 7:
#     #     student['promoted'] = True
#     # else:
#     #     student['promoted'] = False
#     # student['promoted'] = True if student['grade'] >= 7 else False   # short version => inline if
#     student['promoted'] = student['grade'] >= 7                        # even shorter  =>  = true or false :)
#     return student
#
#
# my_students = [{
#     "first_name": "1",
#     "last_name": "1",
#     "grade": 7
# }, {
#     "first_name": "2",
#     "last_name": "2",
#     "grade": 6.55
# }, {
#     "first_name": "3",
#     "last_name": "3",
#     "grade": 8
# }, {
#     "first_name": "4",
#     "last_name": "4",
#     "grade": 10,
# }, {
#     "first_name": "5",
#     "last_name": "5",
#     "grade": 3.25
# }, {
#     "first_name": "6",
#     "last_name": "6",
#     "grade": 1.25
# }]
#
# my_students = list(map(update_student, my_students))
# print(my_students)

# ------------------------------------------------------------------ version with for (additional variable, more lines)
# my_aux_students = []
# for student in my_students:
#     my_aux_students.append(update_student(student))
# my_students = my_aux_students
# print(my_students)

# ----------------------------------------------------------------------------------------------- e.g. map with tuple
# initial_list = (1, 2, 3, 4, 5)
# other_numbers = map(lambda x: x**2, initial_list)
# other_numbers = tuple(other_numbers)
# print(initial_list, type(initial_list))
# print(other_numbers, type(other_numbers))

# ------------------------------------------------------------------ map ex. start from tuple and return tuple of dicts
# initial_list = (1, 2, 3, 4, 5)
# other_numbers = map(lambda x: {'initial_number': x, 'squared_number': x ** 2}, initial_list)
# other_numbers = tuple(other_numbers)
# print(initial_list, type(initial_list))
# print(other_numbers, type(other_numbers))

# -------------------------------------------- map ex. start from tuple and return tuple of dicts or list (conditional)
# initial_list = (1, 2, 3, 4, 5)
# other_numbers = map(lambda x: {'initial_number': x, 'squared_number': x ** 2} if x % 2 == 0 else [1, 2], initial_list)
# other_numbers = tuple(other_numbers)
# print(initial_list, type(initial_list))
# print(other_numbers, type(other_numbers))

# -------------------------------------------------------------------------------------------- filter function on dicts
# def filter_by_promoted(student):
#     # if student['grade'] >= 7:
#     #     return True
#     #
#     # return False
#     return True if student['grade'] >= 7 else False
#
#
# my_students = [{
#     "first_name": "1",
#     "last_name": "1",
#     # "grade": 7
# }, {
#     "first_name": "2",
#     "last_name": "2",
#     "grade": 6.55
# }, {
#     "first_name": "3",
#     "last_name": "3",
#     "grade": 8
# }, {
#     "first_name": "4",
#     "last_name": "4",
#     "grade": 10,
# }, {
#     "first_name": "5",
#     "last_name": "5",
#     "grade": 3.25
# }, {
#     "first_name": "6",
#     "last_name": "6",
#     "grade": 1.25
# }]
# # my_promoted_students = filter(filter_by_promoted, my_students)  # with separated function
# my_promoted_students = filter(lambda x: x.get('grade', 2) >= 7, my_students)  # lambda
# my_promoted_students = list(my_promoted_students)
# # print(type(my_promoted_students))
# print(my_promoted_students)

# ---------------------------------------------------------------------------------------- filter function with tuple
# initial_numbers = tuple(range(1, 10))
# even_numbers = tuple(filter(lambda x: x % 2 == 0, initial_numbers))
# odd_numbers = tuple(filter(lambda x: x % 2 == 1, initial_numbers))
# print(even_numbers)
# print(odd_numbers)

# ------------------------------------------------------------------------------------------------------ zip function
# my_tuple = ('a', 'b', 'c')
# my_list = [1, 2, 3]
# mx = [{}, True, False]
# my_result = zip(my_tuple, my_list, mx)
# my_list_result = list(my_result)
# # print(my_list_result, type(my_list_result))
# print(my_list_result)

# my_tuple = ('a', 'b', 'c', 'd', 'e')
# my_list = [1, 2, 3]
# mx = [{}, True, False]
# my_result = zip(my_tuple, my_list, mx)
# my_list_result = list(my_result)
# # goes until shortest number of elements in iterable =>
# # d, e from tuple not showing up: [('a', 1, {}), ('b', 2, True), ('c', 3, False)]
# print(my_list_result)

# ------------------------------------------------------------------------------------ zip used in for to obtain a dict
# my_tuple = ('a', 'b', 'c', 'd', 'e')
# my_list = [1, 2, 3]
# my_dict = {}
# for a, b in zip(my_tuple, my_list):
#     my_dict[a] = b
# print(my_dict)

# ------------------------------------------------------------------------------------------------- list comprehension
# my_initial_numbers = range(1, 11)
# print(list(my_initial_numbers))
# my_squared_numbers = [x ** 2 for x in my_initial_numbers]
# print('my_squared_numbers', my_squared_numbers)
# my_even_numbers = [x for x in my_initial_numbers if x % 2 == 0]
# print('my_even_numbers', my_even_numbers)
# my_odd_squared_numbers = [x ** 2 for x in my_initial_numbers if x % 2 == 1]
# print('my_odd_squared_numbers', my_odd_squared_numbers)

# my_keys = ('a', 'b', 'c')
# my_values = [1, 2, 3]
# my_dict = {key: value for key, value in zip(my_keys, my_values) if value % 2 == 0}
# print(my_dict)




