num = int(input("please input a number: "))
count = 0
for i in range(2,num):
    print("your number is not a prime")
    count += 1
if count == 0:
    print("your number is a prime")    