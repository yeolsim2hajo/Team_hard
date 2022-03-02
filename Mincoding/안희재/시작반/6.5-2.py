str = input()
# ord'a'는 97
# b입력받으면 2개. 98
for i in range(ord(str),ord('a')-1,-1):
    print(chr(i), end='')
