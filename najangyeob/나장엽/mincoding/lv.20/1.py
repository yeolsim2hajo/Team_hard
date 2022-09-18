# 무한 재귀 막기
# 아래와 같이 재귀 함수를 구현해라

def bbq(x):
    if x == 3:
        return
    bbq(x+1)


bbq(0)