# 빽트랙킹 연습인듯?
# level 5까지 돌리되, 그 이전에 발견하면 바로 끝!
arr = ['Jason', 'Dr.tom', 'EXEXI', 'GK12P', 'POW']
pw = input()

def abc(level):
    if level == 5: # 여기까지 했다면 이미 arr전부 순회한것
        print('암호틀림')
        return
        
    if arr[level] == pw:
        print('암호해제')
        return


    abc(level+1)
    
abc(0)