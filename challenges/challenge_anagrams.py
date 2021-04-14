def is_anagram(first_string, second_string):
    if first_string == '' or second_string == '':
        return False

    if len(first_string) != len(second_string):
        return False
    
    if first_string == second_string:
        return True

    first_string_char_list = []
    second_string_char_list = []

    for char1 in first_string:
        first_string_char_list.append(char1)
        for char2 in second_string:
            second_string_char_list.append(char2)
        if char1 in second_string_char_list and char2 in first_string_char_list:
            return True

    return False
