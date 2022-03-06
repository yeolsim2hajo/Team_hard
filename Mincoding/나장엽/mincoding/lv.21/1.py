def abc(level):
    if level == 2:
        return

    for i in range(3):
        abc(level + 1)


abc(0)