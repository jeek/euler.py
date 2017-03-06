"""
Functions relating to the Fibonacci sequence.
"""

def genfib(first_num, second_num):
    """Generate list of Fibonacci numbers"""
    yield first_num
    yield second_num
    while True:
        first_num, second_num = second_num, first_num + second_num
        yield second_num
