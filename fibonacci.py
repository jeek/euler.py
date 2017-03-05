def genfib(first_number, second_number):
    """Generate list of Fibonacci numbers"""
    yield first_number
    yield second_number
    while True:
        first_number, second_number = second_number, first_number + second_number
        yield second_number
