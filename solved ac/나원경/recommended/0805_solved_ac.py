#1991 트리 순회
# N = int(input())
# tree = {}
# for _ in range(N):
#     key, *value = input().split()
#     tree[key] = value
# preorder = ''
# inorder = ''
# postorder = ''
# def dfs(arg=0, key='A'):
#     global preorder, inorder, postorder
#     preorder += key
#     for i in range(2):
#         alp = tree[key][i]
#         if alp != '.':
#             dfs(arg+1, alp)
#         if alp and key not in inorder:
#             inorder += key
#     postorder += key
# dfs()
# print(preorder, inorder, postorder, sep='\n')


# 걸리는 시간 같음
# N = int(input())
# tree = {}
# for _ in range(N):
#     key, *value = input().split()
#     tree[key] = value
# preorder = ''
# inorder = ''
# postorder = ''
# def dfs(arg=0, key='A'):
#     global preorder, inorder, postorder
#     preorder += key
#     for alp in tree[key]:
#         if alp != '.':
#             dfs(arg+1, alp)
#         if alp and key not in inorder:
#             inorder += key
#     postorder += key
# dfs()
# print(preorder, inorder, postorder, sep='\n')