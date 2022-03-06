s = list(input())
a = input()
b = input()

for i in range(len(s)):
    if s[i] == a:
        s[i] = b

for j in s:
    print(j, end='')
    
