def find_duplicate(nums):
    """ Faça o código aqui. """
    if nums is None or type(nums) != list or len(nums) <= 1:
        return False

    nums.sort()
    for i in range(len(nums) - 1):
        if type(nums[i]) == str or nums[i] < 0:
            return False
        if nums[i] == nums[i + 1]:
            return nums[i]

    return False
