def is_anagram(first_string, second_string):
    if len(first_string) == len(second_string):
        letrasDaPrimeiraString = [letra for letra in first_string]
        letrasDaSegundaString = [letra for letra in second_string]
        return set(letrasDaPrimeiraString) == set(letrasDaSegundaString)

    return False
