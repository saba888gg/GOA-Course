while True:
    number = int(input("Enter a number less than or equal to 50: "))
    if number <= 50:
        break 
    else:
        print("The number should be less than or equal to 50, please try again.")

for i in range(1, 101):
    if i % number == 0:
        print(i)