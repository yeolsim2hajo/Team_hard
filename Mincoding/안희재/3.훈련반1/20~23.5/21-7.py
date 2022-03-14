word = input()
length = len(word)
# 5면 5 4 3 2 1 2 3 4 5

def abc(level):
    if level == 1:
        print(level, end= ' ')
        return
    
    print(level, end= ' ')
    abc(level-1)
    print(level, end= ' ')


abc(length)
