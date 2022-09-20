# 답이 제일 깔끔
def sol(strings):
    result = []
    for i in range(1,len(strings)+1):
        for j in range(i):
            result.append(strings[j:j+len(strings)-i+1])
    return result

input1 = input()
input2 = input()

list1 = set(sol(input1))
list2 = set(sol(input2))

answers = list1.intersection(list2)

answer = max(answers,key=len)
print(len(answer))