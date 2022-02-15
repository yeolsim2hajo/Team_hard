arr = list(map(int,'59461589'))
hard_coding = ['ATKB','CZFD','HGEI']
arr = ['']*3
for i in range(len(hard_coding)):
    arr[i] = list(map(str,hard_coding[i]))

print(arr)