def is_palindrome_recursive(word, low, high):
    if word == "":
        return False
    if word[low] == word[high]:
        if low >= high:
            return True
        return is_palindrome_recursive(word, low + 1, high - 1)
    return False


print(is_palindrome_recursive("ANA", 0, 2))
