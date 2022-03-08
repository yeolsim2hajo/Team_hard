string = [len(input()) for _ in range(4)]

# string 인덱스를 각각 level이라고 하고, min,max를 계속 갱신시킬때
# 인덱스를 level로 저장해두면 될듯
max_index, min_index = 0, 0

def abc(level, min, max):
    global max_index, min_index
    if level == 4:
        print(f'긴문장:{max_index}')
        print(f'짧은문장:{min_index}')
        return

    if min > string[level]:
        min = string[level]
        min_index = level
        
    if max < string[level]:
        max = string[level]
        max_index = level
    
    abc(level+1, min, max)

abc(0, 2e18, 0) #level, min, max길이