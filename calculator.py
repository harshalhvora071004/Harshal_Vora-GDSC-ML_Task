import math

def calculate(expression):
    try:
        result = eval(expression)
#The eval function in Python is used to evaluate a string containing a valid Python expression or code. It takes a single argument, which is a string representing a Python expression, and returns the result of evaluating that expression.
        return result
    except (SyntaxError, NameError, ZeroDivisionError, TypeError) as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    print("Calculator Application")
    print("Enter 'quit' to exit.")

    while True:
        expression = input("Enter a mathematical expression: ")

        if expression.lower() == "quit":
            break

        result = calculate(expression)
        print(f"Result: {result}")
