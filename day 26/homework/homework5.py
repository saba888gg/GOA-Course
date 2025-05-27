def math_op(x, y, op):
    if op == "+":
        return type(x + y)
    elif op == "*":
        return type(x * y)
    else:
        if type(x) == int and type(y) == int:
            if op == "-":
                return type(x - y)
            elif op == "/":
                return type(x / y)
    
print(math_op(5, 20, "+"))
print(math_op(5, "9", "*"))
print(math_op(7, 10, "-"))
print(math_op(10, 5, "/"))