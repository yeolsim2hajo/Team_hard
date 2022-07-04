# 백준 20291 파일 정리

n = int(input())
dic = dict()
for _ in range(n):
    a = input()
    for i in range(len(a)):
        if a[i] == '.':
            b = a[i+1:]
            break
    if b not in dic:
        dic[b] = 1
    else:
        dic[b] += 1

sort_dic = sorted(dic.items(), key=lambda x:x[0])

for i in range(len(dic)):
    print(sort_dic[i][0], sort_dic[i][1])