def manual_sum(*args):
    total = 0
    i = 0
    while i < len(args):
        total += args[i]
        i += 1
    return total