# # lv 15
# # 2차배열 정렬하기
# arr = [['D','A','T','A','W'],['B','B','Q','K']]
# N = int(input())
# if N % 2:
#     arr[0].sort()
# else:
#     arr[1].sort()
# for i in range(2):
#     print(*arr[i],sep='')
#
#
# # 일부 문장만 오려내기
# arr = [list(map(str,x)) for x in ['POTIO','ABCDE','YOURE']]
# a,b = map(int, input().split())
# for i in range(3):
#     for j in range(a,b+1):
#         print(arr[i][j],end='')

# 두 문장 중 같은 문장의 갯수 세기
# arr = [input() for _ in range(2)]
# max_len = max(len(arr[0]),len(arr[1]))
# cnt = 0
# try:
#     for i in range(max_len):
#         if arr[0][i] == arr[1][i]:
#             cnt += 1
# except: pass
# finally:
#     print(max_len - cnt)

# 이중 while로 배열에 값 채우기 - 다시
# munja = input()
# row = 3
# col = 0
# cnt = 1
# arr = [['']*3 for _ in range(3)]
# while row > 0:
#     row -= 1
#     col = 0
#     while col <= 2-row:
#         arr[row][col] = chr(ord(munja) + cnt)
#         cnt += 1
#         col += 1
#         print(*arr[row])
# for i in range(3):
#     print(*arr[i],sep='')


