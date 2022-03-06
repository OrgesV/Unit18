def flip_case(phrase, to_swap):
    string = ""
    for letter in phrase:
        if to_swap.upper() == letter:
            string = string + letter.lower() 
        elif to_swap.lower() == letter:
            string = string + letter.upper()
        else:
            string = string + letter
    return string
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
print(flip_case('Aaaahhh', 'h'))