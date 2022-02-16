cardList = input()

bucket = []

for i in range(len(cardList)):
    if cardList[i] in bucket:
        continue
    else:
        bucket.append(cardList[i])

print(f'{len(bucket)}개')

