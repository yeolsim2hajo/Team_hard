#2630 색종이 만들기
N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
cnt = [0,0]
def split_paper(size, arr):
    if size == 1:
        return arr[0][0]
    half = size//2
    path = []
    for end in (half, size):
        for j in (0, half):
            half_arr = [arr[i][j:j+half] for i in range(end-half, end)]
            path.append(split_paper(half, half_arr))
    for i in range(3):
        element = path[i]
        if element == -1 or element != path[i+1]:
            for j in path:
                if j != -1:
                    cnt[j] += 1
            return -1
    return path[0]

result = split_paper(N, paper)

if result != -1:
    cnt[result] += 1
print(*cnt, sep='\n')



'''
8
1 1 0 0 0 0 1 1
1 1 0 0 0 0 1 1
0 0 0 0 1 1 0 0
0 0 0 0 1 1 0 0
1 0 0 0 1 1 1 1
0 1 0 0 1 1 1 1
0 0 1 1 1 1 1 1
0 0 1 1 1 1 1 1

2
1 1 
1 1 

4
1 1 0 0 
1 1 0 0 
0 0 0 0 
0 0 0 0 
'''
