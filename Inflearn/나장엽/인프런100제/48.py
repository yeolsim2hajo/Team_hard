str1 = 'AAABBBcccddd'
str2 = ''
for i in str1 :
    if i.isupper() :
        str2+= i.lower()
    else :
        str2+= i.upper()

print(str2)