def repeat(phrase, num):
    temp = ""
    if  not isinstance(num, int) or num < 0 :
        return None
    for n in range(num):
        temp += phrase
    return temp
    """Return phrase, repeated num times.

        >>> repeat('*', 3)
        '***'

        >>> repeat('abc', 2)
        'abcabc'

        >>> repeat('abc', 0)
        ''

    Ignore illegal values of num and return None:

        >>> repeat('abc', -1) is None
        True

        >>> repeat('abc', 'nope') is None
        True
    """