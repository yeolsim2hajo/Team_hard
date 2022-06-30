#2805 나무자르기
N, M = map(int,input().split())
heights = list(map(int,input().split()))
max_height = total = 0
min_height = int(2e9)
for height in heights:
    if height < min_height:
        min_height = height
    if height > max_height:
        max_height = height
    total += height
conf = total - min_height * N
if conf == M:
    answer = min_height
else:
    if conf > M:
        start = min_height
        end = max_height
        option = 0
    else:
        start = 0
        end = min_height
        option = 1

    def find_answer():
        global start, end, answer
        while start <= end:
            mid = (start + end)//2
            height_sum = 0
            if option == 0:
                for height in heights:
                    if height > mid:
                        height_sum += height - mid
            else:
                height_sum = total - mid * N

            if height_sum == M:
                return mid
            elif height_sum > M:
                start = mid + 1
            else:
                end = mid - 1
        return end
    answer = find_answer()
print(answer)


# 함수 사용 - 시간 덜 걸림 (이진탐색 함수 아니면 시간 더 걸림)
N, M = map(int,input().split())
heights = list(map(int,input().split()))
max_height = max(heights)
min_height = min(heights)
total = sum(heights)
conf = total - min_height * N
if conf == M:
    answer = min_height
else:
    if conf > M:
        start = min_height
        end = max_height
        option = 0
    else:
        start = 0
        end = min_height
        option = 1

    def find_answer():
        global start, end, answer
        while start <= end:
            mid = (start + end)//2
            height_sum = 0
            if option == 0:
                for height in heights:
                    if height > mid:
                        height_sum += height - mid
            else:
                height_sum = total - mid * N

            if height_sum == M:
                return mid
            elif height_sum > M:
                start = mid + 1
            else:
                end = mid - 1
        return end

    answer = find_answer()
print(answer)