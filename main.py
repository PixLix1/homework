initial_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

ascending_list = initial_list.copy()
ascending_list.sort()
print('sort asc: ', ascending_list)
# print('initial list: ', initial_list)
descending_list = list(ascending_list[::-1])
# descending_list.reverse()
print('reverse desc: ', descending_list)
print('odd list: ', ascending_list[::2])
print('multiple of 3 list: ', ascending_list[2::3])