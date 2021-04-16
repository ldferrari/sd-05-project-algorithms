def find_duplicate(nums):
    if (type(nums) is not list) or (len(nums) == 0):
        return False
    dict = {}
    for num in nums:
        if num not in dict.keys():
            dict[num] = True
        else:
            return num
    return False
