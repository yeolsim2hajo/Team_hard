#10818 최소, 최대
N = int(input())
numbers = list(map(int,input().split()))
print(min(numbers), max(numbers))

#10871 X보다 작은 수
N,X = map(int,input().split())
A = list(map(int, input().split()))
for number in A:
    if number < X:
        print(number, end=' ')

#10950 A+B - 3
T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(A+B)