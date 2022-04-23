def getName():
    str = list(input().split())
    return str

def main():
    str = getName()
    if ord(str[0]) < ord(str[1]):
        fast = str[0]
    else:
        fast = str[1]
    print(fast)

main()