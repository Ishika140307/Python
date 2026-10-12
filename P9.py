score = 50

def update():
    global score
    print(score)
    score = score + 10

update()
print(score)

'''1. Why error?
In Python, if you assign to a variable inside a function, Python treats it as a local variable for the entire function. In update(), score = score + 10 makes score local. So print(score) on the previous line tries to read the local score before it is assigned -> UnboundLocalError: cannot access local variable 'score' where it is not associated with a value.

2. Correct use of global?
Add global score at the start of the function. This tells Python you want to use the global score, not create a local one.

3. Output after correction:

Code
50
60'''