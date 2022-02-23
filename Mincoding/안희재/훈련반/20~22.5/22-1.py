card = ['A', 'B', 'C']
path = [''] * 2

def abc(level):
    if level == 2:
        for i in range(2):
            print(path[i], end='')
        print()
        return
    
    for i in range(3):
        path[level] = card[i]
        abc(level+1)


abc(0)