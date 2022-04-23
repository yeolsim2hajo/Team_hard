arr = [['D','A','S'], ['Q','W','V'], ['R','T','Y']]

def main():
    a, b = map(int,input().split())
    c, d = map(int,input().split())
    print(Find(a,b), Find(c,d))

def Find(x,y):
    return arr[x][y]

main()