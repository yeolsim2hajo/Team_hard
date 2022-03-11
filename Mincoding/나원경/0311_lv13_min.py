#lv13
#8 두 배열이 완전히 똑같은지 비교하기
def main():
    arr = [3,5,1,2,7]
    input_arr = list(map(int,input().split()))
    compare_go(arr, input_arr)
def compare_go(arg1, arg2):
    if arg1 == arg2:
        print('두배열은완전같음')
    else:
        print('두배열은같지않음')

main()

#lv13.5
#1 구조체 문제
#2 너와 나의 거리 구하기
away = [4,2,5,1,6,7,3]
start, end = input().split()
start = ord(start) - ord('A')
end = ord(end) - ord('A')
if start < end:
    print(sum(away[start+1:end]))
else:
    print(sum(away[end + 1:start]))


#3 각각 계산하기
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
result = [0]*5
for i in range(5):
    result[i] = a[i] * b[i] +c[i]

print(*result)


#4 MAX, MIN의 좌표찾기
arr = [[3,4,1,6],[3,5,3,6],[0]*4,[5,4,6,0]]
arr[2] = list(map(int, input().split()))
max_val = 0
min_val = arr[0][0]
for i in range(4):
    for j in range(4):
        if max_val < arr[i][j]:
            max_val = arr[i][j]
            y_max, x_max = i,j
        elif min_val > arr[i][j]:
            min_val = arr[i][j]
            y_min, x_min = i,j
print(f'MAX={max_val}({y_max},{x_max})\nMIN={min_val}({y_min},{x_min})')

#5 입력받은 숫자에 해당하는 문자 출력
arr = [['4','5','7','1','3','2'],['D','F','Q','W','G','Z']]
n = input()
for i in range(6):
    if arr[0][i] == n:
        print(arr[1][i])
        break

#6 A, B, C가 몇개인지 알려주는 함수 만들기
def main():
    mun = input()
    jang = input()
    print('A:{}\nB:{}\nC:{}'.format(*findABC(mun, jang)))

def findABC(*args):
    cnt = [0]*3
    for i in range(len(args)):
        for alp in args[i]:
            if alp == 'A':
                cnt[0] += 1
            elif alp == 'B':
                cnt[1] += 1
            elif alp == 'C':
                cnt[2] += 1
    return cnt

main()

#7 좌표를 지정하면 값 반환하기
arr = [['D','A','S'],['Q','W','V'],['R','T','Y']]
def main():
    for i in range(2):
        y,x = map(int, input().split())
        print(find(y,x),end=' ')
def find(row, col):
    return arr[row][col]

main()

#8 같은 이름인지 확인하기
arr = [input() for _ in range(3)]
if arr[0] == arr[1] == arr[2]:
    print('YES')
else:
    print('NO')