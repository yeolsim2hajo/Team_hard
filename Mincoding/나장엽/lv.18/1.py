arr = list(input())

dat = [0]*71
# 아스키 코드를 써야 한다면...?
# 그냥 인덱스로만 푼다면..?
# 아스키 코드로 풀자. 65 66 67 68 69 ... 인덱스 70까지..?

# 아스키코드로 변환하고, 그 숫자에 해당하는 인덱스에 집어넣기.
# 몇 종류의 카드가 있는지 확인해야하기에...count 가 필요

for i in range(len(arr)):
    dat[ord(arr[i])] += 1

count = 0
for k in range(len(dat)):
    if dat[k] != 0:
        count +=1


print("{0}개".format(count))