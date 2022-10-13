def factorial(n):
    """Return th factorial of N, a positive integer."""
    if n == 1:
        return 1
    return n * factorial(n-1)

def recursive_multiplication(m, n):
    if n == 1:
        return m
    return m + recursive_multiplication(m, n-1)

def is_prime(n):
    def helper(n, m):
        if m == 1:
            return True
        return n % m != 0 and helper(n, m-1)
    
    if n == 1:
        return False
    else:
        return helper(n, n - 1)

def hailstone(n):
    def helper(n, count):
        print(n)
        count += 1
        if n == 1:
            return count
        if n % 2 == 0:
            return helper(n//2, count)
        else:
            return helper(n*3+1, count)

    return helper(n, 0)

def merge(n1, n2):
    if n1 == 0:
        return n2
    if n2 == 0:
        return n1
    if n1 % 10 < n2 % 10:
        return n1 % 10 + 10 * merge(n1//10, n2)
    else:
        return n2 % 10 + 10 * merge(n1, n2//10)