def print_upper_words(str_arr,must_start_with):
    for str in str_arr:
        for letter in must_start_with:
            if str.startswith(letter.lower()) or str.startswith(letter.upper()):
                print(str.upper())
                break


print_upper_words(["hello", "Hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})