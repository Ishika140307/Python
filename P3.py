def find_missing_sum(numbers, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = 0
    for num in numbers:
        actual_sum += num
    return expected_sum - actual_sum

def find_missing_xor(numbers, n):
    xor_all = 0
    xor_list = 0
    for i in range(1, n + 1):
        xor_all ^= i
    for num in numbers:
        xor_list ^= num
    return xor_all ^ xor_list

print(find_missing_sum([1, 2, 4, 6, 3, 7, 8], 8))
print(find_missing_sum([2, 3, 4, 5], 5))

print(find_missing_xor([1, 2, 4, 6, 3, 7, 8], 8))
print(find_missing_xor([2, 3, 4, 5], 5))