t1 = ()
t2 = (1,)
t3 = (1,2,3)
t4 = 1, 2, 3
t5 = ('a', 'b', ('ab', 'cd'))

t1 = (1, 2, 'a', 'b')
# del t1[0]
print (t1)

# 인덱싱

print(t1[0])
print(t1[3])

# 슬라이싱
print(t1[1:])

#튜플 더하기
t2 = (3,4)
t3 = t1 + t2
print(t3)