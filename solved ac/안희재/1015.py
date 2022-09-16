import sys
import math
 
A_size = int(sys.stdin.readline())
A = sys.stdin.readline().replace("\n", "").split(' ')
A = [int(i) for i in A]
 
# A를 오름차순으로 정렬하여 작은 숫자부터 순서대로 정리된 새로운 list를 할당 
sorted_A = [i for i in A]
sorted_A.sort()
 
P = []
# A의 각 숫자들에 대해 sorted_A에서의 index를 찾아 몇번째로 작은 숫자인지 P 수열에 새롭게 append함.
for i in A:
    P.append(sorted_A.index(i))
    # 이미 할당한 숫자는 sorted_A에서 -1로 대채해 재탐색되지 않도록 함.
    sorted_A[sorted_A.index(i)] = -1
 
results = [i for i in P]
 
for result in results:
    sys.stdout.write(str(result)+' ')