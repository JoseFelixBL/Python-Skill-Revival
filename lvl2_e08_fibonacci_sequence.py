"""
Fibonacci Sequence
    Write a function to generate the first N numbers in the Fibonacci sequence 
    using both iterative and recursive approaches. Discuss the trade-offs.
"""
def fibonacci(n):
    """
    Fibonacci Sequence - iterative
        IN - for how many numbers
        OUT - list of numbers
    """
    fib = [1, 1]
    for _ in range(2,n):
        fib.append(fib[-1]+fib[-2])
    return fib

def fibonacci_recursive(n):
    """
    Fibonacci Sequence - recursive
        IN - for how many numbers
        OUT - list of numbers
    """
    if n == 2:
        return [1,1]

    fib = fibonacci_recursive(n-1)
    fib.append(fib[-1]+fib[-2])

    return fib

number = 10
print(f"Fibonaci sequence for {number} numbers (iterative): {fibonacci(number)}")
print(f"Fibonaci sequence for {number} numbers (recursive): {fibonacci_recursive(number)}")
