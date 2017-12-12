from functools import reduce
print(reduce(lambda x, y: x * y, [1, 2, 3, 4]))  # 递归计算
f = lambda a, b: a if (a > b) else b
print(reduce(f, [1, 5, 2, 10]))


even_num = list(filter(lambda x: x % 2 == 1, [1, 2, 3, 4, 5, 6]))
print(even_num)
