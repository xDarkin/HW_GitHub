# заміна значень 2х змінних використовючи 3-тю змінну - рузультат вивести на в термінал
a = 100
b = 200
c = a
a = b
b = c
print(a, b)
# заміна значень 2х змінних використовуючи властивості python - рузультат вивести на в термінал
a = 100
b = 200
a, b = b, a
print(a, b)
# заміна значень 2 змінних не використівуючи 2х попредніх варіантів
a = 100
b = 200
a = a + b
b = a - b
a = a - b
print(a, b)
