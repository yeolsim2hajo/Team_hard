# 
# 

# 1000번 - 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램

from unicodedata import decimal


a, b = map(int, input().split()) # 입력값을 공백 기준으로 나누고 정수형으로 변환
print(a+b)

# 1001번 - 두 정수 A와 B를 입력받은 다음, A-B를 출력하는 프로그램

a, b = map(int, input().split())
print(a-b)

# 1271번

# 첫째 줄에는 최백준 조교가 가진 돈 n과 돈을 받으러 온 생명체의 수 m이 주어진다.\
# (1 ≤ m ≤ n ≤ 101000, m과 n은 10진수 정수)
# 첫째 줄에 생명체 하나에게 돌아가는 돈의 양을 출력한다.
# 그리고 두 번째 줄에는 1원씩 분배할 수 없는 남는 돈을 출력한다.

n, m = map(int, input().split())
print(n // m) # 몫
print(n % m) # 나머지

# 1550번 - 다시

# 16진수 -> 10진수
hex_num = input()
num_list = list(map(int, list(range(10))))
over_9_list = list(range(ord('A'), ord('F')+1))
over_9_list = list(map(chr, over_9_list))
num_list += over_9_list

print(num_list.find(hex_num))


# 2338번 - 두 수 A, B를 입력받아, A+B, A-B, A×B를 구하는 프로그램을 작성

a = int(input())
b = int(input())
print(a+b)
print(a-b)
print(a*b)

# 2475번
# 제조하는 컴퓨터마다 6자리의 고유번호
# 고유번호의 처음 5자리에는 00000부터 99999까지의 수 중 하나가 주어지며 6번째 자리에는 검증수가 들어감
# 검증수는 고유번호의 처음 5자리에 들어가는 5개의 숫자를 각각 제곱한 수의 합을 10으로 나눈 나머지

number_list = map(int, input().split())
square_num = 0
for number in number_list:
    square_num += number ** 2
print(square_num % 10)

# 2557번 - Hello World!를 출력
print('Hello World!')

# 2558번 - 두 정수 A와 B를 입력받은 다음, A+B를 출력
a = int(input())
b = int(input())
print(a+b)

# 2845번
'''
입력
첫째 줄에 1m2당 사람의 수 L (1 ≤ L ≤ 10)과
파티가 열렸던 곳의 넓이 P (1 ≤ P ≤ 1000)가 주어진다.

둘째 줄에는 각 기사에 실려있는 참가자의 수가 주어진다.
106보다 작은 양의 정수 5개가 주어진다.

출력은 첫째 줄에 다섯 개의 숫자를 출력해야 한다. 이 숫자는 상근이가 계산한 참가자의 수와
각 기사에 적혀있는 참가자의 수의 차이
'''
people, area = map(int, input().split())
people_journal = list(map(int, input().split()))
for journal in people_journal:
    dif = journal - people * area
    print(dif, end = ' ')

# 2914번
'''
첫째 줄에 앨범에 수록된 곡의 개수 A와 평균값 I가 주어진다.
(1 ≤ A, I ≤ 100) 평균값은 항상 올림을 해서 정수
첫째 줄에 적어도 몇 곡이 저작권이 있는 멜로디인지 출력한다.
'''
num, avg = map(int,input().split())
sing_num = num * (avg-1) + 1
print(sing_num) # 저작권 멜로디 개수 = 수록곡 개수 * 평균

# 3003번
'''
첫째 줄에 동혁이가 찾은 흰색 킹, 퀸, 룩, 비숍, 나이트, 폰의 개수가 주어짐
첫째 줄에 입력에서 주어진 순서대로 몇 개의 피스를 더하거나 빼야 되는지를 출력
체스는 총 16개의 피스를 사용하며, 킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개로 구성
'''
chess = [1, 1, 2, 2, 2, 8]
exist_chess = list(map(int, input().split()))
for idx in range(len(chess)):
    print(chess[idx] - exist_chess[idx], end = ' ')

# 3046번

'''
첫째 줄에 두 정수 R1과 S가 주어진다. 두 수는 -1000보다 크거나 같고, 1000보다 작거나 같다.
상근이는 정인이 생일 선물로 두 숫자 R1과 R2를 주려고 함
첫째 줄에 R2를 출력한다.
'''
R1, S = map(int, input().split())
print(2*S - R1)

