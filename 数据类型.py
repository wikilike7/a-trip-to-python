# sequence, get the elements with index

# number
num = 1

# string
string = 'abc'

# list
city = ['people', 'car', 'railway']
first = city[0]
city[0:2] # 分片是包含起始元素，而不包含结束元素
city[:]
city[0:]
city[:3]
city[-1]
city[:-1]
print(city[0:-1])

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(numbers[::2])  # 步长是2
print(numbers[4:2:-1])  # 步长是-1

# tuple
company = ('staff', 'computer')

# dict
dictionary = {'name': 'zibba', 'age': 20}

# set, 可以使用{}, 也可以使用set函数
setup = {'a', 'b', 'c', 'd'}
setup1 = set('helloworld')
setup2 = set(['.mp4', '.mkv', '.rmvb'])


