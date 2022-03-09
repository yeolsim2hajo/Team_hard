#lv 3.5

#9 엘레베이터 타고 내려가자
for i in range(9,5,-1):
    print(i, i-3)

#10 징검다리
number = int(input())
for i in range(number):
    print(2*i+1, end=' ')

#11 시작부터 종료까지
arr=['시작','12345','종료']
for j in range(3):
    print(arr[j])

#12 와플사과 샌드위치 출력
number = int(input())
for _ in range(number):
    print('##\n@@')

#13 순서대로 Go!
for i in range(1,6):
    print(f'{i}번go!!')

#14 아이디와 비밀번호 입력받기
input_id, input_pw = map(int, input().split())
if input_id != 1111:
    print('아이디가 틀렸습니다')
elif input_pw != 2222:
    print('비밀번호가 틀렸습니다')
else:
    print('로그인성공')

#15 끝은 항상 0이지
number = int(input())
for i in range(number,-1,-1):
    print(i,end='')