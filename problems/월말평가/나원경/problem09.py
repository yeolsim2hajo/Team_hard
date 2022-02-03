# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def is_position_safe(N, M, position):
    
    # 캐릭터의 현재 위치는 튜플(x, y) 형태로 주어짐
    # x,y는 2차원 평면에서의 행과 열 (0 <= x < 100, 0 <= y < 100)
    # 최대 범위는 숫자 N으로 주어짐 (0 <= N < 100)
    # 키 입력은 숫자 M으로 주어짐 (0: 위, 1: 아래, 2: 왼쪽, 3: 오른쪽)
    # 키 입력의 결과가 최대 범위를 벗어나면 False, 아니면 True 반환
    position_list = list(position) # 요소를 변화시킬 수 있도록 리스트로 변환

    if M == 0:
        position_list[0] -= 1
    elif M == 1:
        position_list[0] += 1
    elif M == 2:
        position_list[1] -= 1
    else:
        position_list[1] += 1

    for i in position_list:
        if 0 <= position_list[i] <= N-1:
            continue
        else:
            return False
    return True


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    print(is_position_safe(3, 1, (0, 0))) # True
    print(is_position_safe(3, 0, (0, 0))) # False
