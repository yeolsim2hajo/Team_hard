time = []
result = 0
for second in range(0, 4):
    time.append(int(input()))

for min in time:
    result = result+min


if (60 <= result <= 3599):
    print(result//60)
    print(result%60)
else:
    pass;