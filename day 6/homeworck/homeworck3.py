correct_password = "saba5"

limit = 3
I = 0
while I < 3:
    password = input("enter your password:")
    if password == correct_password:
        print("password is correct")
        I = 5
    else:
        print("password is incorrect")    
       
    if I == 2:
        print("limiti amoiwura")
    I += 1
