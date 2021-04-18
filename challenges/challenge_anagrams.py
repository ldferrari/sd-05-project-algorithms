# Ajuda do repo da Virginia
def is_anagram(first_string, second_string):
    if len(first_string) == len(second_string):
        first = [i for i in first_string]
        second = [i for i in second_string]
        return set(first) == set(second)

    return False
