#Calculator

from art import logo
print(logo)

#Arithmatic ops
def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

arithmatic_operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

def calculator():
    num1 = float(input("What is the first number?: "))
    for ops in arithmatic_operations:
        print(ops)
    should_continue = True

    while should_continue:
        op_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        answer = arithmatic_operations[op_symbol](num1,num2)
        print(f"{num1} {op_symbol} {num2} = {answer}")
        if input(f"Enter 'y' to continue with {answer} or 'n' to start new calculation!.\n") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()