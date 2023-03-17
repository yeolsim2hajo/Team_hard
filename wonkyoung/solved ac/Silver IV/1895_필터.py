#230317
def greater_than_t():
    R, C = map(int, input().split())
    pixel_arr = [list(map(int, input().split())) for _ in range(R)]
    T = int(input())
    def find_filter_value():
        from collections import deque
        cnt = 0
        for j in range(C-2):
            filter = deque()
            for i in range(2):
                filter.extend(pixel_arr[i][j:j+3])
            for i in range(R-2):
                filter.extend(pixel_arr[i+2][j:j+3])
                sorted_filter = sorted(filter)
                if sorted_filter[4] >= T:
                    cnt += 1
                for _ in range(3):
                    filter.popleft()
        return cnt
    return find_filter_value()
print(greater_than_t())

