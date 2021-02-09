# # this is a comment
# print('Hello World!')
# print('Hi')
# print(complex(3))
# print(float(3))
# print(3+10j)
# print(int(3.6))  # 3 = partea intreaga
# # print(float(3+5j))  # error can't convert
# # print(int(3+5j))  # error can't convert
# print(type(3))  # class int
# print(type(3).__name__)  # int
# print(type(type(3)))  # class type
# print(type(type(3)).__name__)  # type
# print(type(type(type(3))))  # class type
# print(type(type(type(3))).__name__)  # type
# print(type(type(type(3)).__name__))  # class str - because the word type is a string?
# print(type(type(type(3).__name__)))  # class type #??
# print(type(type(type(3).__name__).__name__))  # class str
# print(type(type(type(3).__name__).__name__).__name__)  # str
# print(type(type(type(3)).__name__).__name__)  # str
# print(type(3.6))  # class float
# print(type(3.6).__name__)  # float
# print(type(3+5j))  # class complex
# if type(3) == int:  # int no class
#     print('int no class')
# else:
#     print('bam')
# if type(3).__name__ == int:  # bam!
#     print('int no class')
# else:
#     print('bam!')

# if type(3).__name__ == 'int':  # int no class
#     print('int no class')
# else:
#     print('bam!')

# print(5 / 2)  # 2.5
# print(5 // 2)  # 2 partea intreaga
# print(5 % 2)  # 1 restul impartirii 5 - 2 x 2 = 1
# print(7 % 4)  # 3 => 7 - 4 x 1 = 3
# print(2 % 5)  # 2 => 2 - 5 x 0 = 2
# print(6 % 3)  # 0 => 6 - 3 x 3 = 0

# print(21 % 2)

# print('print: ', input('give me a number:'))
# print(int(input('give me a number: ')) % 2)

# print(2 == 2, type(2 == 2))
# print(2 == 3, type(2 == 3))
# print(2 <= 3, type(2 <= 3))
# print(2 + 3 == 5)
# print(2 == 2 != 3)  # print(True != 3) => true

# print(not(4 < 5 and 4 > 2))
# print(not(4 < 5 and 4 < 2))
# print(2 == 2 and 3 == 3)  # true
# print(2 != 2 and 3 == 3)  # false
# print(2 == 2 or 3 == 3)  # true
# print(2 != 2 or 3 == 3)  # true
# print(not 2 != 2 or 3 == 3)  # true
# print(not(2 != 2 or 3 == 3))  # false

# print(7 is 7)
# print(7 == 7)

# days_before_christmas_2021 = None
# days_before_christmas_2021 = 111
# print(days_before_christmas_2021)
# days_in_year = 365
# print(days_in_year)
# print(id(days_in_year))
# x = 5
# print(x)
# x += 2  # x = x + 2
# print(x)
# x *= 3
# print(x)
# x = 'a'
# print(x)
# x += 'e'
# print(x)
# # x = 2    # err
# # print(x)
# # x += 'e'
# # print(x)

# my_string = 'This is my first string.'
# print(my_string, type(my_string), type(my_string).__name__)
# my_char = 'b'
# print(my_char, type(my_char), type(my_char).__name__)
# empty_string = ' '
# print('_', empty_string, '_')

# my_char = 'b'
# my_char_int = ord(my_char)
# print(my_char)
# print(my_char_int)
# print('a' + 'b')
# print(ord('a') + ord('b'))
# my_sentence = 'Ana' + ' ' + 'are' + ' ' + 'mere.'
# print(my_sentence)
# x = 'Parola este: "Ana are mere!"'  # ok
# print(x)
# x = "Parola este: 'Ana are mere!'"  # ok
# print(x)
# x = 'Parola este: 'Ana are mere!''  # err
# print(x)
# x = 'Parola este: \'Ana are mere!\'. Done'  # escape
# print(x)
# x = 'Parola este: \n"Ana are mere!"'  # new line
# print(x)
# x = 'Parola este: \n"Ana are mere!"a\b'  # backspace
# print(x)
# x = 'Parola este: \n\t"Ana are mere!"'  # tab
# print(x)
# x = '''Parola este:
#     "Ana are mere!"'''
# print(x)
# x = """Parola este:
#     \"Ana are mere!\""""
# print(x)
# x = r'Parola este: \n\t"Ana are mere!"'  # row string
# print(x)
# x = 'Parola este: \\n\\t"Ana are mere!"'  # escape
# print(x)
# keyboard_msg = input("Give me an input: ")
# print(keyboard_msg, type(keyboard_msg))

# keyboard_msg = input('Give me an input: ')
# x = 'Parola este:\n\t''%s' % keyboard_msg
# print(x)
# keyboard_msg = input('Give me an input: ')
# x = 'Parola este:\n\t"%s"' % keyboard_msg
# print(x)
# keyboard_msg = input('Give me an input: ')
# x = 'Parola este:\n\t"{}"'.format(keyboard_msg)  # format
# print(x)
keyboard_msg = input('Give me an input: ')
x = f'Parola este:\n\t"{keyboard_msg}" la la la'
print(x)
# keyboard_msg = input('Give me an input: ')
# my_number = int(input('Give me an input: '))
# x = f'Parola este:\n\t"{keyboard_msg}"\n...{my_number} times.'
# print(x)
# keyboard_msg = input('Give me an input: ')
# my_number = int(input('Give me an input: '))
# x = 'Parola este:\n\t"%s"\n %s times' % (keyboard_msg, my_number)
# print(x)
# keyboard_msg = input('Give me an input: ')
# my_number = int(input('Give me an input: '))
# x = 'Parola este:\n\t"{}"... \n{:.2f} times'.format(keyboard_msg, my_number)
# print(x)
# keyboard_msg = input('Give me an input: ')
# my_number = int(input('Give me an input: '))
# x = 'Parola este:\n\t"{0}"... \n{1:.2f} times'.format(keyboard_msg, my_number)
# print(x)
# keyboard_msg = input('Give me an input: ')
# my_number = int(input('Give me an input: '))
# x = 'Parola este:\n\t"{1}"... \n{0:.2f} times'.format(keyboard_msg, my_number)  # err expect float
# print(x)
# keyboard_msg = input('Give me an input: ')
# my_number = int(input('Give me an input: '))
# x = 'Parola este:\n\t"{1}"... \n{0} times'.format(keyboard_msg, my_number)
# print(x)
# keyboard_msg = input('Give me an input: ')
# my_number = int(input('Give me an input: '))
# x = 'Parola este:\n\t"{message}"... \n{times} times'.format(message=keyboard_msg, times=my_number)
# print(x)
keyboard_msg = input('Give me an input: ')
my_number = int(input('Give me an input: '))
x = 'Parola {1} este {0}:\n\t{message}... \n{times} times'.format(
    'afisata',
    'actuala',
    message=keyboard_msg,
    times=my_number)
print(x)
