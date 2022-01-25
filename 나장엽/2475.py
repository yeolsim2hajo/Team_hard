from ipaddress import summarize_address_range


number = list(map(int, input().split(" ")))
sum = 0
result = 0

for i in number:
    sum += i**2
result = sum % 10

print(result)