#230202
def solution(operations):
    from heapq import heappush, heappop, heapify
    q, q2, = [], []
    for operation in operations:
        command, num = operation.split()
        num = int(num)
        if command == 'I':
            heappush(q, num)
            heappush(q2, -num)
        elif num == 1:
            if q2:
                max_val = heappop(q2)
                q.remove(-max_val)
                heapify(q)
        elif q:
            min_val = heappop(q)
            q2.remove(-min_val)
            heapify(q2)
    if not q:
        return [0, 0]
    max_val = heappop(q2)
    min_val = heappop(q)
    return [-max_val, min_val]