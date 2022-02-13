d, h, w = map(int, input().split())

# 피타고라스의 정리 = c^2 =a^2 + b^2
# 비율이 주어짐 h, w에 대해, a:b = h:w
# 내항의 곱 = 외항의 곱 ah = bw

# a와 b의 값을 구해야 함
# a = (w*b)/h
# a^2 = ((w*b)/h)^2 = (w/h)^2*b^2
# 정리 
# c^2 = (w/h)^2*b^2 + b^2
# b^2 = c^2/(1+(w/h)^2)
# b = (c^2/(1+(w/h)^2))^0.5

b = (d**2/(1+(w/h)**2))**0.5
a = (w*b)/h
print(int(b),int(a))