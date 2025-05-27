mylist = [1, 2, 3, "saba", "rogor?", "ori", "400", True, False, 9.5]

def dt(x):
    str1 = 0
    int1 = 0
    float1 = 0
    bool1 = 0

    for i in x:
        if isinstance(i, str):
            str1 += 1
        elif isinstance(i, bool):
            bool1 += 1
        elif isinstance(i, int):
            int1 += 1
        else:
            float1 += 1

    print(f"string count: {str1}, \ninteger count: {int1}, \nfloat count: {float1}, \nboolean count: {bool1}")
    return max([str1, int1, float1, bool1])


print(dt(mylist))