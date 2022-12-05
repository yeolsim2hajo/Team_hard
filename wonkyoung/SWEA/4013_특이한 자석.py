#221205
def rotate(index, direction, left=True, right=True):
    circle = magnetic[index]
    if left:
        left = index != 1 and circle[6] != magnetic[index-1][2]
    if right:
        right = index != 4 and circle[2] != magnetic[index+1][6]

    if direction == 1:
        circle.insert(0, circle.pop())
    else:
        circle = circle[1:] + circle[0:1]
    magnetic[index] = circle

    if left:
        rotate(index-1, -direction, True, False)
    if right:
        rotate(index+1, -direction, False, True)

def get_score():
    answer = 0
    for i in range(1, 5):
        answer += 0 if magnetic[i][0] == '0' else 2**(i-1)
    return answer

T = int(input())
for tc in range(1, T+1):
    K = int(input())
    magnetic = [[]]
    magnetic.extend([input().split() for _ in range(4)])

    for _ in range(K):
        index, direction = map(int, input().split())
        rotate(index, direction)
    score = get_score()
    print(f'#{tc} {score}')

