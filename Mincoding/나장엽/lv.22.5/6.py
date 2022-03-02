# 문장을 네개 입력받고, 가장짧은 문장부터 긴 문장까지 오름차순으로 정리해라

# 각 문장의 len을 저장한 list와 정렬할 list를 매개변수로 넘겨주기
# 버블정렬을 통해서 정렬해버리기 

def bubblesort(arr, str):
    for i in range(len(arr)-1, 0, -1):
        for k in range(i):
            if arr[k] > arr[k+1]:
                arr[k], arr[k+1] = arr[k+1], arr[k]
                str[k], str[k+1] = str[k+1], str[k]
    return str

str = list(input() for _ in range(4))

length = []
for i in range(4):
    length.append(len(str[i]))

result = bubblesort(length, str)

for i in range(4):
    print(result[i])