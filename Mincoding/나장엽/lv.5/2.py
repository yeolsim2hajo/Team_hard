from xml.etree.ElementTree import SubElement


arr = list(map(int, input().split()))


sum = 0
for i in range(len(arr)):
    sum += arr[i]
    
print(sum)