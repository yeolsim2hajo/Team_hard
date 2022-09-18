arr = [list(input()) for _ in range(2)] 


dat1=[0]*200
dat2=[0]*200
result = [0]*200
cnt = 0
for k in range(len(arr[0])):
    dat1[ord(arr[0][k])] = 1

for k in range(len(arr[1])):
    dat2[ord(arr[1][k])] = 1

for i in range(len(dat1)):
    result[i] = dat1[i] + dat2[i]
    
for i in range(len(result)):
    if result[i] == 2:
        cnt += 1



s1 = len(arr[0])
s2 = len(arr[1])
res= 0
if s1 > s2:
    res = s1 - cnt
else:
    res = s2 - cnt


print(res)