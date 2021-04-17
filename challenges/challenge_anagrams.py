def quicksort(array, low, high):

    if len(array) == 1:
        return array

    if low < high:
        partition_index = partition(array, low, high)

        quicksort(array, low, partition_index - 1)
        quicksort(array, partition_index + 1, high)


def partition(array, low, high):

    i = low - 1
    pivot = array[high]  # pivot

    for j in range(low, high):

        if array[j] <= pivot:

            i = i + 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]

    return i + 1


def is_anagram(first_string, second_string):
    """ Faça o código aqui. """

    first = list(first_string)
    quicksort(first, 0, len(first_string)-1)
    second = list(second_string)
    quicksort(second, 0, len(second_string)-1)
    return first == second
