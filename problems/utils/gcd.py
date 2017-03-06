"""
Functions relating to Greatest Common Denominator
"""

def gcd(first_num, second_num):
    """Greatest common denominator."""
    while second_num:
        first_num, second_num = second_num, first_num % second_num
    return first_num

def lcm(first_num, second_num):
    """Least common multiple."""
    return first_num * second_num / gcd(first_num, second_num)
