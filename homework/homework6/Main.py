text = "hello"
shift = 3
encrypted = ""
for char in text:
    code = ord(char) - ord('a')
    code = (code + shift) % 26
    encrypted += chr(code + ord('a'))
print(f"Зашифрований текст: \"{encrypted}\"")