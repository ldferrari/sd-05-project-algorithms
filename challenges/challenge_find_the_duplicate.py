def find_duplicate(nums):
    sorted_nums = sorted(nums)
    for index in range(len(sorted_nums) - 1):
        if type(sorted_nums[index]) != int:
            return False
        elif sorted_nums[index] < 0:
            return False
        elif sorted_nums[index] == sorted_nums[index+1]:
            return sorted_nums[index]
    return False
