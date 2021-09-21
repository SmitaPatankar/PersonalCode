def mymethod(a, b):
    """Add numbers.

    >>> mymethod(1,2)
    3
    """
    return a+b

if __name__ == "__main__":
    import doctest
    doctest.testmod()
