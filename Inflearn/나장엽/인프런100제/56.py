
nationWidth = {
'korea': 220877,
'Rusia': 17098242,
'China': 9596961,
'France': 543965,
'Japan': 377915,
'England' : 242900 }

target = nationWidth['korea']
nationWidth.pop('korea')
lst = list(nationWidth.items())
max = max(nationWidth.values())

mini = 0
for i in lst:
    if max > abs(i[1] - target):
        max = abs(i[1] - target)
        mini = i

print(mini[0], mini[1] - 220877)