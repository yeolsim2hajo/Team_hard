word = input().split()

cnt = 0
for i in word:
    if i.isupper():
        cnt += 1

if cnt == 3:
    print('풍족하다')
elif cnt == 0:
    print('부족하다')
else:
    print('적절하다')
