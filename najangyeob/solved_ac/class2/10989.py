import sys
input = sys.stdin.readline

N = int(input())
dat = [0]*10001

for _ in range(N):
    number = int(input())
    dat[number] += 1

for i in range(len(dat)):
    if dat[i] != 0:
        for _ in range(dat[i]):
            print(i)