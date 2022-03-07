def bbq(num):
    if num == level:
        return

    for i in range(branch):
        bbq(num+1)

level = int(input())
branch = int(input())