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

a = [1, 2, 3]
print(len(a))

print(str(a[2]) + "hi")

# 리스트 삭제

a[2] = 4
print(a)

del a[1]
print(a)

a = [1,2,3,4,5]
del a[2:]
print(a)

# 리스트 추가
a = [1,2,3]
a.append(4)
print(a)

a.append([5,6])
print(a)

# 리스트 정렬
a = [1, 4, 3, 2, 11]
a.sort()
print(a)

a = ["홍길동", "김진영", "서수길"]
a.sort()
print(a)

a.reverse()
print(a)

print(a.index("홍길동"))

# 리스트 요소 삽입
a = [1, 2, 3]
a.insert(2, 5)
print(a)

# 리스트 요소 제거
a.remove(2)
print(a)

# 리스트 요소 끄집어 내기
a = [1, 2, 3]
# 맨 마지막 요소를 꺼냄
a.pop()
print(a)

# 리스트에 포함된 요소 x의 개수 세기
a = [1, 2, 4, 1]
print(a.count(1))

# 리스트 확장
a = [1, 2, 3]
a.extend([4, 5, 6])
print(a)

b = [7, 8]
a.extend(b)
print(a)
