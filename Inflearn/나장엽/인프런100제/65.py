from re import L


a = [1,2,3,4]
b = ['a','b','c','d']


answer = []    
index = 0
for i, k in zip(a, b):
    if index % 2 == 0: 
        answer.append([i, k])
    else:
        answer.append([k, i])
    index += 1
    
print(answer)
        