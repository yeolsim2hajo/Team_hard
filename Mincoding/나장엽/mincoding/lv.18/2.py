# id는 1 ~ 65535 범위를 가진다
# 누가 가장 성실하게 출근했느냐?
# dat를 이용하여 풀기 / 입력값 없음

record = [[65000, 35, 42, 70],[70,35,65000,1300],[65000, 30000, 38, 42]]

dat = [0]*65001

#dat 배열에 1을 체크 
for row in range(3):
    for col in range(4):
        dat[record[row][col]] += 1

# max값을 찾는게 아닌, 누가 가장 많이 출근했느냐를 찾는 문제이므로 max를 이용하고, index를 저장할 변수 선언        
max = 0
index = 0

# max값을 찾고, index에 i를 저장 
for i in range(len(dat)):
    max = dat[0]
    if max < dat[i]:
        max = dat[i]
        index = i
    else:
        max = max
    
print(index)