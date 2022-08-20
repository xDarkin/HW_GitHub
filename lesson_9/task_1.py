
dic_1 = {"a": 300, "b": 400}
dic_2 = {"c": 500, "d": 600}

a = dic_1["a"]
b = dic_1["b"]
c = dic_2["c"]
d = dic_2["d"]

v = list(dic_1)
n = list(dic_2)

dic_3 = {v[0]: a, v[1]: b, n[0]: c, n[1]: d}
print(dic_3)
