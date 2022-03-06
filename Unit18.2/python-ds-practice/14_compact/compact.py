def compact(lst):
    temp = []
    for l in lst:
        if l:
            temp.append(l)
    return temp
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
print(compact([0, 1, 2, '', [], False, (), None, 'All done']))