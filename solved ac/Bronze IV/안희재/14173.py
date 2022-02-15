x1, y1, x2, y2 = map(int,input().split())
z1, w1, z2, w2 = map(int,input().split())

x = max(x2,z2) - min(x1,z1)
y = max(y2,w2) - min (y1,w1)

print(max(x,y)**2)

# -----------------------
# 첫 코드 - 실패
# if abs(x2-z1) > abs(w2-y1):
#     print(abs(x2-z1)**2)
# else:
#     print(abs(w2-y1)**2)
# -7 ** 2 => -49 나온다.. 오우쉣;;
# 또한, 이 경우는 첫 줄 사각형이 두번째 사각형보다 크다는 것을 가정한 코드...
# 또한, 살짝 겹칠 경우도 생각해 줘야 함
# 간단한 문제는 아니었네. 살짝 생각해야 함