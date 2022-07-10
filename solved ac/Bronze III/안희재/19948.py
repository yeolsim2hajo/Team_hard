# 난 처음에, strings를 content로 했었음 -> strings / string 이렇게 변수 짓는게 더 직관적

strings = input().split() # 시의 내용
space = int(input()) # 스페이스 사용가능 횟수
counts = list(map(int,input().split())) # 각 알파벳의 사용가능 횟수

# strings = ['There', 'is', 'no', 'cow', 'level']
if len(strings)-1 > space: # 공백이 스페이스보다 많으면 -1
    print(-1)
else:
    # 1)strings(시의 내용)을 쓸 수 있는가?
    answer = True
    title = ''
    idx = 0
    while answer and idx < len(strings):
        string = strings[idx]
        i = 0
        while i < len(string):
            if i >= 1 and string[i] == string[i-1]:
                i += 1
                continue
            if counts[ord(string[i].lower())-97] >= 1:
                counts[ord(string[i].lower())-97] -= 1
            else:
                answer = False
                break
            i+= 1
        idx += 1
        if answer:
            title += string[0].upper()
    
    # 2)시의 내용을 쓸 수 있다면, 이제 title을 쓸 수 있는지를 마지막으로 체크
    if answer: # 위에서 answer = False였다면, title이 가능한지 체크할 필요도 없음
        temp = title.lower()
        i = 0
        while i < len(temp):
            if i>= 1 and temp[i] == temp[i-1]:
                i += 1
                continue
            if counts[ord(temp[i])-97] >= 1:
                counts[ord(temp[i])-97] -= 1
            else: # 자판 제한을 초과했다면, 끝
                answer = False
                break
            i += 1
        if answer:
            print(title)
        else:
            print(-1)
    else:
        print(-1)