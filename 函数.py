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


print_twice('zibba')
