# DAT 써야 할듯
# 뭐야 입력에도 # 붙여야 하네 일단 마지막에 해결하자
# 변환하는 함수 새로 만들자 아예 -> 음.. 다르게 해보자 너무 길어진다 코드
# 이게 DAT 끝판왕 같다. 알파벳은 ord,chr썼지만 그냥 이렇게 하는게 재사용성 측면에서 제일 좋은 듯

T = int(input())

for tc in range(1,T+1):
        
    a, N = input().split()
    N = int(N)
    str = input().split()
    # str = SVN FOR ZRO NIN FOR EGT EGT TWO FOR FIV FIV
    # N = 11
    galaxy = ['ZRO','ONE','TWO','THR','FOR','FIV','SIX','SVN','EGT','NIN']
    # order = [0,1,2,3,4,5,6,7,8,9]

    arr = [0] * 10
    for i in range(len(str)):
        for j in range(len(galaxy)):
            if str[i] == galaxy[j]:
                arr[j] += 1

    result = ''
    for i in range(len(arr)):
        result += f'{galaxy[i]} ' * arr[i]

    print(a)
    print(result)
