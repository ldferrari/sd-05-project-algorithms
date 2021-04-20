def is_anagram(first_string, second_string):
    """Verifica se uma palavra é anagrama da outra. """

    # Verifica que não foi passado alguma string vazia.
    if not first_string or not second_string:
        return False

    # Verifica se o tamanho das palavras é o mesmo.
    if len(first_string) != len(second_string):
        return False

    return set(first_string) == set(second_string)
