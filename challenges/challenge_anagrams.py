def is_anagram(first_string, second_string):

    if len(first_string) == len(second_string):
        letra_primeira_string = [letra for letra in first_string]
        letra_segunda_string = [letra for letra in second_string]
        return set(letra_primeira_string) == set(letra_segunda_string)

    return False
