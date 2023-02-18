#230218
def solution(numbers):
    def find_number(number):
        def convert_binary(number):
            reversed_binary = []
            if number == 0:
                return [0]
            while number:
                reversed_binary.append(number%2)
                number //= 2
            return reversed_binary
        def convert_decimal(num_list):
            decimal_number = 0
            multiple = 1
            for number in num_list:
                decimal_number += number*multiple
                multiple *= 2
            return decimal_number

        reversed_binary = convert_binary(number)
        length = len(reversed_binary)
        for i in range(length):
            if reversed_binary[i] == 0:
                reversed_binary[i] = 1
                if i >= 1:
                    reversed_binary[i - 1] = 0
                return convert_decimal(reversed_binary)
        reversed_binary[-1] = 0
        reversed_binary.append(1)
        return convert_decimal(reversed_binary)

    answer = []
    for number in numbers:
        answer.append(find_number(number))

    return answer
