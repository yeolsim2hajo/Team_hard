def bbq(level):
    if level == 2:
        return
    
    for i in range(3):
        bbq(level+1)

bbq(0)