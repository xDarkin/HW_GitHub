
c = set(range(1, 53))
z = set(range(1, 24))
m = set(range(1, 36))
b = set(range(1, 17))

print(len(c) - len(z) - len(m ^ b), "учнів не захоплюються колекціонуванням")
