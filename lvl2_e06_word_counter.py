"""
Word Counter
    Write a function that counts the frequency of each word in a given string. 
    Return a dictionary where keys are words and values are counts. 
    Ignore case and punctuation.
"""
import re


def word_counter(text):
    """
    Counts words from a string. Ignores case and punctuation.
    Returns a dict:
        "word_1": count_1[, "word_2: count_2[, ...]]
    """
    
    text_lc = text.lower()
    return_dict = dict()
    # Using regular expression module to manage punctuations
    patron = re.compile(r'[a-z]+')

    for pal in patron.findall(text_lc):
        if not return_dict.get(pal):
            return_dict[pal] = 0
        return_dict[pal] += 1
    
    return return_dict

texto = "Hola hola, Yo estoy bien, bien bien."
d_palabras = word_counter(texto)
print(f"Texto inicial:\n{texto}")
print()
print(f"Diccionario de palabras:\n{d_palabras}")