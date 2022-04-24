# stack
def solution(plate, moves):
    stack=[0]
    point = 0
    while moves:
        m = moves.pop(0)
        for i in range(len(plate)):
            if plate[i][m-1]!=0:
                if stack[len(stack)-1] == plate[i][m-1]:
                    point+= plate[i][m-1]*2
                    plate[i][m-1] = 0
                    stack.pop()
                else:
                    stack.append(plate[i][m-1])
                plate[i][m-1] = 0
                break
            else:
                if  i==len(plate)-1 and plate[i][m-1]==0:
                    point-=1

    return point