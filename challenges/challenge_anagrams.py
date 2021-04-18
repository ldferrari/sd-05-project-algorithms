def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    if sorter(first_string) == sorter(second_string):
        return True
    return False


def sorter(word):
    word_to_sort = list(word)
    if not word or word == '':
        return []
    first_item = word_to_sort[0]
    less_than = sorter([letter for letter in word_to_sort[1:]
                        if letter < first_item])
    greater_than = sorter([letter for letter in word_to_sort[1:]
                           if letter >= first_item])
    return less_than + [first_item] + greater_than
