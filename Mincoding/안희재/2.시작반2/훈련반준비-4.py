arr1 = [402,401,302,301,202,201,102,101]
arr2 = ['KIM','TEA','SOM','OPPO','TOM','GDK','JAME','MIN']
num = int(input())

idx = 0
for i in range(len(arr1)):
    if arr1[i] == num:
        idx = i

print(arr2[idx])