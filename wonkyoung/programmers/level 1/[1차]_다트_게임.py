#230111
def solution(dartResult):
    index, answer = 0, []
    options = {'*', '#'}
    length = len(dartResult)

    def apply_Option(option):
        nonlocal score
        if option == '*':
            if answer:
                answer[-1] *= 2
            score *= 2
        else:
            score *= -1

    while index < length:
        if dartResult[index:index+2] != '10':
            score = int(dartResult[index])
            index += 1
        else:
            score = 10
            index += 2

        if dartResult[index] == 'D':
            score *= score
        elif dartResult[index] == 'T':
            score **= 3

        if index < length-1 and dartResult[index+1] in options:
            index += 1
            apply_Option(dartResult[index])

        answer.append(score)
        index += 1
    return sum(answer)

solution('1S2D*3T')
solution('1D2S#10S')
solution('1D2S0T')
solution('1S*2T*3S')
solution('1D#2S*3S')
solution('1T2D3D#')
solution('1D2S3T*')