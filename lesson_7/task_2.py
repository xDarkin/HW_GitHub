
v = list(input("Input numbers: "))
k = int(input("Input index: "))
C = input("Input insertable number: ")
print(v)
v[k+1:len(v)+1] = v[k:len(v)]
v[k] = C
print(v)
