a, b = map(int,input().split())
c = int(input())

if b+c < 60:
    print(a, (b+c))

elif a+(b+c)//60 >= 24:
    print(a+(b+c)//60-24, (b+c)% 60)
else:
    print(a+(b+c)//60, (b+c)% 60)

# 와!! 되었다!!!