#230126
a, b = map(int, input().strip().split(' '))
for _ in range(b):
    print('*' * a)
'''
테스트 1 〉	통과 (11.90ms, 7.36MB)
테스트 2 〉	통과 (14.02ms, 7.43MB)
테스트 3 〉	통과 (11.26ms, 7.45MB)
테스트 4 〉	통과 (11.43ms, 7.5MB)
테스트 5 〉	통과 (11.53ms, 7.43MB)
테스트 6 〉	통과 (17.11ms, 7.54MB)
테스트 7 〉	통과 (18.84ms, 7.53MB)
테스트 8 〉	통과 (15.86ms, 7.6MB)
테스트 9 〉	통과 (14.19ms, 7.39MB)
테스트 10 〉	통과 (11.77ms, 7.38MB)
테스트 11 〉	통과 (11.52ms, 7.64MB)
'''
a, b = map(int, input().strip().split(' '))
for _ in range(b):
    for _ in range(a):
        print('*', end='')
    print()
'''
테스트 1 〉	통과 (11.80ms, 7.44MB)
테스트 2 〉	통과 (10.74ms, 7.37MB)
테스트 3 〉	통과 (12.22ms, 7.52MB)
테스트 4 〉	통과 (11.10ms, 7.58MB)
테스트 5 〉	통과 (16.44ms, 7.51MB)
테스트 6 〉	통과 (18.34ms, 7.63MB)
테스트 7 〉	통과 (17.26ms, 7.37MB)
테스트 8 〉	통과 (17.04ms, 7.5MB)
테스트 9 〉	통과 (31.54ms, 7.52MB)
테스트 10 〉	통과 (13.81ms, 7.63MB)
테스트 11 〉	통과 (21.24ms, 7.75MB)
'''
a, b = map(int, input().strip().split(' '))
stars = '*' * a
for _ in range(b):
    print(stars)
'''
테스트 1 〉	통과 (13.87ms, 7.53MB)
테스트 2 〉	통과 (10.63ms, 7.45MB)
테스트 3 〉	통과 (11.18ms, 7.55MB)
테스트 4 〉	통과 (11.12ms, 7.44MB)
테스트 5 〉	통과 (11.34ms, 7.56MB)
테스트 6 〉	통과 (10.92ms, 7.36MB)
테스트 7 〉	통과 (10.86ms, 7.51MB)
테스트 8 〉	통과 (11.67ms, 7.51MB)
테스트 9 〉	통과 (14.22ms, 7.35MB)
테스트 10 〉	통과 (10.74ms, 7.37MB)
테스트 11 〉	통과 (11.01ms, 7.53MB)
'''
a, b = map(int, input().strip().split(' '))
stars = ''
for _ in range(a):
    stars += '*'
for _ in range(b):
    print(stars)
'''
테스트 1 〉	통과 (12.68ms, 7.58MB)
테스트 2 〉	통과 (10.85ms, 7.36MB)
테스트 3 〉	통과 (16.04ms, 7.51MB)
테스트 4 〉	통과 (12.14ms, 7.49MB)
테스트 5 〉	통과 (11.83ms, 7.41MB)
테스트 6 〉	통과 (10.98ms, 7.38MB)
테스트 7 〉	통과 (14.10ms, 7.53MB)
테스트 8 〉	통과 (13.55ms, 7.42MB)
테스트 9 〉	통과 (11.82ms, 7.41MB)
테스트 10 〉	통과 (11.12ms, 7.42MB)
테스트 11 〉	통과 (12.03ms, 7.37MB)
'''

