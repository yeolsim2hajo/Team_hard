N = int(input())
s = '*'

i = 1
while i <= N:
    print(' ' * (N-i) + s * i)
    i += 1