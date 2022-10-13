# Q3
def make_repeater(func, n):
    def g(x):
        res = x
        for i in range(n):
            res = func(res)
        return res
    return g

def apply_twice(func):
    return make_repeater(func, 2)

def div_by_primes_under(n):
    def checker(k):
        for i in range(2, n+1):
            if k % i != 0:
                return False
        return True
    return checker