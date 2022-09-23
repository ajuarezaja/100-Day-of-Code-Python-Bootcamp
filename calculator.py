# Calculator
from artcalc import logo

def add(n1, n2):
    """add n1 + n2 function"""
    return n1 + n2

def subtract(n1, n2):
    """subtract n1 - 2 function"""
    return n1 - n2


def multiply(n1, n2):
    """multiply n1 * 2 function"""
    return n1 * n2


def divide(n1, n2):
    """divide n1 / 2 function"""
    return n1 / n2

def calculator():
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }
    print(logo)
    num1 = float(input("What's the first number?: "))

    # while for asks needs more calculations
    should_continue = True

    while should_continue:
        # print the operations available
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 =float(input("What's the next number?: "))
        answer = operations[operation_symbol](num1, num2)
        print(f'{num1} {operation_symbol} {num2} = {answer}')
        more = input(f"Type 'y to continue calculations with {answer}, or type 'n' to exit, or type 's' to start a new calculation: ").lower()
        if more == "n":
            should_continue = False
        elif more == 'y':
            num1 = answer
        elif more == 's':
            calculator()
            should_continue = False


calculator()

