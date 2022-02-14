T = [list(input()) for _ in range(3)]


def find_M(T):
    for i in range(3):
        for j in T[i]:
            if j == 'M':
                return 'M이 존재합니다'
                
    else:
        return 'M이 존재하지 않습니다'

print(find_M(T))

# 함수로 쓰니까 바로 풀리네.. 함수 없이 하면,
# 계속 답 중복 출력.. break어디다 써야 되나.. 이러고 있었을 듯