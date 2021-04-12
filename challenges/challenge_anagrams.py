def quicksort(array, low, high):
    if len(array) == 1:
        return array

    if low < high:
        partition_index = partition(array, low, high)

        quicksort(array, low, partition_index - 1)
        quicksort(array, partition_index + 1, high)


def partition(array, low, high):
    i = low - 1

    pivot = array[high]
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]

    return i + 1


def is_anagram(first_string, second_string):
    string1 = list(first_string)
    string2 = list(second_string)

    first_sorted = quicksort(string1, 0, len(string1) - 1)
    second_sorted = quicksort(string2, 0, len(string2) - 1)

    return first_sorted == second_sorted
