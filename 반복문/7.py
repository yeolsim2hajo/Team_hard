arr = [2,7,9,3,6,7,2,9,0,1]
# 2,7,9,9,0,1,2,7,9,9,0,1
# 2개 붙인다음, 2칸 move고,
# 처음에 6개 가져왔으면 6개의 끝에서 2개부터 6개 다시 가져오면 됨

s, e = map(int,input().split())

arr_before = arr[0:s]
arr_after = arr[e+1:len(arr)]

    