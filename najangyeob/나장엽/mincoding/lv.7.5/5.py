arr = list(input().split())


cnt = 0
for i in range(len(arr)):
    if arr[i].isupper() == True:
        cnt += 1
        
if cnt >= 3:
    print('풍족하다')
elif 1 <= cnt <= 2:
    print('적절하다')
else:
    print('부족하다')