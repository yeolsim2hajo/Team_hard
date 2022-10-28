# 백준 2729 이진수 덧셈

T = int(input())
for i in range(T):
    a = input().split(' ')
    print(bin(int(a[0],2) + int(a[1],2))[2:])