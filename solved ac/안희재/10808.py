words = input()
bucket = [0]*26 # 알파벳 개수는 총 26개 -> 각각 몇번이 포함되어 있는지에 대한 bucket

for word in words:
    bucket[ord(word)-97] += 1
    
for ele in bucket:
    print(ele, end=' ')