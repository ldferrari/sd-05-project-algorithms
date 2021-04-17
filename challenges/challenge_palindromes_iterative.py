def is_palindrome_iterative(word):
    if not word:
      return False
    return True if word == word[::-1] else False
