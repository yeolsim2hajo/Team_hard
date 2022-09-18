def sorting(a):
    result = []
    for j in range(len(a)):
        result.append(a[j])
    for i in range(len(result)-1, 0, -1):
        for k in range(i):#5 0 1 2 3 4
            if result[k] > result[k+1]:
                result[k], result[k+1] = result[k+1], result[k]

    return result