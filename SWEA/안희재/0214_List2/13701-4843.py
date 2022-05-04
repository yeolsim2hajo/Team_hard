# 아 이거 미는건가?
# 빈 bucket 만들어서 밀면 될듯?
# 길이가 10개인 리스트면,
# 1. 정렬(내림차순)
# 2. arr[0:5], arr[5:10] 나눠서
# 3. arr[0:5]는 차례대로 1,3,5,7,9 버켓에 넣고
# 4. arr[5:10] 차례대로 0,2,4,6,8에 넣는 거지

T = int(input())
for i in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    
    # 오름차순 정렬
    arr.sort(reverse=True)
    bucket = [0] * N
    # 큰수5개, 작은수5개 나누기
    big_arr = arr[0:N//2]
    small_arr = arr[N-1:N-(N//2)-1:-1]

    # 큰거부터 채워놓기 - 0,2,4,6,8
    for j in range(N//2): # 0,1,2,3,4
        bucket[2*j] = big_arr[j]

    # 작은거 채워놓기 = 1,3,5,7,9
    for j in range(N//2): # 0,1,2,3,4
        bucket[2*j+1] = small_arr[j]

    answer = bucket[0:10] # 10개까지 출력이래요...ㅜ

    print(f'#{i}', ' '.join(map(str,answer)))