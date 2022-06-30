T = int(input())

for i in range(T):
    stack = []
    a=input()
    for j in a:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack:
                stack.pop()
            else: 
                print("NO")
                break
    else: 
        if not stack: 
            print("YES")
        else: 
            print("NO")