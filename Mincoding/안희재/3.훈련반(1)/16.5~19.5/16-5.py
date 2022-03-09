lst = list(input())
idx = int(input())

# 내장함수 쓰면 금방이겠지만, 그걸 원하는 것은 아닌것 같음

new_lst = [0] * (len(lst)-1)

new_lst[0:idx] = lst[0:idx]
new_lst[idx:len(lst)] = lst[idx+1:len(lst)]

print(''.join(map(str,new_lst)))