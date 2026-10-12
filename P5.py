def are_anagrams(s1, s2):
    s1 = s1.lower().replace(" ", "")
    s2 = s2.lower().replace(" ", "")

    if len(s1)!= len(s2):
        return False

    freq = {}

    for ch in s1:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in s2:
        if ch not in freq:
            return False
        freq[ch] -= 1
        if freq[ch] < 0:
            return False

    for count in freq.values():
        if count!= 0:
            return False

    return True

print(are_anagrams("listen", "silent"))
print(are_anagrams("hello", "world"))