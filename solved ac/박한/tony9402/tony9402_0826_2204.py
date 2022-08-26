# 백준 2204 도비의 난독증테스트

while 1:
    n = int(input())
    if n == 0:
        break
    dic = dict()
    for _ in range(n):
        a = input()
        dic[a.lower()] = a
    dic1 = sorted(dic.items())
    print(dic1[0][1])