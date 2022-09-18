def main():
    print(yesOrNo())
    
def yesOrNo():
    n = int(input())
    if n % 3 == 0:
        return 7
    elif n % 3 == 1:
        return 35
    elif n % 3 == 2:
        return 50
main()