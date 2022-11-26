# 221126
def rot13():
    S = input()
    result = ''
    match = {}
    ascii_a,ascii_A = ord('a'), ord('A')
    for i in range(13):
        small_before, large_before = chr(ascii_a + i), chr(ascii_A + i)
        small_after, large_after = chr(ascii_a + i + 13), chr(ascii_A + i + 13)

        match[small_before] = small_after
        match[small_after] = small_before
        match[large_before] = large_after
        match[large_after] = large_before

    for munja in S:
        if munja.isalpha():
            result += match[munja]
        else:
            result += munja

    return result

print(rot13())