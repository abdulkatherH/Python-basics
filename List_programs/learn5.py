# Decorator with Arguments
# If your function takes argumnets, the wrapper should handle them too.
def smart_divide(func):
    def wrapper(a, b):
        print(f"Dividing {a} by {b}")
        if b == 0:
            print("Cannot divide by zero!")
            return
        return func(a, b)
    return wrapper
@smart_divide
def divide(a, b):
    print(a / b)

divide(10, 2)
divide(10, 0)