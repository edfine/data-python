def concat(values):
    '''Concatenate multiple strings

    >>> concat(['foo', 'bar', 'baz'])
    'foobarbaz'
    >>> concat(['foo', ' bar ', 'baz'])
    'foo bar baz'
    >>> concat(['foo', ' bar ', 5])
    Traceback (most recent call last):
    ...
    TypeError: can only concatenate str (not "int") to str
    '''
    result = ''
    for value in values:
        result += value
    return result


def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> average([20, 30, 70])
    40.0
    """
    return sum(values, 0.0) / len(values)
