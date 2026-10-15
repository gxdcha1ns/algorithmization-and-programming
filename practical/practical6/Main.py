s = "Hello123"
letters = digits = others = 0
for c in s:
    o = ord(c)
    if 48 <= o <= 57:
        digits += 1
    elif 65 <= o <= 90 or 97 <= o <= 122:
        letters += 1
    else:
        others += 1
print(letters, digits, others)

s = "A man a plan a canal Panama"
s = s.lower()
filtered_chars = []
for c in s:
    o = ord(c)
    if 97 <= o <= 122 or 48 <= o <= 57:
        filtered_chars.append(c)
is_palindrome = filtered_chars == filtered_chars[::-1]
print(is_palindrome)