arr = [[3,5,1],[4,2,6]]
input = list(map(int, input().split()))

# arr안에 input의 값이 있는지 검사하는 문제
# dat를 만들고, dat에 arr을 체크하고, dat의 인덱스 와 input을 비교해보자?

# max = 0
# for m in range(len(input)):
#     if max < input[m]:
#         max = input[m]
#     else:
#         max = max


# dat = [0] * max + 1
dat = [0] * 8
for row in range(2):
    for col in range(3):
        dat[arr[row][col]] = 1
# dat 0 1 1 1 1 1 1 0



for j in range(len(input)):
    if dat[input[j]] == 1:
        print("{0}번 합격".format(input[j]))
    else:
        print("{0}번 불합격".format(input[j]))