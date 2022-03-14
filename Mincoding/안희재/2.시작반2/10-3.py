def chicken():
    num = int(input())
    return num + 10

def coke():
    str = input()
    return str

def KFC():
    a = chicken()
    a = str(a)
    b = coke()
    return a+b

def main():
    return KFC()

print(main())