str_lst = list(input())
from_str = input()
to_str = input()

for i in range(len(str_lst)):
    if str_lst[i] == from_str:
        str_lst[i] = to_str

print(''.join(str_lst))