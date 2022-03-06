def multiple_letter_count(phrase):
    dct = {}
    for l in phrase:
        dct[l] = dct.get(l,0) + 1
    return dct

    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """