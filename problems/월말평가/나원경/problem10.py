# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
from turtle import position


def get_final_position(N, mat, moves):
    
    # 캐릭터는 2차원 평면(N * N)에서 이동
    # 현재 2차원 평면은 0과 1로 이루어진 2차원 리스트(mat)로 주어짐
    # 캐릭터의 현재 위치는 숫자 1로 표현됨 (캐릭터는 단 하나)
    # 캐릭터는 0으로 표시된 모든 영역으로 이동 가능
    # 키 입력은 리스트 moves로 주어짐 (0: 위, 1: 아래, 2: 왼쪽, 3: 오른쪽)
    # 캐릭터의 최종 위치 (x, y 리스트 형태로 출력 - x,y는 2차원 평면에서의 행과 열)
    # 캐릭터가 범위 밖을 넘어간다면 None 반환
    
    x = 0
    y = 0 # 위치를 (x, y)로 놓을 것
    
    for lst in mat:
        if 1 not in lst: # 이차원 리스트의 원소(리스트)가 1을 포함하는지
            x += 1
        else:
            break

    for element in mat[x]: # 1을 포함하는 리스트에서 1의 위치 반환
        if element:
            break
        else:
            y += 1              
    
    for move in moves: # 방향에 따라 x, y 변화
        if move == 0:
            x -= 1
        elif move == 1:
            x += 1
        elif move == 2:
            y -= 1
        else:
            y += 1
    
    position_list = [x, y]
        
    for position in position_list: # 범위를 벗어났는지 확인
        if N-1 < position or position < 0:
            return None
    return position_list


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    N = 3
    mat = [
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ] 
    moves1 = [1, 1, 3]
    print(get_final_position(N, mat, moves1)) # [2, 1]
    
    moves2 = [1, 3, 3]
    print(get_final_position(N, mat, moves2)) # [1, 2]