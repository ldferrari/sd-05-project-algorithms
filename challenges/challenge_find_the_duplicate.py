from collections import Counter


def find_duplicate(numbers):
    duplicate = [i for i, count in Counter(numbers).items() if count > 1]

    if (duplicate):
        if (duplicate[0] < 0):
            return False
        return duplicate[0]

    return False
