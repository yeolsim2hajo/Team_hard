arr = [["C","D","A"],["B","M","Z"],["Q","P","O"]]

input = list(input())

dat = [0]*92

for row in range(3):
    for col in range(3):
        dat[ord(arr[row][col])] = 1

cnt = 0
#if문을 2번 주어야 한다.
#if ord(input[j]) == i:
#              cnt+=1
# 위의 코드만 쓰면, 4가 나온다 왜냐? ord(input[0~4]] == i로 했으니까.. 다 있다고 생각하고 출력함
# dat 리스트에 1 값을 가지고 있는 것으로만 제한해서 풀어야함!

for i in range(65, len(dat)):
    for j in range(len(input)):
        if dat[i] == 1:
            if ord(input[j]) == i:
                cnt+=1

print("{0}명".format(cnt))