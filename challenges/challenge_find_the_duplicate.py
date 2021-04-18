from challenges.challenge_anagrams import sorter


def find_duplicate(nums):
    """ Faça o código aqui. """
    if not nums or isinstance(nums, str) or len(nums) <= 1:
        return False
    sorted = sorter(nums)
    for i, item in enumerate(sorted):
        if not isinstance(item, int) or item < 0:
            return False
        if item == sorted[i - 1]:
            return item
    return False
