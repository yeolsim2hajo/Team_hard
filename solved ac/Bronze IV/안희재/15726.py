a, b, c = map(int,input().split())

print(max(int(a*b/c), int(a/b*c)))

# 아래도 되지만, 위 코드가 제일 나음
# A, B, C = map(int,input().split())
# if(A==min(A,B,C)):
#     print(int(A/B*C))
# elif(B==min(A,B,C)):
#     print(int(A/B*C))
# else:
#     print(int(A*B/C))

# 처음에 다른 방식으로 풀이했는데 계속 안되어서 문제를 욕했지만,
# 분명 되는 코드인데, 문제 설명이 미진했던것 또한 사실)
# 근데, 다시 생각해보면 레퍼런스 코드처럼 문제가 생길 여지가 없는 코드를 짜는것도
# 매우 중요한 것 같다