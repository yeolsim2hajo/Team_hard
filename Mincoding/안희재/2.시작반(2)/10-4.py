def getChar():
    a, b = input().split()
    if ord(a) > ord(b):
        return a
    else:
        return b

def main():
    print(getChar())

main()