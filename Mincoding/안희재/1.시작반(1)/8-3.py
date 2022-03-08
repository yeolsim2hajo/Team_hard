arr = list(map(int,input().split()))

def Input():
    return arr[0] + arr[1]

def output():
    n = 5
    while n < Input()+1:
        print(n,end= ' ')
        n += 1

output()