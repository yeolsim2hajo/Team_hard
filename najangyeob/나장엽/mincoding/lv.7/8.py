arr = [[3,4,1],[2,1,4],[3,3,0]]
cnt1 = 0
cnt2 = 0
for i in range(3):
    for k in range(3):
        if arr[i][k] % 2 == 1:
            cnt1 += 1
        else:
            cnt2 += 1
            
print(f'짝수 : {cnt2}')
print(f'홀수 : {cnt1}')