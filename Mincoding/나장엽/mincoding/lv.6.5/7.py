str1, str2 = input().split()


if str1.isupper() == True :
    str1 = str1.lower()
else:
    str1 = str1.upper()
    
if str2.isupper() == True :
    str2 = str2.lower()
else:
    str2 = str2.upper()
    
print(str1, str2)