def cal():
    num = int(input())
    if num >= 90:
        return 'A'
    elif num >= 80:
        return 'B'
    elif num >= 70:
        return 'C'
    else:
        return 'D'

def main():
    print(cal())

main()