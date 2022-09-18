N = input()
F = int(input())
number = int(N[:-2] + '00')

while True:
    if number % F == 0:
        break
    else:
        number += 1
print(str(number)[-2:])


