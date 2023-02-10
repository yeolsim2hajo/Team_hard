def solution(numbers, k):
    length = len(numbers)
    half, remain = divmod(length, 2)
    if remain == 0:
        index = (k-1)%half
        return numbers[2*index]
    index = (k-1)%length
    for i in range(1, length//2+1):
        number = numbers.pop(i)
        numbers.append(number)
    return numbers[index]