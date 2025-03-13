sityva =input("please enter word with three leter: ")
while len(sityva) != 3:
    sityva = input("try again please enter word with three leter: ")

if sityva == sityva[::-1]:
    print(True)
else:
    print(False)    
 