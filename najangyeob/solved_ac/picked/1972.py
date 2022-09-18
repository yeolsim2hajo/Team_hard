
# D-쌍 거리가 D인 두 문자를 순서대로 나열한 것을 이 문자열의 D-쌍
# 문자열의 길이가 N이라고 할때, 0 ~ N-2 쌍 까지 정의 된다
# 만일 정의되는 D에 대해, 어 떤 문자열의 모든 D쌍들이 서로 다를 때, 이 문자열을 D-유일하다고 한다.
# 예를 들어 ZGBG -> 0 쌍 : ZG GB BG, 1쌍 : ZB, GG, 2쌍 : ZG
# 어떤 문자열이 정의되는 모든 D에 대해 D-유일하면, 이 문자열을 정말이지 '놀라운 문자열'이라고 한다. 문자열이 주어질 때, 이 문자열이 놀라운 문자열인지 아닌지를 구하는 프로글매을 작성해라
Strings = []
while True:
    String = input()

    if String == '*':
        break
    else:    
        Strings.append(String)

# pair 초기화
pair = [] 
for i in range(len(Strings)):
    pair.append([])
    for k in range(len(Strings[i]) - 1):
        pair[i].append([])

# 쌍을 만들고, pair에 append
for i in range(len(Strings)): 
    if len(Strings[i]) == 1:
        pair[i].append(Strings[i])

    for k in range(0, len(Strings[i]) - 1): 
        for j in range(0, len(Strings[i]) - 1): 
            if (j + k + 1) < len(Strings[i]):
                temp_str = Strings[i][j]+Strings[i][j+k+1]
                pair[i][k].append(temp_str)


# 각 쌍마다 중복이 있는지 체크 -> len 함수를 이용하여 체크함.
for i in range(len(pair)):
    flag = True
    for k in range(len(pair[i])):
       if len(pair[i][k]) != len(set(pair[i][k])): # 길이가 다르다 -> 중복된 것이 있다. -> NOT surprising -> break문으로 탈출하여 다음 문자를 검사한다
           flag = False
           break

    
    if flag == False:
        print(f'{Strings[i]} is NOT surprising.')
    else:
        print(f'{Strings[i]} is surprising.')

