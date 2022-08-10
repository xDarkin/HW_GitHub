
a = list(input("Input first list of numbers: "))
b = list(input("Input second list of numbers: "))
count = 0
a[len(a):] = b
for i in range(0, len(a)):
    a[i] = int(a[i])
for i in range(0, 10):
    if a.count(i) == 1:
        count += 1
print(count)
