def is_palindrome_iterative(word):
    for index in range((len(word)+1)//2):
        if word[index] != word[-index-1]:
            return False
    
    return True
