count = 1   # 그룹 번호
while True:
    nasty = 1
    name = []
    word = []
    n = int(input())
    
    if n == 0:  # 0 입력받을 시 종료
        break
    for _ in range(n):
        n_w = input()   #이름 & 메시지 한번에 입력
        new = n_w.split()   
        name.append(new[0]) #이름 저장
        for _ in range(1,n):
            word.append(new[_]) #메시지 저장
    print("Group",count)
    size = n-1  
    for i in range(len(word)):  #단어의 개수만큼 반복
        if word[i] == 'N':  #나쁜 말이면
            print(name[size],"was nasty about",name[i//(n-1)])
            nasty = 0
        size -= 1
        if size == -1:
            size = n-1
    if nasty:   
        print("Nobody was nasty")
    print("")
    count += 1