def is_anagram(first_string, second_string):
    if not first_string or not second_string:
        return False
    list_first = list(first_string)
    list_second = list(second_string)
    f_i = 0
    s_i = 0
    while f_i < len(second_string):
        if list_second[s_i] == '' or list_first[f_i] != list_second[s_i]:
            s_i += 1
        list_second[s_i] = ''
        f_i += 1
        s_i = 0
    if s_i >= len(first_string):
        return False
    return True
