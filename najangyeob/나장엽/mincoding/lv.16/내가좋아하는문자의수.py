arr = [["A","B","K","T"],["K","F","C","F"],["B","B","Q","Q"],["T","P","Z","F"]]

str1, str2 = list(input().split())

# 알파벳은 26개
alpha_check = [0]*27
cnt1 = 0
cnt2 = 0
for i in range(4):
    for j in range(4):
        if arr[i][j] == str1:
            cnt1 += 1
        if arr[i][j] == str2:
            cnt2 += 1
print(cnt1+cnt2)