text = input("please enter: ")
number = int(input("please enter number: "))

if 1 <= number <= len(text):
    print(f"your: {text[number - 1]}")
else:
    print("your name is not faound")