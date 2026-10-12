def second_largest_distinct(numbers):
    if len(numbers) < 2:
        return "No second-largest distinct value"
    
    largest = None
    second = None

    for num in numbers:
        if largest is None or num > largest:
            second = largest
            largest = num
        elif num != largest and (second is None or num > second):
            second = num
    
    if second is None:
        return "No second-largest distinct value"
    return second

print(second_largest_distinct([12, 35, 1, 10, 34, 35]))
print(second_largest_distinct([5, 5, 5, 4]))
print(second_largest_distinct([10, 10, 10]))
print(second_largest_distinct([-5, -2, -10, -1]))