"""
FizzBuzz (The Classic)

    Print numbers from 1 to 100.
    For multiples of 3, print "Fizz".
    For multiples of 5, print "Buzz".
    For multiples of both 3 and 5, print "FizzBuzz".
"""
for num in range(1,101):
    # For making the output in lines of 10 - more readable
    if num % 10 == 1:
        print()

    salida = ""
    if num % 3 == 0:
        salida = "Fizz"
    if num % 5 == 0:
        salida += "Buzz"
    if not salida:
        salida = num

    print(f"{salida:^10}", end="")
print()
