#17175 피보나치는 지겨웡~
n = int(input())
call = [1,1]
for i in range(2,n+1):
    call.append(call[i-1]+call[i-2]+1)
print(call[-1]%1000000007)

from collections import deque
n = int(input())
call = deque([1,1])
for i in range(2,n+1):
    call.append(call[-1]+call[-2]+1)
    call.popleft()
print(call[-1]%1000000007)

n = int(input())
pre = pre_pre = 1
for i in range(2,n+1):
    pre_pre, pre = pre, pre_pre + pre + 1
print(pre%1000000007)