#  no bubbly :(
#  print(bubble_sort(['a', 'n', 'a', 'c', 'o', 'n', 'd', 'a']))

def quicksort(array, low, high):
    # caso base: se já atingiu a menor porção (1)
    if len(array) == 1:
        # retorne o array
        return array

    # os índices irão se cruzar quando o array estiver ordenado
    if low < high:
        # índice da partição é o índice onde o array foi divido
        # e é determinado a partir do pivô.
        # Este índice já está ordenado
        partition_index = partition(array, low, high)

        # Ordena os elementos presentes antes da partição (menores que o pivô)
        # e depois (maiores que o pivô)
        quicksort(array, low, partition_index - 1)
        quicksort(array, partition_index + 1, high)


# função auxiliar responsável pela partição do array
# escolhendo um pivô e fazendo movimentações dos sub arrays gerados
def partition(array, low, high):
    # índice do menor elemento
    i = low - 1
    # o pivô será escolhido
    # através do índice que divide o array
    pivot = array[high]  # pivot

    # itera sobre os elementos
    for j in range(low, high):
        # se o elemento corrente é menor ou igual ao pivô
        if array[j] <= pivot:
            # incrementa o índice do menor elemento
            i = i + 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]

    return i + 1


#  arraia = list('pedro')
#  quicksort(arraia, 0, len(arraia)-1)
#  print(arraia)


def is_anagram(first_string, second_string):
    if len(first_string) != (len(second_string)):
        return False

    first_arrayed = list(first_string)
    second_arrayed = list(second_string)

    quicksort(first_arrayed, 0, len(first_arrayed)-1)
    quicksort(second_arrayed, 0, len(second_arrayed)-1)

    return first_arrayed == second_arrayed
