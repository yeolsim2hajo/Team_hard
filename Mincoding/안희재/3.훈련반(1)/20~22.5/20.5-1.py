def abc(level):
    if level == 3:
        return
    
    abc(level+1)

abc(0)