#2168 타일 위의 대각선
# 틀림
# width, height = map(int, input().split())
# if width == height:
#     answer = width
# else:
#     answer = height//width * width if height%width == 0 else (height//width+1) * width
# print(answer)

# 틀림
# width, height = map(int, input().split())
# if width == height:
#     answer = width
# else:
#     if width > height:
#         width, height = height, width
#     answer = height//width * width if height%width == 0 else (height//width + 1) * width
# print(answer)


#20115 에너지 드링크
# N = int(input())
# drink = list(map(int, input().split()))
# drink.sort()
# print(round(drink[-1] + sum(drink[:N-1])/2, 5))

# 다른 방법
# N = int(input())
# drink = list(map(int, input().split()))
# drink.sort()
# print(round(drink[-1]/2 + sum(drink)/2, 5))