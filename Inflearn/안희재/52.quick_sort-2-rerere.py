def quick_sort(arr):
    def sort(low, high):
        if high <= low:
            return

        mid = partition(low, high)
        sort(low, mid - 1)
        sort(mid, high)

    def partition(low, high):
        pivot = arr[(low + high) // 2]
        while low <= high:
            while arr[low] < pivot:
                low += 1
            while arr[high] > pivot:
                high -= 1
            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
                low, high = low + 1, high - 1
        return low

    return sort(0, len(arr) - 1)

array = [6, 5, 1, 4, 7, 2, 3]
quick_sort(array) # 이거만 찍으면 모르지.. 와우 신기하네 되게
print(array) # 아. quick_sort는 정렬시키는 함수구나;;; arr.sort() 처럼;;;;

# https://www.daleseo.com/sort-quick/ - 아 쥰내 어렵다..
# 재귀인데, 2번호출임.. 그래프모양으로 그리면서 해야할듯..
# 더 어렵긴 한데, 이것이 최적화된 코드....