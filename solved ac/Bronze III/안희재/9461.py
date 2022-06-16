t = int(input())
 
li = [1,1,1,2,2]
for i in range(5, 100):
    li.append(li[i-1]+li[i-5])
 
for _ in range(t):
    n = int(input())
    print(li[n-1])