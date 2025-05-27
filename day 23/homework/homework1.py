def safe_sum(a, b):
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
        raise ValueError("Unsupported type")

    return to_number(a) + to_number(b)