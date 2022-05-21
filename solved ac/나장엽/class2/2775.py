N = int(input())
for _ in range(N):
    floor = int(input())
    people = int(input())
    result = [ x for x in range(1, people+1)]
    for i in range(floor):
        for k in range(1, people):
            result[k] += result[k-1]
    print(result[-1])


# 1,3 일때 1층의 3호에 살려면 , 0층의 1호부터 3호까지 사는 사람들의 수를 합한만큼 사람을 데려와 살아야한다.
# 0층의 1호에는 1명 2호 2명 3호 3명 4호 4명 5호 5명
# 1층의 1호 1명 2호 3명 3호 6명 4호 10명 
# 2층의 3호에서 살려면? 1층의 1, 2, 3호에 사는 사람들.