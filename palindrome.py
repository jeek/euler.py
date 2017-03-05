def reverse_number(i):
    """Reverse a positive integer."""
    new_number = 0
    while i > 0:
        new_number = new_number * 10 + i % 10
        i /= 10
    return new_number

def is_palindrome(i):
    """Is this number a palindrome?"""
    return i == reverse_number(i)
