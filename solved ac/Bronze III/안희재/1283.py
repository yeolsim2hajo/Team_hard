import sys
from collections import defaultdict
input = sys.stdin.readline
dab = []
dic = defaultdict(int)
for _ in range(int(input())):
	s = input().split()
	tmp = []
	cnt = 0
	tf = False
	for i in s:
		if tf:
			tmp.append(i)
			continue
		if i[0].upper() in dic:
			cnt += 1
			tmp.append(i)
		elif i[0].upper() not in dic and not tf:
			tmp.append(i.replace(i[0], '['+i[0]+']', 1))
			dic[i[0].upper()] += 1
			tf = True
 
	if cnt == len(s):
		tmp = []
		for i in s:
			cnt = 0
			if tf:
				tmp.append(i)
				continue
			for j in i:
				if j.upper() in dic:
					cnt += 1
					if cnt == len(i):
						tmp.append(i)
				elif not tf and j.upper() not in dic:
					tf = True
					dic[j.upper()] += 1
					tmp.append(i.replace(j, '['+j+']', 1))
					continue
	dab.append(' '.join(tmp))
 
for i in dab:
	print(i)