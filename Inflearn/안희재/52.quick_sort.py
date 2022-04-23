def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)

a = [6, 5, 1, 4, 7, 2, 3]
print(quick_sort(a))

# # 파이썬의 장점을 살린 퀵 정렬
# def quick_sort(array):
#     # 리스트가 하나 이하의 원소를 가지면 종료
#     if len(array) <= 1: return array
    
#     pivot, tail = array[0], array[1:]
    
#     leftSide = [x for x in tail if x <= pivot]
#     rightSide = [x for x in tail if x > pivot]
    
#     return quick_sort(leftSide) + [pivot] + quick_sort(rightSide)