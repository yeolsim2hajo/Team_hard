import sys
input = sys.stdin.readline
#sys.stdin.readline은 매 줄의 마지막에 있는 개행 문자까지 같이 반환합니다. 
#따라서 문자열을 저장하는 경우 rstrip()을 해줘야 isdigit이 정수를 정수라고 판단할 수 있습니다. 
# 마찬가지로 이 문자열을 그대로 print로 출력할 경우 저장된 개행 문자에 
# print가 기본적으로 출력하는 개행 문자가 겹쳐 개행이 두 번 일어나게 됩니다.
n, m = map(int, input().split())

poketmon = []
pok_index = dict()

for i in range(n):
    pkm = input().rstrip()
    poketmon.append(pkm)
    pok_index[pkm] = i + 1 # 인덱싱 해버리기

for _ in range(m):
    problem = input().rstrip()

    if problem.isdigit():
        print(poketmon[int(problem)-1])

    else:
        print(pok_index[problem])