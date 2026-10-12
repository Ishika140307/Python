def longest_consecutive_run(numbers):
    if not numbers:
        return 0

    max_count = 1
    current_count = 1

    for i in range(1, len(numbers)):
        if numbers[i] == numbers[i - 1]:
            current_count += 1
        else:
            if current_count > max_count:
                max_count = current_count
            current_count = 1

    if current_count > max_count:
        max_count = current_count

    return max_count

print(longest_consecutive_run([1, 1, 2, 2, 2, 3, 3, 1, 1, 1, 1]))
print(longest_consecutive_run([7, 7, 7, 7]))