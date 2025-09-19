"""
Prime Checker
    Write a function to check if a number is prime. 
    Then, write a function to generate all prime numbers 
    up to a number N (using the Sieve of Eratosthenes for a challenge).
"""
def sieve_of_eratostenes(n):
    """
    Generate all prime numbers up to n
    """
    numbers = {n:"prime" for n in range(2, n+1)}
    print(numbers)

    for i in range(2, int(n/2)):
        if numbers[i] != "prime":
            continue
        for j in range(i*2, n+1, i):
            numbers[j] = "comp."

    return numbers

MAX_NUMBER = 120
primes = sieve_of_eratostenes(MAX_NUMBER)

print(f"Los números primos hasta el {MAX_NUMBER} son:")
print(f"{'':^8}", end="")
for num in range(2, MAX_NUMBER + 1):
    if primes[num] == "prime":
        print(f"{num:^8}", end="")
    else:
        print(f"{primes[num]:^8}", end="")
    if not num % 10:
        print()
