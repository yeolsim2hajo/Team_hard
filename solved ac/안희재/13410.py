N, K = map(int, input().split())

arr = []
for i in range(1, K + 1) :
  tmp = str(N * i) # 문자로 바꿔줘야 앞뒤를 바꿀 수 있음
  arr.append(int(tmp[::-1])) # 넣을 때는, 다시 int로

print(max(arr))