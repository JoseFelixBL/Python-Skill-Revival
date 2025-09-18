"""
Basic Calculator

    Write a script that takes two numbers and an operator (+, -, *, /) from 
    the user and performs the calculation. Handle division by zero gracefully.
"""

number_1 = input("Please insert first number: ")
number_2 = input("Please insert second number: ")
operator = input("Insert an operator (+, -, *, /): ")

match operator:
    case "+":
        print(int(number_1) + int(number_2))
    case "-":
        print(int(number_1) - int(number_2))
    case "*":
        print(int(number_1) * int(number_2))
    case "/":
        print(int(number_1) / int(number_2))
    case _:
        print("EL operador no es correcto, solo +, -, *,  /")