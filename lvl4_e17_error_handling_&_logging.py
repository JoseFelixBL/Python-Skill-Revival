"""
Error Handling & Logging
    Take your "Basic Calculator" or "API Consumption" code.

    Wrap the risky parts in `try...except` blocks to handle specific 
    exceptions (e.g., `ValueError`, `ZeroDivisionError`, 
    `requests.exceptions.RequestException`).
    
    Use the `logging` module to log informative messages (debug, 
    info, error) instead of just printing.
"""
import logging

def calculate(number_1:int, number_2:int, operator:str)->int | str:
    """
    Receives 2 int and an operation\n
    Returns the operation result on the received ints
    """
    logging.debug("Dentro de calculate")
    match operator:
        case "+":
            logging.debug("Suma")
            result = number_1 + number_2
        case "-":
            logging.debug("Resta")
            result = number_1 - number_2
        case "*":
            logging.debug("Multiplicación")
            result = number_1 * number_2
        case "/":
            logging.debug("División")
            if number_2 == 0:
                logging.info('No se puede dividir entre 0')
                result = "Error: División entre 0"
            else:
                result = number_1 / number_2
        case _:
            logging.info("Input Error: Otro operador")
            result = "EL operador no es correcto, solo +, -, *,  /"
    return result

def accept_number(order:str)->int:
    """
    Asks for user input of a number including 'order' in the prompt.\n
    Checks and enforces input to be a number.\n
    Returns the number.
    """
    logging.debug("Dentro de accept_number")
    while True:
        logging.debug("Pidiendo el número")
        r = input(f"Inserte el {order} número: ")

        try:
            logging.debug("Intentando la conversión del str a int")
            r = int(r)
            logging.info(f"{order}: {r} es un int")
            break
        except Exception as ex:
            logging.warning(f"Problema con lo insertado: {r}\t - Exception: {ex}")
            print("Asegúrese de que introduce un número")
            continue
    return r


logging.basicConfig(filename='lvl4_e17.log', encoding='utf-8', level=logging.INFO)

logging.debug("Antes del while")
while True:
    logging.debug("Dentro del while de pedir los números y el operador")
    num_1 = accept_number("primero")
    num_2 = accept_number("segundo")
    op = input("Elija operación (+, -, *, /): ")
    logging.INFO(f"Operador {op}")
    resultado = calculate(num_1, num_2, op)
    logging.info(f"Resultado: {resultado}")
    print(f"El resultado de {num_1} {op} {num_2} = {resultado}")
    print()
    if input("otra operación (S/N): ").lower() != 's':
        logging.debug("Termiando...")
        break
