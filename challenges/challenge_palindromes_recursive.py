def is_palindrome_recursive(palavra, low, high):
    if  palavra == "" or palavra[low] != palavra[high] :
        return False
    if low == high:
        return True
    return is_palindrome_recursive(palavra, low + 1, high - 1);


print(is_palindrome_recursive("ANA", 0, len("ANA") - 1))