a = 1
b = "python"
c = [1, 2, 3]

# 올바른 변수명
name = "홍길동"
age = 25
user_name = "gildong"
userName = "gildong"
_private = "비공개"
count1 = 10

# 잘못된 변수명
# 1name = "홍길동" # 숫자로 시작
# user-name = "홍길동" # 하이픈 사용
# if = 10 # 예악어 사용

# 메모리 얇은 복사 하는 방법

a = [1, 2, 3]
b = a[:]
a[1] = 4
print(a)
print(b)

from copy import copy

a = [1, 2, 3]
b = copy(a)
# b = a.copy() #어느것도 됨
print(b is a)

# 변수 만드는 방법
a , b = ('python','life')
print(a, b)

(a, b) = 'python', 'life'
print(a, b)

[a, b] = 'python', 'life'

a = b = 'python'

a = 3
b = 5
a, b = b, a
print(a, b)

if a == 5:
    print("test");
        #print("test");