for t in range(10):
    a = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    arr1 = [[0]*102 for _ in range(102)]
    for i in range(100):
        for j in range(100):
            arr1[i+1][j+1] = arr[i][j]
    b = 0
    for i in range(102):
        if arr1[i][100]==2:
            b += i
            break
    def get_p(ar, m, n):
        while(1):
            if ar[m-1][n]!=1 and ar[m+1][n]!=1:
                n -= 1
            elif ar[m+1][n]==1:
                m += 1
            else:
                m -= 1
            if n==1:
                return 1
        return m-1
    p = get_p(arr1, b, 100)
    print(p)
