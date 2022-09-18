s = list(input())
c1, c2 = input().split()

for i in range(len(s)):
    
    if s[i] == c1:
        if i == 0:
            s[i+1] = '#'
        else:
            s[i-1] = '#'
            s[i+1] = '#'
    
    if s[i] == c2:
        if i == 6:
            s[i-1] = '#'
        else:
            s[i-1] = '#'
            s[i+1] = '#'
print(''.join(s))