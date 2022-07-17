# while 1:
#     word = input()
#     if word == '*':
#         break
#     check = 1
#     for x in range(1,len(word)): # 거리가 1,2,3 ... n-1
#         result = []

        # for y in range(len(word)): # 0쌍, 1쌍, 2쌍 ... n-2쌍
        #     if y+x < len(word):
        #         result.append(word[y]+word[x+y])
        # # if len(result) = ~~

        # for z in range(len(result)):
        #     if result[z] in result[z+1]:
        #         check = 0
#     if check:
#         print(word + " is surprising.")
#     else:
#         print(word + " is NOT surprising.")


while True:
    word = input()
    if word == "*":
        break
    
    for x in range(1,len(word)-1): # 0쌍부터, n-2쌍까지(0쌍: 거리1, 1쌍: 거리2 ...)
        dict = set()

        for y in range(len(word)-x):
            tmp = word[y]+word[y+x]
            if tmp in dict:
                print(word,"is NOT surprising.")
                break
            else:
                dict.add(tmp)
        else: # for else문 - 위에서 break가 안나온다면, continue
            continue
        break
    else:
        print(word,"is surprising.")