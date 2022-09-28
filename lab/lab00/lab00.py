def twenty_twenty_two():
    """Come up with the most creative expression that evaluates to 2022,
    using only numbers and the +, *, and - operators.

    >>> twenty_twenty_two()
    2022
    """
    return ((20 ** 2 + 22 ** 2) + ((2 ** 0 + 2 ** 2) * 20 * 22) + (20 + 2 * 2) * 20 * 2) // 2

def identity(k):
    return k

def cube(k):
    return pow(k, 3)

def summer(N, term):
    '''
    Compute sum of Nth item

    >>> summer(5, cube)
    225
    '''
    k = 1
    total = 0
    while k < N+1:
        total += term(k)
        k += 1
    return total

def make_adder(n):
    '''
    Return a function takes a number k and return k + n.

    >>> add_three = make_adder(3)
    >>> add_three(4)
    7
    '''
    def adder(k):
        return k + n
    return adder