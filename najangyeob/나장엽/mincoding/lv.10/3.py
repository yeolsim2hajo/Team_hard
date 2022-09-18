def main():
    KFC()
    
def KFC():
    a = chicken()
    b = coke()
    print(a, end='')
    print(b, end='')
    
def chicken():
    n = int(input())
    return n + 10

def coke():
    s = input()
    return s
    
main()