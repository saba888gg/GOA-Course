age = int(input("შეიყვანე შენი ასაკი: "))

if age <= 10:
    print("Kid")
elif age > 10 and age < 18:
    print("teenager")
elif age >= 18 and age < 30:
    print("adult")
else:
    print("unc")