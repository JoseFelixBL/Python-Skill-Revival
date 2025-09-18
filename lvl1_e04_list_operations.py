"""
List Operations

    Create a list of numbers. Write code to:
        Find the sum and average.
        Find the largest and smallest number.
        Create a new list with only the even numbers.
"""

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