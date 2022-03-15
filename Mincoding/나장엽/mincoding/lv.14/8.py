str = list(input())
for i in range(len(str)):
    str[i] = ord(str[i])

for i in range(0 , len(str)-1): #0~4 인덱스까지
    for j in range(i+1, len(str)): 
        if str[i] > str [j] : 
            str[i], str[j] = str[j], str[i]



for i in range(len(str)):
    print(chr(str[i]), end='')