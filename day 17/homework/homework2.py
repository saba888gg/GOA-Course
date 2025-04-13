listn = [1, 2, 3, 4, 5, 6]

def manual_index(l, li):
    count = 0
    for i in l:
        if i != li:
            count+=1
        else:
            count+=1
            break
    count-=1
    return count

print(manual_index(listn, 1))

print(listn.index(1))