"""
List Operations

    Create a list of numbers. Write code to:
        Find the sum and average.
        Find the largest and smallest number.
        Create a new list with only the even numbers.
"""

LISTA_INICIAL = [1,2,3,4,5,6,7,8,9,10]
suma = 0
largest = smallest = None
only_even = []

for num in LISTA_INICIAL:
    suma += num
    if not largest:
        largest = num
    if not smallest:
        smallest = num
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
    if  num % 2 != 0:
        only_even.append(num)

average = suma / len(LISTA_INICIAL)

print(f"Lista Inicial: {LISTA_INICIAL}")
print(f"La suma de los números es: {suma}, la media (average) es: {average}")
print(f"El mayor número de la lista es: {largest}, el menor es: {smallest}")
print(f"Los número impares de la lista: {only_even}")