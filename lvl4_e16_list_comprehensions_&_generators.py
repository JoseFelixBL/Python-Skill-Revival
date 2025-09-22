"""
List Comprehensions & Generators
    Take the exercises from Level 1 (e.g., finding even numbers, squaring 
    numbers) and rewrite them using list comprehensions.
    For a large range of numbers, create a generator expression to find even 
    numbers instead of a list comprehension. Explain the memory difference.
"""
"""
# lvl1_e04_list_operations.py
# Already used list comprehension!

LISTA_INICIAL = [8,9,10,3,6,4,1,2,5,7]

suma = 0
for num in LISTA_INICIAL:
    suma += num

average = suma / len(LISTA_INICIAL)

lista = LISTA_INICIAL.copy()
lista.sort()
smallest = lista[0]
largest = lista[-1]

only_even = [num for num in lista if num % 2 == 0]

print(f"Lista Inicial: {LISTA_INICIAL}")
print(f"La suma de los números es: {suma}, la media (average) es: {average}")
print(f"El mayor número de la lista es: {largest}, el menor es: {smallest}")
print(f"Los números pares de la lista: {only_even}")
"""
import random

def enteros_aleatorios(cuantos):
    contador = 0
    while contador < cuantos:
        yield(random.randint(1, 1000))
        contador +=1

def operaciones(maximo):
    """
    Creates a list of 'maximo' number of random integers [1-1000]
    Returns:
        - smallest, 
        - largest, 
        - suma, 
        - average, 
        - list_random, 
        - only_even
    """
    smallest = None
    largest = None
    only_even = []
    list_random = []

    for numero in enteros_aleatorios(maximo):
        list_random.append(numero)
        if not numero % 2:
            only_even.append(numero)

        if not smallest:
            smallest = numero
        elif numero < smallest:
            smallest = numero

        if not largest:
            largest = numero
        elif numero > largest:
            largest = numero

        suma = sum(list_random)
        average = suma / len(list_random)

    return smallest, largest, suma, average, list_random, only_even

menor, mayor, suma_tot, media, lista_final, solo_pares = operaciones(20)

print(f"{menor=}")
print(f"{mayor=}")
print(f"{suma_tot=}")
print(f"{media=}")
print(f"{lista_final=}")
print(f"{solo_pares=}")