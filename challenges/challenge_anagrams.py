def is_anagram(first_string, second_string):
    if len(first_string) == len(second_string):
        palavra_um = [letra for letra in first_string]
        palavra_dois = [letra for letra in second_string]
        return set(palavra_um) == set(palavra_dois)

    return False
