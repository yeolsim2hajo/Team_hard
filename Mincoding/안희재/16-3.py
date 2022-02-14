str = list(input())
num = int(input())

new_list = [0] * (len(str))

new_list[0:num] = str[0:num]
new_list[num] = 'A'
new_list[num+1:len(new_list)] = str[num:len(str)]

print(''.join(new_list))