"""
String Manipulation

    Write a function that takes a string and returns:
        The string reversed.
        The string in all uppercase.
        The number of vowels in the string.
"""

def string_manipulation(string):
    """
    string_manipulation: takes a string and returns:
        The string reversed.
        The string in all uppercase.
        The number of vowels in the string.
    """
    num_vocales = 0
    for letra in string:
        if letra in 'aeiou':
            num_vocales += 1
    return (string[::-1], string.upper(), num_vocales)


ENTRADA = "Hola, esto es una prueba."

str_reversed, str_to_upper, num_vocales = string_manipulation(ENTRADA)

print(f"String inicial: {ENTRADA}")
print(f"String al revés: {str_reversed}")
print(f"String en mayúsculas: {str_to_upper}")
print(f"Número de vocales en String: {num_vocales}")