# 길이가 짧은 것 부터
# 길이가 같으면 사전 순으로
N = int(input())
words = []
for i in range(N):
    words.append(input())


words = set(words) # 중복제거
words = list(words) # 다시 list 형 변환
words.sort()
words.sort(key=len) #단어 길이를 기준으로 sort.
    
for i in words:
    print(i)


for _ in range(N):
    word = str(input())
    word_len = len(word)
    words.append((word, word_len))

#중복삭제
words = list(set(words))
words.sort(key=lambda word : (word[1], word[0]))

for word in words:
    print(word[0])

# for i in range(1, len(words)):
#     if len(words[i-1]) == len(words[i]): #단어의 길이가 같은 경우 사전순으로 해야함.
#         for k in range(len(words)):
#             if words[i-1][k] > words[i][k]: # 단어의 첫번째 글자 대소 비교
#                 words[i-1], words[i] = words[i], words[i-1] 

#             elif words[i-1][k] == words[i][k]: # 첫 번째 글자가 같은 글자라면
#                 if k < len(words):
#                     if words[i-1][k+1] > words[i][k+1]: # 두 번째 글자 비교
#                         words[i-1], words[i] = words[i], words[i-1] 
#                     else:
#                         continue
#             else:
#                 continue
    
# for i in words:
#     print(i)


