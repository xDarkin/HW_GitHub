
v = list(input("Input numbers: "))
k = int(input("Input index: "))
C = input("Input insertable number: ")
print(v)
v[k+1:len(v)] = v[k:len(v)-1]
v[k] = C
v.append("!")
print(v)
