# 백준 1991 트리 순회

import sys
input = sys.stdin.readline
n = int(input())
dic = {}
for _ in range(n):
    x, y, z = input().split()
    dic[x] = [y, z]

def root1(m):
    print(m, end="")
    for i in range(2):
        if dic[m][i] != '.':
            root1(dic[m][i])
def root2(m):
    for i in range(2):
        if dic[m][i] != '.':
            root2(dic[m][i])
        if i == 0:
            print(m, end="")
def root3(m):
    for i in range(2):
        if dic[m][i] != '.':
            root3(dic[m][i])
    print(m, end="")

root1("A")
print()
root2("A")
print()
root3("A")

# 왜 .까지 받을 생각을 못했을까