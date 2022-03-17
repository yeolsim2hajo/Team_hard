#56 리스트
nationwidth = {
    'Korea':220877,
    'Rusia': 17098242,
    'China' : 9596961,
    'France' : 543965,
    'Japan' : 377915,
    'England' : 242900}
ans = 'Rusia'
min_val = nationwidth[ans]
for key in nationwidth.keys():
    if key != 'Korea':
        if min_val > nationwidth[key]:
            min_val = nationwidth[key] - nationwidth['Korea']
            ans = key
print(ans,min_val)

