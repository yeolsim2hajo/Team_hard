arr = []
def abc(cnt, start, target, sub):
    if cnt == 1:
        arr.append([start, target])
        return 
    
    abc(cnt-1, start, sub, target)
    arr.append([start, target])
    abc(cnt-1, sub, target, start)
    
abc(3, 'A','B','C')
print(arr)
print(len(arr))
    
    