odd = [1, 3, 5, 7, 9]

a = []
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is']
e = [1, 2, 3,['Life', 'is']]

print(a)
print(b)
print(b[2])
print(b[0] + b[2])
print(b[-1])
print(e[0])
print(e[-1][0])
print(e[3])

# 리스트 슬라이싱

a = [1, 2, 3, 4, 5]
print(a[0:2])

# 중첩된 리스트에서 슬라이싱하기

a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print(a[2:5])

print(a[3][:2])

a = [1, 2, 3]
b = [4, 5, 6]
print(b + a)

a = [1, 2, 3]
print(a * 3)