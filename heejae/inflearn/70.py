# 행렬끼리 곱할 수 있으려면, 왼쪽 행렬의 열과 오른쪽 행렬의 행이 같아야 함
# 입력
# a = ([1, 2],
#      [2, 4])
# b = ([1, 0],
#      [0, 3])

# 출력
# ([1,6], [2,12])
# ------------------------
a = ([1, 2],
    [2, 4])
b = ([1, 0],
    [0, 3])

result = [[0]*len(a) for _ in range(len(b[0]))] # 2*3,3*2이면 확인은 3,3이 같은지 / 결과는 2*2로!
if len(a[0]) != len(b):
    print(-1)
else:
    for i in range(len(b[0])):
        for j in range(len(a)):
            for k in range(len(b)):
                result[i][j] += a[i][k]*b[k][j]
                # 어우;; 여기 짜는게 은근히 아직도 힘드네;;; 손코딩하면서 계속 익히자!
print(result)