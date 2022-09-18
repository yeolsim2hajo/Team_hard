arr = [3,7,4,1,2,6]

check = [list(map(int, input().split())) for _ in range(2)]


        #! 2x2 배열을 순회할 for문 2개
for k in range(2):
    for i in range(2):

        #! flag를 설정 초기화를 잘해야 한다.!! 초기화 안하면 오류~
        flag=0

        #* arr의 값들과 2x2 배열의 값들을 비교하는 for문
        #* 만약에 값이 같다면, flag를 1로 저장한 후 break(종료) 값이 있으니까~
        #* 그 다음 코드를 실행, flag가 1이라면 ok를 출력 아니면 no를 출력
        #* 만약에 찾는 것이 없다면? for문 종료 후 flag=0  인 채로 if문에 들어감.
        #* 그렇게 해서 2번 반복 후 출력~ 2번 반복 후 출력~

        for j in range(0, len(arr)):
            if arr[j] == check[k][i]:
                flag = 1
                break

        if flag == 1:       
            print("OK", end=' ')
        else:
            print("NO", end= ' ')
    print()