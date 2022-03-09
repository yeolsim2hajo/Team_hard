arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

result = []
for i in range(8):
    if len(arr1) != 0 and len(arr2) != 0:
        if arr1[0] <= arr2[0]:
            result.append(arr1[0])
            arr1 = arr1[1:]
        elif arr1[0] > arr2[0]:
            result.append(arr2[0])
            arr2 = arr2[1:]
    elif len(arr1) != 0: # arr1만 on일때
        result.append(arr1[0])
        arr1 = arr1[1:]
    else: # arr2만 on일때
        result.append(arr2[0])
        arr2 = arr2[1:]


print(' '.join(map(str,result)))

# --------------------------------
# 원경 코드
# 나 처음에, 인덱스로 하려다가 실패했음. 아래처럼 하면 되는구먼..
# arr1 = list(map(int, input().split()))
# arr2 = list(map(int, input().split()))
# result = []
# idx1 = idx2 = 0

# while idx1 < 4 and idx2 < 4:
#     if arr1[idx1] < arr2[idx2]:
#         result += [arr1[idx1]]
#         idx1 += 1
#     else:
#         result += [arr2[idx2]]
#         idx2 += 1
# if idx1 < 4: # -> idex2 == 4가 이해가 더 쉽긴 하다
#     result += arr1[idx1:]
# else:
#     result += arr2[idx2:]
# print(*result)

# --------------------------------
# 박한 코드 - 재귀로;; ㄷㄷ 재귀의 신
# 와우;;
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# lst = [0]*8
# def abc(al, bl):
#     if al+bl == 8:
#         return
#     if al>=4:
#         lst[al+bl] = b[bl]
#         abc(al, bl+1)
#     elif bl>=4:
#         lst[al+bl] = a[al]
#         abc(al+1, bl)
#     elif a[al] > b[bl]:
#         lst[al+bl] = b[bl]
#         abc(al, bl+1)
#     else:
#         lst[al+bl] = a[al]
#         abc(al+1, bl)
# abc(0, 0)
# print(*lst)
# --------------------------------