def quicksort(arr):
    arr_len = len(arr)
    if arr_len <= 1:
        return arr
    value = arr.pop(arr_len // 2)
    group1 = []
    group2 = []

    for i in range(arr_len-1):
        if arr[i] < value:
            group1.append(arr[i])
        else:
            group2.append(arr[i])
    return quicksort(group1) + [value] + quicksort(group2)

arr = input().split()
arr = [int(i) for i in arr]

print(quicksort(arr))
