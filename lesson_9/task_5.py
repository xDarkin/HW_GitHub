
v = str("pythonist")
dict_1 = {}

for i in v:
    n = v.count(i)
    dict_1.update({i: n})
print(dict_1)
