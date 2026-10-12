def move_zeros_new_list(numbers):
    result = []
    zero_count = 0
    for num in numbers:
        if num!= 0:
            result.append(num)
        else:
            zero_count += 1
    result.extend([0] * zero_count)
    return result

def move_zeros_in_place(numbers):
    pos = 0
    for i in range(len(numbers)):
        if numbers[i]!= 0:
            numbers[pos] = numbers[i]
            pos += 1
    while pos < len(numbers):
        numbers[pos] = 0
        pos += 1
    return numbers

numbers = [0, 1, 0, 3, 12, 0, 5]

print(move_zeros_new_list(numbers))
print(move_zeros_in_place(numbers.copy()))