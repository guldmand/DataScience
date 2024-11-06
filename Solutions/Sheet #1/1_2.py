# 1.2
i = 3
f = 2.19

# 1.2.a
a = i + 3 * i
print(type(a))  # int

# 1.2.b
b = (i + 3.0) * i
print(type(b))  # flaot

# 1.2.c
c = 1 - i + 2
print(type(c))  # int

# 1.2.d
d = 3.0 + i * i
print(type(d))  # float

# 1.2.e
e = 9**0.5
print(type(e))  # float

# 1.2.f
f = i**2 // 2
print(type(f))  # int

# 1.2.g
g = i**2 // f
print(type(g))  # int

# 1.2.h
h = i**f // i
print(type(h))  # int

# 1.2.i
i = i / i - 2
print(type(i))  # float

# 1.2.j
j = i / f * f
print(type(j))  # float
