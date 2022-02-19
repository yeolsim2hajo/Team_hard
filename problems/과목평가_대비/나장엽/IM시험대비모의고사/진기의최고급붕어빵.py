#* 0초부터 붕어빵을 만듬, m 초의 시간을 들이면 k개의 붕어빵이 산출
#! 0초 이후에 손님들이 언제 도착하는지 주어지면, 모든 손님들에게 기다리는 시간없이 붕어빵을 제공할 수 있는지 판별하는 프로그램을 만들어라
#! 첫 번째 줄에 테스트 케이스 T
#! 각 테스트 케이스의 첫 번째 줄에는 세 자연수 n, m, k 가 주어진다 1~100
#! 두 번째 줄에는 n개의 정수가 공백으로 구분되어 주어짐
#! 각 정수는 각 사람이 언제 도착하는지를 초 단위로 나타낸다

        # 0초부터 만들기 시작. m 초의 시간을 들여 k의 붕어빵이 산출됨
        # n,m,k = 2, 2, 2 2초 당 2개 
        # 3, 4 -> 각 손님이 도착하는 시간.. 3초에 도착 4초에 도착  3초에 도착하면 붕어빵은 2개 , 4초에 도착하면 붕어빵은 4개..
        # 무조건 m초의 시간이 지나야 붕어빵이 나옴
        #* 붕어빵 제공 실패 조건?
        #* m 초전에 온 사람은 붕어빵 x  -> impossible
        #* 손님들이 만들어 놓은 붕어빵보다 많이와도 실패.
        
T = int(input())
def BubbleSort(arr): 
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
#만들어놓은 빵의 갯수는 그 (사람이 온 초//m)*k
#그 사람이 만들어 놓은 빵보다 초과하여 온 사람이면 impossible
def result(n,m,k,arr):
        arr = BubbleSort(arr)
        # 검사하기
        for i in range(n):
            TotalBread = (arr[i]//m)*k
            if TotalBread < i + 1: # 인덱스 i 를 이용하면 몇 번째 사람인지 알 수 있음, 인덱스는 0부터 시작이니 1을 더함
                return 0 # 만약에 만들어놓은 빵의 갯수보다 많이 왔다면 RETRUN 0
        return 1


for tc in range(1, T+1):
    n, m, k = map(int, input().split())
    customer = list(map(int, input().split()))
    
    customer = BubbleSort(customer)
    answer = result(n,m,k,customer)
    
    if answer == 1:
        print('#{0} "Possible"'.format(tc))
    else:
        print('#{0} "Impossible"'.format(tc))