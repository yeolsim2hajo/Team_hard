### solved.ac 를 풀면서 느낀점
1. 기존에 풀었던 방식으로는 시간초과가 많이 발생한다.
2. 코드의 최적화 + 시간 줄이기가 필요
3. 각종 라이브러리에 대한 학습이 필요할 것 같다.


### 라이브러리 학습 예정
1. Counter
2. itertools

### 어려웠던 문제
* 다른 사람들이 푸는 것과 동일한데 시간초과가 발생한다.
* 함수로 선언한 다음 사용하는 것과 다른 것인가?
* 무슨 차이가 있는지 모르겠다. -> 찾아봐야겠음.


1. 시간 초과 코드
```python
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
trees = list(map(int, input().split()))

meter = 1
index = 0
take_tree = 0

while True:
    if take_tree == M:
        break

    temp = 0
    for i in range(N):
        if trees[i] <= meter:
            temp +=  0
        else:
            temp += trees[i] - meter
        
        if temp > M:
            break

    take_tree = temp
    if take_tree != M:
        meter += 1

print(meter)

````
2. 시간초과 코드
```python
# 이분탐색 알고리즘 쓰기
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))
start, end = 1, max(trees)

while start <= end:
    mid = (start+end) // 2
    cutting = 0

    for tree in trees:
        if tree > mid:
            cutting += tree - mid
        
    if cutting >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)
```