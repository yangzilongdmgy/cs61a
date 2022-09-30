# def even(f):
#     def odd(x):
#         if x < 0:
#             return f(-x)
#         return f(x)
#     return odd

# def cake():
#     print('beets')
#     def pie():
#         print('sweets')
#         return 'cake'
#     return pie

# def snake(x, y):
#     if cake == more_cake:
#         return chocolate
#     else:
#         return x + y

# n = 7

# def f(x):
#     n = 8
#     return x + 1

# def g(x):
#     n = 9
#     def h():
#         return x + 1
#     return h

# def f(f, x):
#     return f(x + n)

# f = f(g, n)
# g = (lambda y: y())(f)

# def composer(f, g):
#     return lambda x: f(g(x)) == g(f(x))

def cycle(f1, f2, f3):
    def func(n):
        def final(x):
            res = x
            lst = [f1, f2, f3]
            i = 0
            while(i < n):
                    index = i % 3
                    res = lst[index](res)
                    i += 1
            return res
        return final
    return func

def add1(x):
    return x + 1

def times2(x):
    return x * 2

def add3(x):
    return x + 3
