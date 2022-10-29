


#220923
def palindrome():
    import sys
    new_input = sys.stdin.readline
    while True:
        numbers = new_input().rstrip()
        if numbers == '0':
            return
        if numbers == numbers[::-1]:
            print('yes')
        else:
            print('no')
palindrome()