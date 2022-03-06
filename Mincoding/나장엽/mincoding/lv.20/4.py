# 두칸씩 점프..


n = int(input())

def abc(level, n):
    if level == 3:
        print(n, end= ' ')
        return

    abc(level+ 1, n+2)
    print(n, end= ' ')

abc(0, n)