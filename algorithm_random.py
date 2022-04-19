# 알고리즘 책에서 모의 평가할 문제 랜덤으로 반환하는 코드 작성

from random import sample

# chapter = ['greedy', 'simulation', 'dfs/bfs', 'sort', 'binary search', 'dynamic programming', 'shortest_path', 'graph']
# possible = [0.5, 0.5, 0.5, 0.5, 0.5, 0, 0, 0] # 알고리즘 학습 여부 (0.5는 쉬운 문제만 풀 수 있을 정도) # 당분간은 1 없이 0.5로만 할 예정
# number = [6, 14, 22, 26, 30, 36, 40, 45] # 각 챕터의 마지막 번호
# already = [7, 29, 27, 1, 8, 15] # 이미 푼 문제 번호 또는 아직 풀 수 없는 문제
# for i in range(0, 8): # already에 문제 넣어주기
#     start = number[i - 1] + 1 if i !=0 else 0
#     end = number[i]
#     if not possible[i]:
#         already += list(range(start, end + 1))
#     elif possible[i] == 0.5:
#         already += list(range(start + ((end - start) // 2), end+1))

# problems = [x for x in range(1,46) if x not in already] # 조건 만족하는 문제 번호만 넣은 리스트
# test = sample(problems, 2) # 샘플 추출
# for i in range(2): # 문제 번호와 챕터 출력
#     for j in range(8):
#         if test[i] <= number[j]:
#             print(f'#{i+1} {chapter[j]} : {test[i]}번')
#             break


# SWEA 문제 중 모의 평가할 문제를 랜덤으로 반환하는 코드 작성
problem_lst = ['벌꿀','보급로'] # 문제 목록
number = 2 # 풀 문제 수
print(*sample(problem_lst,number))

# import random
# print(random.sample(['원경', '장엽', '한', '희재'],4))