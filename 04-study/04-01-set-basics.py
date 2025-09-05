s1 = set([1, 2, 3])
print(s1)

s2 = set("Hello")
print(s2)

s1 = set([1, 2, 3])
l1 = list(s1)
print(l1)
print(l1[0])

t1 = tuple(s1)
print(t1)

s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

# 교집합(積集合）
print(s1 & s2)

print(s1.intersection(s2))

# 합집합(和集合）
print(s1 | s2)

print(s1.union(s2))

# 차집합(差集合）
print(s1-s2)
print(s2-s1)

print(s1.difference(s2))
print(s2.difference(s1))

s1 = set([1,2,3])
s1.add(4)
print(s1)

s1.update([5,6])
print(s1)

# 특정 값 제거
s1 = set([1,2,3])
s1.remove(2)
print(s1)

s1 = set([1, 2, 3])
s1.discard(2)
s1.discard(4) # 없는 값이라도 오류가 발생하지 않음
print(s1)