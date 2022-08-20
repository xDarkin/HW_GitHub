
clas = set(range(1, 41))
a = set(range(1, 26))
b = set(range(1, 23))
c = set(range(1, 23))
ab = 33
ac = 32
bc = 31
abc = 10

ab_1 = len(a) + len(b) - ab - abc
ac_1 = len(a) + len(c) - ac - abc
bc_1 = len(b) + len(c) - bc - abc

a_1 = len(a) - ab_1 - ac_1 - abc
b_1 = len(b) - ab_1 - bc_1 - abc
c_1 = len(c) - ac_1 - bc_1 - abc

print("Одну книгу прочли", a_1 + b_1 + c_1, "учнів")
print("Дві книги прочли", ab_1 + bc_1 + ac_1, "учнів")
print("Жодної книги не прочли", len(clas) - a_1 - b_1 - c_1 - ab_1 - ac_1 - bc_1 - abc, "учнів")
