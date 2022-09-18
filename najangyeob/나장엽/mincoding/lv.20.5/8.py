# 두 배열 merge 하기

from multiprocessing.dummy import Array


arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
result = []
i1 = 0
i2 = 0
# 두개의 배열을 합쳐 한개의 result 배열에 채우려 한다.
# 1 가장 첫 번째 숫자 중 작은 숫자를 result에 넣고 화살표를 한칸 옮긴다.

while True:
    if arr1[i1] <= arr2[i2]:
        result.append(arr1[i1])
        i1 += 1
    else:
        result.append(arr2[i2])
        i2 += 1
    
    if i1 == 4:
        result.extend(arr2[i2:])
        break
    if i2 == 4:
        result.extend(arr1[i1:])
        break
    
print(*result)
        