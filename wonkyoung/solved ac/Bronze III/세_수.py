#230307
# arr = sorted(map(int, input().split()))
# print(arr[1])

#
arr = list(map(int, input().split()))
arr.sort()
print(arr[1])

#
def find_second():
    arr = list(map(int, input().split()))
    check = [0] * 3
    for i in range(2):
        if arr[i] < arr[i+1]:
            check[i+1] += 1
        else:
            check[i] += 1
    if arr[0] < arr[-1]:
        check[-1] += 1
    else:
        check[0] += 1
    for i in range(3):
        if check[i] == 1:
            return arr[i]
print(find_second())
