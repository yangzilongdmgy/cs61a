def num_eights(pos):
    if pos == 0:
        return 0
    else:
        last = pos % 10
        if last == 8:
            return 1 + num_eights(pos//10)
        else:
            return num_eights(pos//10)

def pingpong(n):
    def helper(result, i, step):
        if i == n:
            return result
        elif i % 8 == 0 or num_eights(i) > 0:
            return helper(result-step, i+1, -step)
        else:
            return helper(result+step, i+1, step)
    return helper(1, 1, 1)

def next_larger_coin(coin):
    """Returns the next larger coin in order.
    >>> next_larger_coin(1)
    5
    >>> next_larger_coin(5)
    10
    >>> next_larger_coin(10)
    25
    >>> next_larger_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25

def next_smaller_coin(coin):
    """Returns the next smaller coin in order.
    >>> next_smaller_coin(25)
    10
    >>> next_smaller_coin(10)
    5
    >>> next_smaller_coin(5)
    1
    >>> next_smaller_coin(2) # Other values return None
    """
    if coin == 25:
        return 10
    elif coin == 10:
        return 5
    elif coin == 5:
        return 1

def count_conins(n):
    def helper(total, largest):
        if total < 0 or largest == None:
            return 0
        elif total == 0:
            return 1
        count_largest = helper(total-largest, largest) 
        count_next_largest = helper(total, next_smaller_coin(largest))
        return count_largest + count_next_largest
    
    return helper(n, 25)
