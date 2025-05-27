mylist = [1, 3, 5, 7, "string"]

def cl(x):
    new_list = []
    for i in x:
        if type(i) != int:
            continue
        else:
            new_list.append(i)
    return new_list

print(cl(mylist))