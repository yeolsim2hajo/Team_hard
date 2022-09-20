def sol():
    i = 0
    while i != 2:
        i = int(input())
        if i == 2:
            break
        d = list(input())
        step =0
        for i in d:
            if i =="(":
                step += 1
            elif i==")":
                step -=1

            if step !=0:
                return print(False)
        if step==0:
            return print(True)
sol()