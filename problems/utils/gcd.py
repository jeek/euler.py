def gcd(a, b):
    """Greatest common denominator."""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Least common multiple."""
    return a * b / gcd(a, b)