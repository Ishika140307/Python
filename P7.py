def analyze_marks(*args):
    if len(args) == 0:
        return "No marks provided"

    total = 0
    highest = args[0]
    passing = 0

    for mark in args:
        total += mark
        if mark > highest:
            highest = mark
        if mark >= 40:
            passing += 1

    average = total / len(args)

    return f"Total: {total}\nAverage: {average}\nHighest: {highest}\nPassing count: {passing}"

print(analyze_marks(35, 72, 80, 45, 90, 30))
