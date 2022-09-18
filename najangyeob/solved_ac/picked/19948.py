# 시는 대문자, 소문자 알파벳과 빈칸으로 이루어짐
# 시에 나오는 단어들의 첫 글자를 대문자로 바꾼 뒤 순서대로 이어서 제목을 만든다
# 시의 내용이 there is no cow lovel -> TINCL

# 스페이스(빈칸)과 영자판을 누를 수 있는 횟수가 정해져 있음
# 같은 문자가 연속으로 나오거나, 빈칸이 연속으로 나오는 경우 꾹 눌러 한번만으로 해결가능
# 시의 내용과 시의 제목은 enter 키로 구분, shift, enter은 무한
# 시의 내용과 제목을 모두 기록하면 시의 제목을 출력
# 기록못하면 -1 출력


# poetry = list((input().split()))  #['There', 'is', 'no', 'cow', 'level']
# poetry = [list(i) for i in poetry]
# print(poetry)


# space = int(input())
# remain = list(map(int, input().split()))
# alpha = [chr(i).lower() for i in range(65, 91)]

# check = [False]*26

# dic = list(zip(remain, alpha))
# for i in range(len(dic)): # 튜블 자료형으로 zip 된 요소들을 list 형으로 변경
#     dic[i] = list(dic[i]) 


# for word in poetry:
#     for w in word:
#         for i in range(len(dic)):
#             if dic[i][0] > 0 and dic[i][1] == w:
#                 dic[i][0] -= 1
                
                

# print(poetry)
# print(dic)







