a, b, c = map(int,input().split())
d = int(input())

if c + d < 60:
    print(a, b, c+d)
elif b+(c+d)//60 < 60:
    print(a, b+(c+d)//60, b+(c+d)%60)
elif a + b + (c+d)//60 >= 24:
    print(a+b+(c+d)//60)

# ?????????????? 오늘은 무리데스,,