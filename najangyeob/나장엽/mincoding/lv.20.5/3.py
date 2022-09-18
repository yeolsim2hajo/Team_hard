str = list(input())

length = len(str)//2

result = 0
if len(str) % 2 != 0:
    print('다른문장')
else:
    for i in range(length):
        if str[i] == str[i+3]:
            result = 1

if result == 1:
    print('동일한문장')