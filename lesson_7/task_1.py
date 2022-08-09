
v = list(input("Input numbers: "))
k = int(input("Input index: "))
print(v)
v[k:len(v)-1:1] = v[(k+1):len(v):1]
v.pop()
print(v)
