#230216
def solution(board):
    rows, cols = len(board), len(board[0])
    answer = rows * cols
    visited = [board[i][:] for i in range(rows)]
    for row in range(rows):
        for col in range(cols):
            if board[row][col] == 1:
                answer -= 1
                for dr in range(-1, 2):
                    nr = row+dr
                    if 0 <= nr < rows:
                        for dc in range(-1, 2):
                            nc = col+dc
                            if 0 <= nc < cols and visited[nr][nc] == 0:
                                answer -= 1
                                visited[nr][nc] = 1

    return answer
'''
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.4MB)
테스트 3 〉	통과 (0.03ms, 10.2MB)
테스트 4 〉	통과 (0.02ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.04ms, 10.2MB)
테스트 7 〉	통과 (0.03ms, 10.1MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
테스트 11 〉	통과 (0.01ms, 10MB)
테스트 12 〉	통과 (0.01ms, 10.1MB)
테스트 13 〉	통과 (0.01ms, 10.1MB)
테스트 14 〉	통과 (0.07ms, 10.2MB)
'''

def solution(board):
    rows, cols = len(board), len(board[0])
    answer = rows * cols
    visited = [[False] * cols for _ in range(rows)]

    for row in range(rows):
        for col in range(cols):
            if board[row][col] == 1:
                for dr in range(-1, 2):
                    nr = row + dr
                    if 0 <= nr < rows:
                        for dc in range(-1, 2):
                            nc = col + dc
                            if 0 <= nc < cols and not visited[nr][nc]:
                                answer -= 1
                                visited[nr][nc] = True

    return answer
'''
테스트 1 〉	통과 (0.02ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.03ms, 10.2MB)
테스트 4 〉	통과 (0.02ms, 10.2MB)
테스트 5 〉	통과 (0.02ms, 10.3MB)
테스트 6 〉	통과 (0.02ms, 10.2MB)
테스트 7 〉	통과 (0.03ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.3MB)
테스트 9 〉	통과 (0.01ms, 10.3MB)
테스트 10 〉	통과 (0.01ms, 10.3MB)
테스트 11 〉	통과 (0.01ms, 10.3MB)
테스트 12 〉	통과 (0.01ms, 10.2MB)
테스트 13 〉	통과 (0.01ms, 10.2MB)
테스트 14 〉	통과 (0.07ms, 10.4MB)
'''

def solution(board):
    rows, cols = len(board), len(board[0])
    answer = rows * cols
    visited = [[False] * cols for _ in range(rows)]

    def find_safe_area():
        nonlocal answer
        if board[row][col] == 0:
            return
        for dr in range(-1, 2):
            nr = row + dr
            if 0 <= nr < rows:
                for dc in range(-1, 2):
                    nc = col + dc
                    if 0 <= nc < cols and not visited[nr][nc]:
                        answer -= 1
                        visited[nr][nc] = True

    for row in range(rows):
        for col in range(cols):
            find_safe_area()

    return answer
'''
테스트 1 〉	통과 (0.03ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.03ms, 10.2MB)
테스트 4 〉	통과 (0.02ms, 10.4MB)
테스트 5 〉	통과 (0.02ms, 10.3MB)
테스트 6 〉	통과 (0.03ms, 10.3MB)
테스트 7 〉	통과 (0.04ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.3MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
테스트 11 〉	통과 (0.01ms, 10.4MB)
테스트 12 〉	통과 (0.01ms, 10.2MB)
테스트 13 〉	통과 (0.02ms, 10.2MB)
테스트 14 〉	통과 (0.07ms, 10.2MB)
'''

def solution(board):
    rows, cols = len(board), len(board[0])
    answer = rows * cols
    visited = [[False] * cols for _ in range(rows)]

    for row in range(rows):
        for col in range(cols):
            if board[row][col] == 0:
                continue
            for dr in range(-1, 2):
                nr = row + dr
                if 0 <= nr < rows:
                    for dc in range(-1, 2):
                        nc = col + dc
                        if 0 <= nc < cols and not visited[nr][nc]:
                            answer -= 1
                            visited[nr][nc] = True

    return answer
'''
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.03ms, 10.4MB)
테스트 4 〉	통과 (0.02ms, 10.2MB)
테스트 5 〉	통과 (0.02ms, 10.1MB)
테스트 6 〉	통과 (0.02ms, 10.3MB)
테스트 7 〉	통과 (0.04ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.3MB)
테스트 10 〉	통과 (0.01ms, 10.3MB)
테스트 11 〉	통과 (0.01ms, 10.3MB)
테스트 12 〉	통과 (0.01ms, 10.2MB)
테스트 13 〉	통과 (0.01ms, 10.4MB)
테스트 14 〉	통과 (0.07ms, 10.3MB)
'''
def solution(board):
    n = len(board)
    if n == 1:
        return 1 - board[0][0]
    answer = n * n
    visited = [[False] * n for _ in range(n)]

    def find_range(num):
        if num == 0:
            return 0, 2
        elif num == n - 1:
            return -1, 1
        else:
            return -1, 2

    for row in range(n):
        for col in range(n):
            if board[row][col] == 0:
                continue
            start_r, end_r = find_range(row)
            for dr in range(start_r, end_r):
                nr = row + dr
                start_c, end_c = find_range(col)
                if 0 <= nr < n:
                    for dc in range(start_c, end_c):
                        nc = col + dc
                        if 0 <= nc < n and not visited[nr][nc]:
                            answer -= 1
                            visited[nr][nc] = True

    return answer
'''
테스트 1 〉	통과 (0.03ms, 10.1MB)
테스트 2 〉	통과 (0.01ms, 10.1MB)
테스트 3 〉	통과 (0.04ms, 10.2MB)
테스트 4 〉	통과 (0.02ms, 10.2MB)
테스트 5 〉	통과 (0.02ms, 10.1MB)
테스트 6 〉	통과 (0.03ms, 10.4MB)
테스트 7 〉	통과 (0.06ms, 10.2MB)
테스트 8 〉	통과 (0.00ms, 10.2MB)
테스트 9 〉	통과 (0.00ms, 10.3MB)
테스트 10 〉	통과 (0.01ms, 10.3MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)
테스트 12 〉	통과 (0.01ms, 10.2MB)
테스트 13 〉	통과 (0.02ms, 10.2MB)
테스트 14 〉	통과 (0.09ms, 10.3MB)
'''



def solution(board):
    n = len(board)
    if n == 1:
        return 1 - board[0][0]
    answer = n * n
    visited = [[False] * n for _ in range(n)]

    def find_range(num):
        start, end = -1, 2
        if num == 0:
            start = 0
        elif num == n - 1:
            end = 1
        return start, end

    for row in range(n):
        for col in range(n):
            if board[row][col] == 0:
                continue
            start_r, end_r = find_range(row)
            for dr in range(start_r, end_r):
                nr = row + dr
                start_c, end_c = find_range(col)
                for dc in range(start_c, end_c):
                    nc = col + dc
                    if not visited[nr][nc]:
                        answer -= 1
                        visited[nr][nc] = True

    return answer
'''
테스트 1 〉	통과 (0.03ms, 10.4MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.03ms, 10.3MB)
테스트 4 〉	통과 (0.03ms, 10.4MB)
테스트 5 〉	통과 (0.02ms, 10.1MB)
테스트 6 〉	통과 (0.02ms, 10.2MB)
테스트 7 〉	통과 (0.03ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.00ms, 10.1MB)
테스트 10 〉	통과 (0.01ms, 10.1MB)
테스트 11 〉	통과 (0.01ms, 10.4MB)
테스트 12 〉	통과 (0.01ms, 10.3MB)
테스트 13 〉	통과 (0.01ms, 10.1MB)
테스트 14 〉	통과 (0.07ms, 10.3MB)
'''

def solution(board):
    n = len(board)
    answer = n * n
    visited = [[False] * n for _ in range(n)]

    for row in range(n):
        for col in range(n):
            if board[row][col] == 0:
                continue
            for dr in range(-1, 2):
                nr = row + dr
                if 0 <= nr < n:
                    for dc in range(-1, 2):
                        nc = col + dc
                        if 0 <= nc < n and not visited[nr][nc]:
                            answer -= 1
                            visited[nr][nc] = True

    return answer
'''
테스트 1 〉	통과 (0.04ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.03ms, 10.1MB)
테스트 4 〉	통과 (0.02ms, 10.1MB)
테스트 5 〉	통과 (0.02ms, 10.2MB)
테스트 6 〉	통과 (0.02ms, 10.2MB)
테스트 7 〉	통과 (0.03ms, 10.1MB)
테스트 8 〉	통과 (0.00ms, 10.1MB)
테스트 9 〉	통과 (0.01ms, 10.1MB)
테스트 10 〉	통과 (0.01ms, 10.3MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)
테스트 12 〉	통과 (0.01ms, 10.2MB)
테스트 13 〉	통과 (0.01ms, 10.4MB)
테스트 14 〉	통과 (0.07ms, 10.2MB)
'''