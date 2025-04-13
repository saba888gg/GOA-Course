number = input("chawere samnishna ricxvi: ")

if len(number) == 3:
    asi = int(number[0])
    ati = int(number[1])
    erti = int(number[2])

    sumnum = asi + ati + erti
    sum = int(number) % sumnum

    print(sum)
else:
    print("unda chawero samnishna ricxvi")