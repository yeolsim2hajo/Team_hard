# n = 3
# arr = ['a','b','c','d']
# path = ['']*n # 경로를 표시할 path 배열 선언
#
# def abc(level):
#     if level == 3:
#         for k in range(3):
#             print(path[k], end='')
#         print()
#         return
#
#     for i in range(4):
#         path[level] = arr[i]
#         abc(level+1)
#         path[level] = ''  # 덮어씌우거나, 이것처럼 초기화 하던가. 둘 중 하나.
# abc(0)

sign = ['A','B','C']
path = ['']*2

def abc(level):
    if level == 2:
        for k in range(2):
            print(path[k], end='')
        print()
        return
    for i in range(3):
        path[level] = sign[i]
        abc(level+1)
        
abc(0)