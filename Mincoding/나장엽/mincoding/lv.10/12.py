
def countdown(n):
    for i in range(n, 0, -1):
        print(i, end = ' ')
def Input():
    n = int(input())
    return n
def main():
    a = Input()
    countdown(a)
    
main()