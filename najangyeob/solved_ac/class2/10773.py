
N = int(input())
stack = []

for i in range(N):
    number = int(input())

    if number == 0:
        stack.pop()

    else:
        stack.append(number)

print(sum(stack))