def main():
    a = getChar()
    print(a)
    
def getChar():
    a, b = input().split()
    if ord(a) > ord(b):
        return a
    else:
        return b
main()