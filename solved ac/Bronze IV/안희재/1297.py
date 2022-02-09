import math

a, b, c = map(int,input().split())

height = math.floor(((a**2/(b**2+c**2)) ** 0.5) * b)
width = math.floor(((a**2 / (b**2+c**2)) ** 0.5) * c)

print(height, width)