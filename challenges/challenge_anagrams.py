# 1. Chosing algorithm type:
# - excluding selection & insertion sorts, both using brute force;
# - bubble is iterating, which was already trained in other reqs;
# - tim sort, mix between insert & merge, is new to my knowledge;
# - preference for merge or quick sort to train divide & conquer.

# Final choice: Quick Sort
# "Determina um elemento pivô
# (nome dado ao elemento que divide o array em porções menores).
# Todos os elementos maiores que o pivô serão colocados a direita
# e os menores a esquerda.
# Tem complexidade de O(n log n). Ou pior caso, O(n2)".


# 2. Take quick sort algorithm code from course model
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


array = [100, 4, 6, 33, 56, 67]
quicksort(array, 0, len(array) - 1)
# print(array)


# 3. use quicksort in our function is_anagram
def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    # 3.1. Cut case where it can never be anagram
    if len(first_string) != (len(second_string)):
        return False
    # 3.2. Turn parameters into arrays
    first_array = list(first_string)
    second_array = list(second_string)
    # 3.3 apply quicksort to order both arrays
    quicksort(first_array, 0, len(first_array)-1)
    quicksort(second_array, 0, len(second_array)-1)
    # 3.4 return true or false depending on arrays comparisons
    if first_array == second_array:
        return True
    return False


print(is_anagram("sapos", "passo"))
print(is_anagram("bla", "bli"))
