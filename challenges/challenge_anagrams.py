def is_anagram(first_string, second_string):
    if not len(first_string) == len(second_string):
        return False
    f = [i for i in first_string]
    s = [i for i in second_string]
    return set(f) == set(s)
