def is_anagram(first_string, second_string):
    if first_string =="" or second_string == "":
        return False

    lista1 = list(first_string)
    lista2 = list(second_string)

    lista1.sort()
    lista2.sort()

    pos = 0
    anagrama = True

    while pos < len(first_string) and anagrama:
        if lista1[pos] == lista2[pos]:
            pos = pos + 1
        else:
            anagrama = False

    return anagrama