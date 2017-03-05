def sumsteplist(maxnumber, step):
    """Add up a range of numbers, skipping through it."""
    return reduce(lambda x, y: x + y, xrange(0, maxnumber, step))
