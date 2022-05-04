for i in range(100):
    for j in range(100):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]