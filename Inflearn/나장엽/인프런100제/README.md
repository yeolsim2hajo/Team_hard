problem 66번
```
arr = ['ABCDEF', 'BCAD', 'ADEFQRX', 'BEDFG', 'AEBFDGCH']
target = 'ABCD'

def check(lst, target):
    temp = target.index(target[0])
    for i in lst:
        if i in target:
            if temp > target.index(i):
                return False
            temp = target.index(i)
            
    return True

def func(arr, target):
    answer = []
    for i in arr:
        answer.append(check(i, target))
        
    return answer

print(func(arr, target))
```

규칙을 지킨 문자열인지 검사하는 문제
arr을 하나씩 분할하여 check함수에 매개변수로 전달하여 
규칙의인덱스와 전달받은 부분 문자열의 인덱스의 값을 비교하여 해결!


problem 65번

```
a = [1,2,3,4]
b = ['a','b','c','d']


answer = []    
index = 0
for i, k in zip(a, b):
    if index % 2 == 0: 
        answer.append([i, k])
    else:
        answer.append([k, i])
    index += 1
    
print(answer)
```
두 배열의 값을 하나씩 번갈아가며 합치는 문제.
처음에는 그냥 합쳤다가, 문제를 자세히 봐야겠다.
% 연산자를 사용하여, 간단하게 해결 할 수 있음.

problem 64번
```
#64번 이상한 엘리베이터
n = int(input())
result = 0

while True:
    if n%7 == 0: 
        result += n//7
        print(result)
        break
    n -= 3
    result += 1
    if n < 0:
        print(-1)
        break
```
정량 n에 정확히 맞춰야 움직이는 엘리베이터 문제.
n을 입력받고, 7로 나누어 떨어지면 그대로 n을 7로 나누어 출력하면 끝
나누어 떨어지지 않으면, 3kg으로씩 빼면서 다시 검사하고 어떻게 해도 n이 0이 되지 않아서 0보다 작아지면 -1을 출력하게 하였습니다.

problem 63
```
string = list(input().split())
for i in range(len(string)):
    print(string[i][0], end = '')
```
문장을 입력받고, 문장의 첫글자만 따서 출력하는 문제
list로 입력받고, 리스트 인덱싱을 이용하여 출력하였음.


problem 62
```
string = 'aacdddddddddeee'

a = string.count('a') # 2
b = string.count('b') # 0
c = string.count('c') # 1
d = string.count('d') # 9
e = string.count('e') # 3

print(str(a)+str(b)+str(c)+str(d)+str(b)+str(d)+str(a)+str(e))
```
숫자를 사용하지 않고 숫자를 출력하는 문제.
간단하게 알파벳을 이용하고, count함수를 이용해 갯수를 반환받아 출력하였음.