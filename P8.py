def is_palindrome_recursive(text, left=0, right=None):
    if right is None:
        right = len(text) - 1
    if left >= right:
        return True
    if text[left]!= text[right]:
        return False
    return is_palindrome_recursive(text, left + 1, right - 1)

print(is_palindrome_recursive("racecar"))
print(is_palindrome_recursive("python"))