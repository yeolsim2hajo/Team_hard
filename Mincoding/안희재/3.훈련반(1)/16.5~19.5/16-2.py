arr = [['A','B','K','T'], ['K','F','C','F'], ['B','B','Q','Q'], ['T','P','Z','F']]

T = input().split()

cnt1 = 0
cnt2 = 0

for i in range(len(arr)):
    for j in arr[i]:
        if j == T[0]:
            cnt1 += 1
        if j == T[1]:
            cnt2 += 1

print(cnt1+cnt2)