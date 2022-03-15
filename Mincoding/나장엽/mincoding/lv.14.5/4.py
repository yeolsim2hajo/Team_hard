str1 = list(input())
str2 = list(input())

def Sort(str): 
    for i in range(0 , len(str)-1): 
        for j in range(i+1, len(str)): 
            if str[i] > str [j] : 
                str[i], str[j] = str[j], str[i]
    return str


str1 = Sort(str1)
str2 = Sort(str2)

str1.extend(str2)


print(*str1, sep='')