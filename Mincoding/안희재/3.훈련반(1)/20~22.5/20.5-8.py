arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
idx1 = 0 # arr1의 인덱스
idx2 = 0 # arr2의 인덱스

#1 3 3 7
#2 3 4 6

result = []
for i in range(7): # 7 ㅠㅠ 마지막 추가하는 코드 구현 못해서 야매로 했음..
    if arr1[idx1] < arr2[idx2]:
        result.append(arr1[idx1])
        if idx1 + 1 == 4:
            continue
        else:
            idx1 += 1
    elif arr1[idx1] > arr2[idx2]:
        result.append(arr2[idx2])
        if idx2 + 1 == 4:
            continue
        else:
            idx2 += 1
    else: # 두개다 같다면,
        result.append(arr1[idx1])
        if idx1 + 1 == 4:
            continue
        else:
            idx1 += 1

result.append(max(arr1[idx1],arr2[idx2]))
# 근데.. ㄹㅇ 에반데.. 심지어 '일부정답'
# ㅅㅂ;;
# 1 2 3 4 / 5 6 7 8 하면 왜 -> 1 2 3 4 4 4 5가 나오지?
# 아.. 흠;; 인덱스가 끝으로 갈 경우가 계속 문제구나..

print(' '.join(map(str,result)))


