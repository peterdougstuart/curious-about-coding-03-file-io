#  we can combine the values of two lists

a = [100.0, 200.0, 50.0, 60.0, 205.0]
b = [10.0, 20.0, 5.0, 6.0, 20.0]

c = []

# element-wise addition of a and b

# The long way infleixible way

c.append(a[0] + b[0])
c.append(a[1] + b[1])
c.append(a[2] + b[2])
c.append(a[3] + b[3])
c.append(a[4] + b[4])

for i in range(len(c)):
    print(c[i])

# The short way

c = []

for i in range(len(a)):
    c.append(a[i] + b[i])

for i in range(len(c)):
    print(c[i])

# concatenation of two lists

print("Concatenation of two lists")

d = a + b

for i in range(len(d)):
    print(d[i])
