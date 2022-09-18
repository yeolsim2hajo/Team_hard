arr = list(input().split())
name = ['원영','은비','채연']
cnt = [0,0,0]

for i in range(len(arr)):
    if arr[i] == name[0]:
        cnt[0] += 1
    elif arr[i]==name[1]:
        cnt[1] += 1
    else:
        cnt[2] += 1
        
max = cnt[0]
idx = 0       
for k in range(len(cnt)):
    if max < cnt[k]:
        max = cnt[k]
        idx = k
    else:
        max = max