# class 3++ 1676 팩토리얼 0의 개수

n = int(input())
rst2, rst5 = 0, 0

def abc(a):
    global rst2, rst5
    while a > 1:
        if a%5 == 0:
            a = a//5
            rst5 += 1
        elif a%2 == 0:
            a = a//2
            rst2 += 1
        else:
            break

for i in range(1, n):
    abc(i+1)

print(min(rst2, rst5))