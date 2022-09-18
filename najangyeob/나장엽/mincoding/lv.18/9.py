arr = [[1,3,3,5,1],[3,6,2,4,2],[1,9,2,6,5]]

n = int(input())

# 배열 중에서 입력받은 n의 숫자만큼 존재하는 숫자가 무엇인지 모두 찾으라는 문제
# dat 사용해서 누적합 구하기?
# dat의 인덱스를 출력?

# 3x5배열이니.. 16개 필요
dat = [0]*16

# dat에 arr 배열에 등장하는 수 만큼 1씩 증가 시켜서 저장 
for row in range(3):
    for col in range(5):
        dat[arr[row][col]] += 1


# 입력받은 n과 같은 등장횟수를 가지는 수를 모두 출력하기
# n과 value값을 비교하고, index를 출력하면 될듯..?

for i in range(len(dat)):
    # n과 dat의 value에 해당하는 값이 같으면 아래 코드문 실행.
    if n == dat[i]:
        print(i, end= ' ')