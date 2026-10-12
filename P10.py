def process_numbers(numbers):
    squared = []

    for num in numbers:
        if num < 0:
            continue
        if num % 2!= 0:
            continue
        squared.append(num * num)

    if len(squared) == 0:
        return "Total: 0\nCount: 0\nLargest squared value: None"

    total = 0
    largest = squared[0]

    for val in squared:
        total += val
        if val > largest:
            largest = val

    return f"Total: {total}\nCount: {len(squared)}\nLargest squared value: {largest}"

def process_numbers_functional(numbers):
    from functools import reduce

    filtered = list(filter(lambda x: x >= 0 and x % 2 == 0, numbers))
    squared = list(map(lambda x: x * x, filtered))

    if not squared:
        return "Total: 0\nCount: 0\nLargest squared value: None"

    total = reduce(lambda a, b: a + b, squared)

    return f"Total: {total}\nCount: {len(squared)}\nLargest squared value: {max(squared)}"

numbers = [-2, 1, 2, 3, 4, 6, -8]

print(process_numbers(numbers))
print()
print(process_numbers_functional(numbers))