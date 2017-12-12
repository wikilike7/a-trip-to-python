def func(g, arr):
    return [g(x) for x in arr]


arr = func(lambda x: x + 1, [1, 2, 3, 4])



