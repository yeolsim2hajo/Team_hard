# 0보다 크거나 같고, 99보다 작거나 같은 정수가 주어질 때 다음과 같은 연산을 할 수 있다.
# 주어진 수가 10보다 작다면 앞에 0을 붙여 두자리 수로 만들고,
# 각 자리의 숫자를 더한다
# 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다.

# 예시 
# 26부터 시작 -> 2 + 6 = 8, 새로운 수는 68이다. 6+8=14  새로운 수는 8+4 = 12 새로운 수는 42이다. 
# 4+2 = 6 새로운 수는 26
# 위의 예는 4번만에 원래의 수로 돌아올 수 있다. 따라서 26의 사이클은 4이다.
# N이 주어졌을 때 N의 사이클의 길이를 구하는 프로그램을 작성하라


def integer(num):
    global cycle_int
    while True:
        a = num // 10 # 2
        b = num % 10 # 6
        c = (a + b) % 10 # 8 
        num = (b * 10) + c # 60 + 8 = 68

        cycle_int += 1 # 사이클 수 + 1
        if (num == n): # 같게 되면 while 종료
            print(cycle_int)
            break

def string(num):
    global cycle_str
    while True:
        if len(num) == 1:
            num = '0' + num

        plus = str(int(num[0]) + int(num[1]))
        num = num[-1] + plus[-1]
        cycle_str += 1
        if num == n :
            print(cycle_str)
            break

n = int(input())
num_int = n
num_str = str(n)
cycle_int = 0
cycle_str = 0

integer(num_int)
string(num_str)