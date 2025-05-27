def type_check(x):
    if isinstance(x, str):
        return "Literature"
    elif isinstance(x, bool):
        return "Science"
    else:
        return "Math"
    

print(type_check("temo"))
print(type_check(5))
print(type_check(5.0))
print(type_check(True))