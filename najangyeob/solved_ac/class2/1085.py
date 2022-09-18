X, Y, W, H = map(int, input().split())
start_x, start_y = 0, 0


# 경계선에서 빼기만 하면 됨.
# X- start_x, Y - start_y, W - X , H - Y 를 Min 리스트에 넣어두고 최소값 찾으면 해결.
Min = []

Min.append(X - start_x)
Min.append(Y - start_y)
Min.append(W - X)
Min.append(H - Y)


print(min(Min))