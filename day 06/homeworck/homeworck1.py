num = int(input("please enter your number: "))
count = 0
for i in range(num):
    if i % 2 != 0:
        count += i
print(count)

      