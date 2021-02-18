import csv
import json
import os
import glob

# output_dir_path = '../output_data'
output_dir_path = './output_data'
try:
    os.mkdir(output_dir_path)
except FileExistsError as err:
    if len(os.listdir(output_dir_path)) != 0:
        files = glob.glob(output_dir_path + '/*')
        for f in files:
            os.remove(f)


def create_json_file(directory, action_type, *list_name):
    """
    Generates json files based on multiple tuples as arguments
    :param directory: location of the output files
    :param action_type: write, append
    :param list_name: tuple format: first element should be the output file's name,
        second element should be the list which is to be printed in the newly generated file
    :return: not applicable
    """
    for x in list(list_name):
        file_name = x[0] + '.json'
        with open(directory + '/' + file_name, action_type) as json_file:
            json_file.write(json.dumps(x[1]))


header = []
car_data = []
with open('input.csv') as csv_file:
    my_data = csv.reader(csv_file)  # read csv

    for index, data in enumerate(my_data):
        if index == 0:
            header = data
            header.insert(index, 'id')
            header = [x.strip(' ') for x in header]
        else:
            data = [x.strip(' ') for x in data]
            for x, y in enumerate(data):
                if data[x] == '' or data[x] == ' ':
                    data.pop(x)
                    data.insert(x, 0)
            data[-2:] = [int(x) for x in data[-2:]]
            data.insert(0, index)
            car_data.append(data)

car_data = [{key: value for key, value in zip(header, element)} for element in car_data]

slow_cars = [x for x in car_data if x['hp'] in range(0, 120)]
fast_cars = [x for x in car_data if x['hp'] in range(120, 180)]
sport_cars = [x for x in car_data if x['hp'] not in range(0, 180)]
cheap_cars = [x for x in car_data if x['price'] in range(0, 1000)]
medium_cars = [x for x in car_data if x['price'] in range(1000, 5000)]
expensive_cars = [x for x in car_data if x['price'] not in range(0, 5000)]

create_json_file(output_dir_path, 'w',
                 ('slow_cars', slow_cars), ('fast_cars', fast_cars), ('sport_cars', sport_cars),
                 ('cheap_cars', cheap_cars), ('medium_cars', medium_cars), ('expensive_cars', expensive_cars))

brands = [car_data[x]['brand'] for x, y in enumerate(car_data)]
brands = set(brands)
for item in brands:
    temp_list = [car_data[x] for x, y in enumerate(car_data) if item in car_data[x]['brand']]
    create_json_file(output_dir_path, 'a', (item, temp_list))

# # --------------------------------------------------------------------------------------------------------- old stuff

# DOES NOT CREATE LIST OF DICTS, INSTEAD DICTS ARE PLACED SIDE BY SIDE, WITHOUT COMMA
# FILE NOT RECOGNIZABLE AS JSON FORMAT
# IF CRITERIA NOT MET, FILE IS NOT GENERATED :(
# slow_cars = [create_json_file(output_dir_path, 'slow_cars.json', 'a', x) for x in car_data if x['hp'] in range(0, 120)]
# fast_cars = [create_json_file(output_dir_path, 'fast_cars.json', 'a', x) for x in car_data if x['hp'] in range(120, 180)]
# sport_cars = [create_json_file(output_dir_path, 'sport_cars.json', 'a', x) for x in car_data if x['hp'] not in range(0, 179)]
# cheap_cars = [create_json_file(output_dir_path, 'cheap_cars.json', 'a', x) for x in car_data if x['price'] in range(0, 1000)]
# medium_cars = [create_json_file(output_dir_path, 'medium_cars.json', 'a', x) for x in car_data
#                if x['price'] in range(999, 5000)]
# expensive_cars = [create_json_file(output_dir_path, 'expensive_cars.json', 'a', x) for x in car_data
#                   if x['price'] not in range(0, 4999)]


# # with open(dir_path + '/' + 'temp_file.json') as f:
# #     test_data_exists = json.load(f)
#
#
# # print(test_data_exists)
#
#
# # # def calc_speed_price_range(car):
# # #     """
# # #     classify cars based on keys 'hp' and 'price'
# # #     :param: car element from dict
# # #     :return: dict elem with two new keys: 'speed_range' and 'price_range'
# # #     """
# # #     car = car.copy()
# # #     try:
# # #         if int(car['hp']) < 120:
# # #             car['speed_range'] = 'slow_cars'
# # #         elif 120 <= int(car['hp']) < 180:
# # #             car['speed_range'] = 'fast_cars'
# # #         else:
# # #             car['speed_range'] = 'sport_cars'
# # #     except ValueError as e:
# # #         car['speed_range'] = 'unclassified'
# # #     try:
# # #         if int(car['price']) < 1000:
# # #             car['price_range'] = 'cheap'
# # #         elif 1000 <= int(car['price']) < 5000:
# # #             car['price_range'] = 'medium'
# # #         else:
# # #             car['price_range'] = 'expensive'
# # #     except ValueError as e:
# # #         car['price_range'] = 'unclassified'
# # #     return car
# #
# # print(type(car_data))
# # # car_data = list(map(calc_speed_price_range, car_data))
# # print(car_data)
# # print(list(car_data))
#
# # # def filter_by_speed(car, criteria):
# # #     return True if car['speed_range'] == criteria else False
# # # def filter_by_speed(car):
# # #     if car['speed_range'] == 'slow_cars':
# # #         return True
# # #     elif car['speed_range'] == 'fast_cars':
# # #         return True
# # #     elif car['speed_range'] == 'sport_cars':
# # #         return True
# # #     return False
#
#
# # slow_cars = [x for x in car_data if x['hp'] in range(120)]
# # fast_cars = [x for x in car_data if x['hp'] in range(119, 180)]
# # sport_cars = [x for x in car_data if x['hp'] not in range(0, 179)]
# # cheap_cars = [x for x in car_data if x['price'] in range(1000)]
# # medium_cars = [x for x in car_data if x['price'] in range(999, 5000)]
# # expensive_cars = [x for x in car_data if x['price'] not in range(0, 4999)]
#
# # # create_json_file(dir_path, 'w', cheap_cars, fast_cars, sport_cars, cheap_cars, medium_cars, expensive_cars)
# # create_json_file(dir_path, 'slow_cars.json', 'w', slow_cars)
# # create_json_file(dir_path, 'fast_cars.json', 'w', fast_cars)
# # create_json_file(dir_path, 'sport_cars.json', 'w', sport_cars)
# # create_json_file(dir_path, 'cheap_cars.json', 'w', cheap_cars)
# # create_json_file(dir_path, 'medium_cars.json', 'w', medium_cars)
# # create_json_file(dir_path, 'expensive_cars.json', 'w', expensive_cars)
#
#
# # slow_cars = [x for x in car_data if x['speed_range'] == 'slow_cars']
# # slow_cars = [x for x in car_data if x.get('hp', 0) < 120]
# # slow_cars = [x for x in car_data if int(x.get('hp', 0)) < 120]
# # fast_cars = [x for x in car_data if x['speed_range'] == 'fast_cars']
# # sport_cars = [x for x in car_data if x['speed_range'] == 'sport_cars']
#
# # # create_json_file(dir_path + '/' + 'output_file.json', 'w')  ## nu sterge, merge asa
#
# # # filtered_dict = {k: v for (k, v) in car_data if 'slow_cars' in k}
# # # test_filter = list(filter(filter_by_speed, car_data))
# # # print(filtered_dict)
#
# # def create_json_file(new_file, action_type):
# #     with open(new_file, action_type) as json_file:
# #         json_file.write(json.dumps(car_data))
#
#
# # def create_json_file(directory, action_type, *list_name):
# #     while list_name:
# #         file_name = list_name
# #         with open(directory + '/' + file_name + '.json', action_type) as json_file:
# #             json_file.write(json.dumps(list_name))
#
#
# # def create_json_file(directory, action_type, list_name):
# #     while list_name:
# #         file_name = list_name
# #         with open(directory + '/' + file_name + '.json', action_type) as json_file:
# #             json_file.write(json.dumps(list_name))
#
# # temp_list = [car_data[x] for x, y in enumerate(car_data) for z in enumerate(brands) if z in car_data[x]['brand']]
#
# # for x, y in enumerate(car_data):
# #     for z in brands:
# #         if z in car_data[x]['brand']:
# #             print(car_data[x])
#
#
# # test_l = ['a', '1', ' ']
# # for x, y in enumerate(test_l):
# #     if test_l[x] == ' ':
# #         test_l.pop(x)
# #         test_l.insert(x, 0)
# #     else:
# #         temp_elem = test_l.pop(x)
# #         test_l.insert(x, int(temp_elem))
# #         # int(test_l[x])
# #
# # print('list: ', test_l)

# print(list(range(0, 120)))
# print(range(120, 180))
# print(range(0, 180))
# print(range(0, 1000))
# print(range(999, 5000))
# print(range(0, 4999))
# if 1000 in list(range(1000, 5000)):
#     print('True')
