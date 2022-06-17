# 크기가 2^n * 2^n 배열을 z모양으로 탐색
# 왼위 오위 왼아 오아를 순서대로 방문
# n>1인 경우, 배열을 크기가 2^n-1 x 2^n-1로 4등분한 후에 재귀적으로 순서대로 방문한다.

#분할정복, 재귀
# 2^(n-1) * 2^(n-1)로 쪼개면, n=3인경우 1사분면은 0, 2사분면은 16, 3사분면은 32, 4사분면은 48부터 시작


import sys
input = sys.stdin.readline
N, r, c = map(int, input().split())

ans = 0

while N != 0:

	N -= 1

	# 1사분면
	if r < 2 ** N and c < 2 ** N:
		ans += ( 2 ** N ) * ( 2 ** N ) * 0

	# 2사분면
	elif r < 2 ** N and c >= 2 ** N: 
		ans += ( 2 ** N ) * ( 2 ** N ) * 1
		c -= ( 2 ** N )
        
	# 3사분면    
	elif r >= 2 ** N and c < 2 ** N: 
		ans += ( 2 ** N ) * ( 2 ** N ) * 2
		r -= ( 2 ** N )
        
	# 4사분면    
	else:
		ans += ( 2 ** N ) * ( 2 ** N ) * 3
		r -= ( 2 ** N )
		c -= ( 2 ** N )
    
print(ans)