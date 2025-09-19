"""
Palindrome Checker
    Write a function that checks if a given string is a palindrome 
    (ignoring spaces, punctuation, and case). 
    (e.g., "A man, a plan, a canal, Panama!" returns True).
"""
import re

def palindrome_checker(phrase):
    """
    IN - phrase
    OUT - {True|False}
    """
    normalized_phrase = phrase.lower()
    no_spaces = []
    patron = re.compile(r'[a-z]+')

    for pal in patron.findall(normalized_phrase):
        no_spaces.append(pal)

    final_phrase = "".join(no_spaces)

    back = 0
    for letter in final_phrase:
        back -= 1
        if letter != final_phrase[back]:
            return False
    return True

frase = "A man, a plan, a canal, Panama!"
print(f"La frase: \"{frase}\" {'es' if palindrome_checker(frase) else 'NO es'} palíndrome.")