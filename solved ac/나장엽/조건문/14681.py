# 사분면 고르기
# 1사분면 x, y 좌표값이 양수

# 2사분면 x의 좌표값이 음수 y 좌표값이 양수

# 3사분면 x, y 좌표값이 음수

# 4사분면 x 좌표값이 양수 y 좌표값이 음수

# 첫 줄에는 정수 x가 주어진다.
# 다음 줄에는 정수 y가 주어진다

x = int(input())
y = int(input())

if x > 0 and y > 0 :
    print(1)
elif x < 0 and y > 0 :
    print(2)
elif x < 0 and y < 0 : 
    print(3)
else:
    print(4)