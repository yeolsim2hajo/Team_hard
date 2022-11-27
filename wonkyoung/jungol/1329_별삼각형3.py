N = int(input())
if N%2 and N <= 100:
    for i in range(N//2):
        print(' '*i+'*'*(2*i+1))
    for i in range(N//2, -1, -1):
        print(' '*i+'*'*(2*i+1))
else:
    print('INPUT ERROR!')