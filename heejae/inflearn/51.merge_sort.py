def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
    
    mid = len(unsorted_list) // 2
    left = unsorted_list[:mid]
    right = unsorted_list[mid:]

    left1 = merge_sort(left) # left가 길이가 1이면 merge_sort(left) = left1은 바로 1짜리 리턴되고, 아래 merge가 이루어짐 1짜리 right이랑
    right1 = merge_sort(right)

    return merge(left1,right1) # merge함수로 정렬 및 합병이 되면, 더 상위 merge_sort로 back!

def merge(left,right):
    i = 0
    j = 0
    sorted_list = []

    while (i < len(left)) & (j < len(right)):
        if left[i] < right[i]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    while i < len(left):
        sorted_list.append(left[i]) # 8 7 6 5 vs 4 3 2 1일 경우 한쪽만 4개 남잖아.
        i += 1
    while j < len(right):
        sorted_list.append(right[j])
        j += 1

    return sorted_list

# 8 7 6 5 4 3 2 1
array = [8,7,6,5,4,3,2,1]
# num = list(map(int,input().split()))
print(merge_sort(array))