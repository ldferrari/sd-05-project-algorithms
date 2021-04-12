def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    """Algoritmos com complexidade O(n log n): merge sort e quicksort"""

    first_string_list = list(first_string)
    second_string_list = list(second_string)
    first_string_ordered = merge_sort(first_string_list)
    second_string_ordered = merge_sort(second_string_list)

    return True if first_string_ordered == second_string_ordered else False

# Referência: https://pt.wikipedia.org/wiki/Merge_sort


def merge_sort(lista):

    if len(lista) <= 1:
        return lista

    meio = len(lista)//2
    # também é valido: meio = int(len(lista)/2)

    listaDaEsquerda = lista[:meio]
    listaDaDireita = lista[meio:]

    merge_sort(listaDaEsquerda)
    merge_sort(listaDaDireita)

    merge(listaDaEsquerda, listaDaDireita, lista)

    return lista


def merge(listaDaEsquerda, listaDaDireita, lista):
    i, j, k = 0, 0, 0

    while i < len(listaDaEsquerda) and j < len(listaDaDireita):

        if listaDaEsquerda[i] < listaDaDireita[j]:
            lista[k] = listaDaEsquerda[i]
            i += 1
        else:
            lista[k] = listaDaDireita[j]
            j += 1
        k += 1

    while i < len(listaDaEsquerda):

        lista[k] = listaDaEsquerda[i]
        i += 1
        k += 1

    while j < len(listaDaDireita):
        lista[k] = listaDaDireita[j]
        j += 1
        k += 1
