#1
# munjayeol = input()
# alp = {}
# for i in range(6):
#     alp[chr(i+65)] = 0
# for element in munjayeol:
#     if alp.get(element.upper(),-1) != -1:
#         alp[element.upper()] += 1
# for key,value in alp.items():
#     print(f'{key}:{value}')


#2 빠른 이름검색
# team = {'POP': 'yes','TOM': 'yes','MC': 'yes','JASON': 'yes','KFC': 'yes'}
# N = int(input())
# for i in range(N):
#     print(team.get(input(),'no'))


#3 같은 단어 찾아내기
# hard = 'BOBOOBOBOBOBBM'
# word_3 = {}
# for i in range(len(hard)-2):
#     idx = hard[i:i+3]
#     if idx in word_3.keys(): # 값 존재
#         word_3[idx] += 1
#     else: # 값 존재
#         word_3[idx] = 1
# N = int(input())
# for i in range(N):
#     print(word_3.get(input(),0))


#4 공룡들의 나이 정리
# age = int(input())
# dino = {5:'Sour', 2:'Dav', 3:'Nica', 6:'Timer', 15:'Pico',22:'Topisl',13:'Whab',9:'Hap'}
# print(dino.get(age-1000000000))