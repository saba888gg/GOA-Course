def smart_divide(a, b):
    def to_number(x):
        if isinstance(x, bool):
            return int(x)
        if isinstance(x, (int, float)):
            return x
        if isinstance(x, str):
            if '.' in x:
                return float(x)
            else:
                return int(x)
        raise ValueError("Only numeric types are allowed")

    num1 = to_number(a)
    num2 = to_number(b)

    big = max(num1, num2)
    small = min(num1, num2)

    if small == 0:
        raise ZeroDivisionError("Cannot divide by zero")

    return big / small