#피보나치 함수
# fibo(n)을 호출했을 때 fibo(1) 과 fibo(0)이 몇 번 호출되었는지 검사하는 프로그램


t = int(input())
# fibo(0) = 0
# fibo(1) = 1
# fibo(2) = fibo(1) + fibo(0)
# fibo(3) = fibo(2) + fibo(1) # fibo(3)에서 0과 1의 호출 회수는? fibo(2)와 fibo(1)의  0과 1의 호출 횟수 
# fibo(4) = fibo(3) + fibo(2) # fibo(4)에서 0과 1의 호출 회수는? fibo(3)과 fibo(2)의 0과 1의 호출 횟수
# 호출 회수 또한 피보나치 수열을 따르고 있다.
# 0부터 2까지는 미리 배열을 만들고, 이보다 큰 숫자에서는 0과 1의 호출 횟수를 추가로 저장
# 배열을 만들어서 저장하는 이유?. 다이나믹프로그래밍을 통해 이미 구한 숫자를 또다시 구하는 일이 없도록하여 시간을 단축하기 위함.



zero = [1, 0, 1]
one = [0, 1, 1]

def fibo(n):
    if len(zero) <= n: # 배열의 길이보다 입력받은 숫자의 값이 크거나 같으면 반복문을 시작 -> 그렇지 않다면? 이미 배열에 저장되어 있는 값을 출력한다.
        for i in range(len(zero), n + 1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    print(zero[n],one[n])

for i in range(t):
    n = int(input())
    fibo(n)