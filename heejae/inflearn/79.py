def sol(a, t):
    b = a.copy()
    c = []
    for i in range(t):
        b.insert(0,b.pop())
    for i,j in zip(a,b):
        c.append(abs(i-j))
    index = c.index(min(c))
    print("index :",index)
    print("value :",a[index],b[index])

sol(l,turn)