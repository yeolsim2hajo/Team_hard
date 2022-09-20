import sys
input = sys.stdin.readline


def isAvailableStr(str):
    todo = list(str)

    while len(todo) >= 3:
        for i in range(2, len(todo), 2):
            if todo[i-2] == todo[i]:
                return False

        nextTodo = []
        for i in range(1, len(todo), 2):
            nextTodo.append(todo[i])

        todo = nextTodo

    return True


T = int(input())
for _ in range(T):
    curInput = str(input().rstrip())

    if isAvailableStr(curInput):
        print("YES")
    else:
        print("NO")