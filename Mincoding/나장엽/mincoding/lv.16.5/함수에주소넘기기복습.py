# 2x3 리스트에서 최대값을 찾는 함수

def Max(arr):
    # max 값을 초기화
    max = arr[0][0]
    #! 2중for문을 이용해 arr의 요소들 중에서 가장 큰 값을 찾는 코드
    #todo 조건문에서 else를 잘 생각해야함.
    for row in range(2):
        for col in range(3):
            if max < arr[row][col]:
                max = arr[row][col] 
            else:
                max=max
    return max

#! 2x3 리스트에서 최소값을 찾는 함수
#todo 조건문에서 else를 잘 생각해야함.

def Min(arr):
    min = arr[0][0]
    for row in range(2):
        for col in range(3):
            if min > arr[row][col]:
                min = arr[row][col] 
            else:
                min = min 
    return min

num = list(map(int, input().split()))

#* 2x3 리스트를 선언
arr = [[0 for col in range(3)]for row in range(2)]

#* 입력받은 숫자들을 2x3리스트에 집어넣기.
#todo index를 조작하는 방법 생각 잘하기.
for i in range(len(num)):
    arr[i//3][i%3] = num[i]

#* 함수로부터 리턴받은 max와 min 값을 2중for문을 이용해, arr의 요소들과 하나씩 비교, 같다면, 좌표값을 출력.
for k in range(2):
    for a in range(3):
        if Max(arr) == arr[k][a]:
            print("({0},{1})".format(k, a))
        if Min(arr) == arr[k][a]:
            print("({0},{1})".format(k, a))