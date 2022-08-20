
n = set(range(1, 76))
j = set(range(1, 28))
b = set(range(1, 14))

print("У будинку живе", len(n) + len(j ^ b), "сімей")
