arr=[7,4,8,1,5,3,9,6]  # Min heap
heap=[0]*50
hindex=1  # 힙 이라는 1차배열의 인덱스 역활

def insert(value):
    global heap,hindex
    heap[hindex]=value
    now=hindex
    hindex+=1

    while 1:
        parents=now//2
        if parents==0: break
        if heap[parents]<=heap[now]: break
        heap[parents],heap[now]=heap[now],heap[parents]
        now=parents 

def top():
    global heap
    return heap[1] # 1번 인덱스의값 (루트노드 리턴)

def pop():
    global heap,hindex
    heap[1]=heap[hindex-1] # 맨 뒤에 있는 아이를 루트로 일단 옮기기
    heap[hindex]=0
    hindex-=1

    now=1
    while 1:
        son=now*2 # 왼쪽자식
        rson=son+1 # 오른쪽 자식

        if rson<=hindex and heap[son]>heap[rson]: son=rson
        if son>hindex or heap[now]<heap[son]: break
        heap[now],heap[son]=heap[son],heap[now]
        now=son

for i in range(len(arr)):
    insert(arr[i])   # 트리의 형태로 저장 (1차배열)

for i in range(len(arr)):
    print(top(),end=' ') # 루트노드 출력
    pop() # 맨뒤에 있는아이를 1번 인덱스로 올리고 자식들이랑 비교