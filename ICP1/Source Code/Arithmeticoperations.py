def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if a != 0:
        return b / a
    else:
        return "cannot be divisible"


def operations():
    _input1 = int(input("Enter the first number:-"))
    _input2 =int(input("Enter the second number:-"))
    output = add(_input1, _input2)
    print("The addition of 2 numbers is", output)
    output = subtract(_input1, _input2)
    print("The subtraction of 2 numbers is", output)
    output = multiply(_input1, _input2)
    print("The multiplication of 2 numbers is", output)
    output = divide(_input1, _input2)
    print("The division of 2 numbers is", output)


operations()
