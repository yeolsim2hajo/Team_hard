def mergesort(arr):
    arr_len = len(arr)
    if arr_len <= 1:
        return arr
    mid = arr_len//2
    group1 = mergesort(arr[:mid])
    group2 = mergesort(arr[mid:])
    result = []

    while group1 and group2:
        if group1[0] < group2[0]:
            result.append(group1.pop(0))
        else:
            result.append(group2.pop(0))

    while group1:
        result.append(group1.pop(0))
    while group2:
        result.append(group2.pop(0))
    return result


arr = input().split()
arr = [int(i) for i in arr]

print(mergesort(arr))