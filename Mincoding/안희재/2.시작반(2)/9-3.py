arr = ['A','F','G','A','B','C']
word = input().split()

cnt1 = 0
cnt2 = 0
for i in arr:
    if i == word[0]:
        cnt1 = 1
    if i == word[1]:
        cnt2 = 1

if cnt1 + cnt2 == 2:
    print('와2개')
elif cnt1 + cnt2 == 1:
    print('오1개')
else:
    print('우0개')