a, b = map(int, input().split())

if a > b:
    result = a - b
else:
    result = b - a
    
if result % 2 == 0:
    print("짝사랑만")
else:
    print("고백한다")