type('string')
type(123)
# int('Hello')  # 这个是转换不了的，'Hello'是字符串，无法转换为整数
int(123.12)  # 转换为123
float(12)  # 转换为12.0
str(123)  # 转换为字符串123


def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")


def repeat_lyrics():
    print_lyrics()
    print_lyrics()


repeat_lyrics()


def print_twice(bruce):
    print(bruce)
    print(bruce)


print_twice('zibba ' * 4)


def cat_twice(part1, part2):
    cat = part1 + part2
    print_twice(cat)  # call another function


cat_twice(1, 2)
cat_twice('Hello ', 'World')


# Exercise 1
def right_justfy(s):
    print(' ' * (70 - len(s)), end=s)


right_justfy('zibba')  # test pass


print('\n')  # print a blank line


# # Exercise 2
# def print_twice(arg):
#     print(arg)
#     print(arg)
#
#
# def do_twice(func, arg):
#     func(arg)
#     func(arg)
#
#
# def do_four(func, arg):
#     do_twice(func, arg)
#     do_twice(func, arg)
#
#
# do_twice(print_twice, 'spam')
# print('')
# do_four(do_twice, 'spam')


# Exercise 3
print('+', '-' * 4, '+', '-' * 4, '+')
print('|', ' ' * 4, '|', ' ' * 4, '|')
print('|', ' ' * 4, '|', ' ' * 4, '|')
print('|', ' ' * 4, '|', ' ' * 4, '|')
print('|', ' ' * 4, '|', ' ' * 4, '|')


def print_table(num):
    print('+', '-' * num, '+', '-' * num, '+')
    print('|', ' ' * num, '|', ' ' * num, '|')
    print('+', '-' * num, '+', '-' * num, '+')
    print('|', ' ' * num, '|', ' ' * num, '|')
    print('+', '-' * num, '+', '-' * num, '+')


print_table('h')
