# 한 문장을 입력받고 글자수를 구해라
# 재귀 호출을 이용해 다음과 같이 출력
# abcde 를 입력받았다면 5글자이므로 4 3 2 1 2 3 4 5

chr = list(input())
n = len(chr)
# def abc(level):
#     global cnt, chr
#     if level == len(chr):
#         return
#
#     cnt += 1
#     abc(level+1)
#     print(cnt, end=' ')
#     cnt -= 1
#
# abc(0)



def abc2(level):
    global n
    print(level, end=' ')
    if level == 1:
        return

    abc2(level-1)
    print(level, end = ' ')
abc2(n)