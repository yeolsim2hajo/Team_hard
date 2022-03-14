# 처음 코드 - 실패
word = input()
a, b = input().split()

result = []

for i in range(len(word)):
    if word[i] == a:
        result[i] = a
    elif word[i] == b:
        result[i] = b
    else:
        result[i] = '#'

print(''.join(result))

# 아 이게 아니지.. 양옆만 #이잖아