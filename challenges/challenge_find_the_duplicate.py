def find_duplicate(nums):
    nums.sort()
    for index in range(1, len(nums)):
        if type(nums[index]) != int or nums[index] < 0:
            return False
        elif nums[index] == nums[index - 1]:
            return nums[index]
