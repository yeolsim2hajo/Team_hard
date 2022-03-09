def main():
    print(yon())

def yon():
    num = int(input())
    if num % 3 == 0:
        return 7
    elif num % 3 == 1:
        return 35
    else:
        return 50

main()