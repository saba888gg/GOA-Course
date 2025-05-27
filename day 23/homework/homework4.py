def mix_strings(*args):
    strings = []
    numbers = []

    for item in args:
        if isinstance(item, int):
            numbers.append(str(item))
        else:
            strings.append(str(item))

    result = strings + numbers
    return " ".join(result)