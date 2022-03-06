arr = [3,7,6,4,2,9,1,7]
input = list(map(int, input().split()))


#기차에 탄 사람들 중에 우리팀이 있는지 찾으려함
#우리팀은 3명...붙어있음 = 연속된 배열임 
#우리팀 입력받고.. 몇 번 칸부터 몇 번째 칸에 탑승하고 있는 지 출력해라~


# arr 중에서 input에 해당하는 패턴을 찾기.
# 패턴이 발견되면 종료하기..?


for i in range(6):
    find = 0
    for k in range(len(input)): # 0 1 2 
        if input[k] == arr[i+k]:
            find = 1
            print("{0}번~{1}번 칸".format(i, i+2))
        if find == 1:
            break
        
