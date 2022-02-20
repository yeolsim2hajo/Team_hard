# arr = [[1,2,3,4], [5,6,7,8,], [9,10,11,12], [13,14,15,16]]

bucket = [0] * 16

nums = list(map(int,input().split()))

for i in range(len(nums)):
    bucket[nums[i]-1] = i+1

for i in range(0,16,4):
    print(*bucket[i:i+4])
