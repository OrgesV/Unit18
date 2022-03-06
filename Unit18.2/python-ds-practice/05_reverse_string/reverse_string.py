def reverse_string(phrase):
    lst = list(phrase)
    lst.reverse()
    return "".join(lst)
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """