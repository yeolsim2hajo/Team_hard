# 능숙함의 차이
# arr = [1,5,4,2,9,7]
# N = int(input())
# A, B = map(int,input().split())
# for _ in range(N):
#     for i in range(A, B+1):
#         arr[i] += 1
# print(arr)


#2
# arr = input().split()
# check = {}
# for alp in arr:
#     if check.get(alp):
#         check[alp] += 1
#     else:
#         check[alp] = 1
# max_val = 0
# for key, value in check.items():
#     if value > max_val:
#         max_val = value
#         max_key = key
# print(max_key, max_val)

#3
arr = 'ASADADAS'
def dfs(idx):
    print(arr[idx], end='')
    if idx < len(arr) - 1:
        dfs(idx+1)
    print(arr[idx], end='')
dfs(0)