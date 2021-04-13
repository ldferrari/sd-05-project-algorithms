def find_duplicate(nums):
    """ Faça o código aqui. """
    # 1. Take care of exceptions codable outside iterating
    # if not nums or len(nums) == 0 or type(nums) != int:
    #     return False
    # (took it away because too complex and inferred in next exceptions)
    # 2. Create a sorted nums array to facilitate comparing numbers
    sorted_nums = sorted(nums)
    # 3. Iterate through it to treat last exceptions
    for i in range(len(nums) - 1):
        if type(sorted_nums[i]) != int:
            return False
        elif sorted_nums[i] < 0:
            return False
        # 4. Iterate through it two by two to find repeated number
        elif sorted_nums[i] == sorted_nums[i+1]:
            repeated_num = sorted_nums[i]
            return repeated_num
    return False


array_test = [1, 3, 4, 2, 2]
print(find_duplicate(array_test))
# ``python challenges/challenge_find_the_duplicate.py`` succesfully returns 2

# Academic honesty: got help from student Cristian Duessel
# https://github.com/tryber/sd-05-project-algorithms/pull/9/files
