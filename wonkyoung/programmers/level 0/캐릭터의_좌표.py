#230131
def solution(keyinput, board):
    now = [0, 0]
    move = {
        'up' : [0, 1],
        'down' : [0,-1],
        'left' : [-1, 0],
        'right' : [1, 0]
    }
    half = [board[0]//2, board[1]//2]
    for direction in keyinput:
        delta = move[direction]
        for i in range(2):
            if -half[i] <= now[i] + delta[i] <= half[i]:
                now[i] += delta[i]
    return now
'''
테스트 1 〉	통과 (0.02ms, 10.3MB)
테스트 2 〉	통과 (0.00ms, 10.2MB)
테스트 3 〉	통과 (0.02ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.3MB)
테스트 7 〉	통과 (0.04ms, 10.3MB)
테스트 8 〉	통과 (0.03ms, 10.1MB)
테스트 9 〉	통과 (0.02ms, 10.3MB)
테스트 10 〉	통과 (0.01ms, 10.3MB)
테스트 11 〉	통과 (0.01ms, 10.1MB)
'''

def solution(keyinput, board):
    now = [0, 0]
    move = {
        'up' : [0, 1],
        'down' : [0,-1],
        'left' : [-1, 0],
        'right' : [1, 0]
    }
    half = list(map(lambda x: x//2, board))
    for direction in keyinput:
        delta = move[direction]
        for i in range(2):
            if -half[i] <= now[i] + delta[i] <= half[i]:
                now[i] += delta[i]
    return now
'''
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.00ms, 10.3MB)
테스트 3 〉	통과 (0.03ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.04ms, 10.2MB)
테스트 8 〉	통과 (0.04ms, 10.3MB)
테스트 9 〉	통과 (0.05ms, 10.3MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
테스트 11 〉	통과 (0.01ms, 10.3MB)
'''

def solution(keyinput, board):
    now = [0, 0]
    move = {
        'up' : [0, 1],
        'down' : [0,-1],
        'left' : [-1, 0],
        'right' : [1, 0]
    }
    plus = lambda x, y: x + y
    half = [board[0]//2, board[1]//2]
    for direction in keyinput:
        delta = move[direction]
        now = list(map(plus, delta, now))
        for i in range(2):
            if not (-half[i] <= now[i] <= half[i]):
                now[i] -= delta[i]
    return now
'''
테스트 1 〉	통과 (0.03ms, 10.2MB)
테스트 2 〉	통과 (0.00ms, 10.2MB)
테스트 3 〉	통과 (0.03ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.3MB)
테스트 6 〉	통과 (0.01ms, 10.3MB)
테스트 7 〉	통과 (0.05ms, 10.4MB)
테스트 8 〉	통과 (0.04ms, 10.3MB)
테스트 9 〉	통과 (0.03ms, 10.4MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)
'''