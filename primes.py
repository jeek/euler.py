def prime_factors(i):
    """Yield prime factors of a number"""
    j = 2
    while i > 1:
        if i % j == 0:
            yield j
            i /= j
        else:
            j += 1
