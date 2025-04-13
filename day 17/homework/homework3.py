def manual_len(iterable):
    count = 0
    for _ in iterable:
        count += 1
    return count
print(manual_len("hello"))