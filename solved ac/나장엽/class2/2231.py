import sys
input = sys.stdin.readline

def func(start, end):
    answer = 0
    if start < 0:
        return 0
    for i in range(start, end):
        temp = list(map(int, str(i)))
        Sum = i + sum(temp)
        if (Sum == N):
            answer = i
            return answer


N = int(input())
length = len(str(N)) 
start = N - length*9
end = N
print(func(start, end))


# boj, 2231 : 분해합, python3
N = int(input())
result = 0

for i in range(1, N+1):        
    a = list(map(int, str(i)))  
    s = i + sum(a)              
    if(s == N):                 
        result = i                   
        break

print(result)