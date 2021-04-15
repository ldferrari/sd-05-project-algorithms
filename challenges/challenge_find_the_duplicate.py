def find_duplicate(nums):
    if len(nums) <= 1:
        return False

    for number in nums:
        counter = nums.count(number)
        if type(number) != int or number < 0:
            return False

        elif counter != 1:
            return number

    return False
