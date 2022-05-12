# 187번째 영화 제목이 66666 
N = int(input())
first = 666
while N != 0:
    if '666' in str(first): # 문자열에 666이 있으면 아래 코드 실행
        N = N - 1 
        if N == 0: # N = 0 일 때, -> N번째 값이라는 뜻.
            break 
    first = first + 1 # 666이 문자열 안에 없으면 계속 증가.
print(first)