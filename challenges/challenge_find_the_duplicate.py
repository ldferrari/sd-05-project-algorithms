def find_duplicate(nums):
    """ Busca por duplicidade do número na lista. """

    if not nums or type(nums) == str:
        return False

    for n in nums:
        if type(n) != int or n < 0:
            return False

        if nums.count(n) > 1:
            return n

    return False
