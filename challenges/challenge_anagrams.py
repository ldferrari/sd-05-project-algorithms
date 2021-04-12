from challenges.quickSort import quicksort


def is_anagram(first_string, second_string):
    if len(first_string) != (len(second_string)):
        return False

    string1 = list(first_string)
    string2 = list(second_string)

    first_sorted = quicksort(string1, 0, len(string1) - 1)
    second_sorted = quicksort(string2, 0, len(string2) - 1)

    return first_sorted == second_sorted
