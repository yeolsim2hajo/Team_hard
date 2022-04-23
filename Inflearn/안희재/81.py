# 내 풀이 - 그냥, 깃발찾으면 direct돌려서 배열범위내인 곳에 지뢰깔기
# 아래는 레퍼런스

#첫번째 풀이
value ='''0 1 0 0 0
    0 0 0 0 0
    0 0 0 1 0
    0 0 1 0 0
    0 0 0 0 0'''

    print(value.split('\n'))
    sp = value.split('\n')
    count = 0
    for i in sp:
        sp[count] = i.replace('1', 'f').split(' ')
        count += 1
    print(sp)
    count = 0
    search = 0
    for s in sp:
        for i in s:
            if i == 'f':
                search = s.index(i)
                if search > 0:
                    s[search-1] = '*'
                if search < 4:
                    s[search+1] = '*'
                if count > 0:
                    sp[count-1][search] = '*'
                if count < 4:
                    sp[count+1][search] = '*'
        count += 1
    for i in sp:
        print(i)

# #두번째 풀이
# inputList = []
#     for i in range(5):
#         inputList.extend(input().split())
#     for i in range(25):
#         if inputList[i] == "1":
#             inputList[i] = "f"
#             if i // 5 != 0:
#                 inputList[i - 5] = "*"
#             if i // 5 != 4:
#                 inputList[i + 5] = "*"
#             if i % 5 != 0:
#                 inputList[i - 1] = "*"
#             if i % 5 != 4:
#                 inputList[i + 1] = "*"
#     for i in range(25):
#         if i % 5 != 4:
#             print(inputList[i], end = "")
#         else:
#             print(inputList[i], " ")