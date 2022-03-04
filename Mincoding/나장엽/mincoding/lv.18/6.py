# 3x5 배열의 알파벳을 정렬해서..한줄로 출력!
# 아스키와 dat를 사용하면 될듯? 아닌거같은디... dat[65]는 4값을 가지고 있음... 출력 시 이를 이용할 수 있나?


arr = [["A","B","C"],["A","G","H"],["H","I","J"],["K","A","B"],["A","B","C"]]

dat=[0]*92

for row in range(5):
    for col in range(3):
        dat[ord(arr[row][col])] += 1


for i in range(len(dat)):
    if dat[i] >= 1:
        print(chr(i)*dat[i], end='')