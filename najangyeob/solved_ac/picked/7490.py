def recur(sum, sign, num, n, string):
  if (n == N):
    sum = sum + (sign*num)
    if sum == 0:
      print(string)
  else:
    recur(sum, sign, num*10+(n+1), n+1, string+' '+str(n+1))
    recur(sum+sign*num,1, (n+1), n+1, string+'+'+str(n+1))
    recur(sum+sign*num, -1, (n+1), n+1, string+'-'+str(n+1))
      
test_case = int(input())

for _ in range(test_case):
  N = int(input())
  recur(0,1,1,1,"1")
  print()