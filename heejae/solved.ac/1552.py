import sys

n = sys.stdin.readline()
n= int(n)

for i in range(n):
    line= sys.stdin.readline()
    a,b = line.split()
    print(int(a)+int(b))