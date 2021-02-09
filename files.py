import csv
import json
# my_text = ''

# with open('my_input.txt', 'r') as my_file:
#     lines = my_file.readlines()
#     print('lines:', type(lines), lines)  # lines is class list! reads all lines

# with open('my_input.txt', 'r') as my_file:
#     line = my_file.readline()
#     print('line:', type(line), line)  # line is class str! reads first line only

# -------------------------------------------------------------------------------------- read all line (str) with while
# with open('my_input.txt', 'r') as my_file:
#     while True:
#         line = my_file.readline()
#         print('line:', type(line), line)
#         my_text += line
#         if not line:
#             break
#         # print('line:', type(line), line)
#
# print('From file:', my_text)

# ------------------------------------------------------------------------------------ create file and write into it
# Open in write mode
# with open('my_output.txt', 'w') as my_file:
#     my_file.write(my_text)

# ---------------------------------------------------------------------------------------------------- append to file
# Open in append mode
# with open('my_output.txt', 'a') as my_file:
#     my_file.write('\n\n\n')
#     my_file.write(my_text)

# ---------------------------------------------------------------------------------------- read line by line from .csv
# with open('my_input.csv') as csv_file:
#     header = ()
#     student_data = []
#     for index, line in enumerate(csv_file.readlines()):
#         if index == 0:
#             header = line.split(',')
#             print('header', header)
#         else:
#             student_data = line.split(',')
#             print('student_data', student_data)

# --------------------------------------------------------------------------------------------------------- import csv
my_students = []
header = ()
student_data = []

with open('my_input.csv') as csv_file:
    my_data = csv.reader(csv_file)
    # print(type(my_data), my_data)

    for index, data in enumerate(my_data):
        if index == 0:
            header = data
        else:
            student_data.append(data)

# print('header', header)
# print('student_data', student_data)
my_students = [{key: value for key, value in zip(header, element)} for element in student_data]
print(my_students)

with open('my_output.json', 'w') as json_file:
    json_object = json.dumps(my_students)
    # print(type(json_object), json_object)
    json_file.write(json_object)


