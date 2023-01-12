#221011
command = input()
match = {'c': 26, 'd': 10}
total = match[command[0]]
for i in range(1, len(command)):
    next_num = match[command[i]]
    if command[i] == command[i-1]:
        next_num -= 1
    total *= next_num
print(total)