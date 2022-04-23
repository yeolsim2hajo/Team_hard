nationWidth = {
	'korea': 220877, 
	'Rusia': 17098242, 
	'China': 9596961, 
	'France': 543965, 
	'Japan': 377915,
	'England' : 242900,
}

standard = nationWidth['korea']
nationWidth.pop('korea') # 오호;; 딕셔너리도 이렇게 키를 기준으로 pop가능!
item_list = list(nationWidth.items())
result = ''
Min = max(nationWidth.values())
for ele in item_list:
    if Min > abs(ele[1]-standard):
        Min = abs(ele[1]-standard)
        result = ele[0]

print(result,Min)