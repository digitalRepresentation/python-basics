# 정상 출력
food = "Python's favorite food is perl"
print(food)


# 비정상 출력
# food = 'Python's favorite food is perl'
# print(food)

# 따옴표
multiline = '''
Life is too short
You need python
'''

print(multiline)

# 문자열 길이 구하기

a = "안녕하세요 "
print(len(a))

# 문자열 인덱싱

a = "안녕하세요 파이썬을 사랑하는 사람입니다."
print(a[4])

print(a[:5])

print(a[5:])

print(a[3:4])

date = "20250831"
print(date[:4])
print(date[4:6])
print(date[6:])

a = "파이손"
a = a[:2] + '썬'
print(a)

# 문자열 포매팅
#print("I eat %d apples." % "ㅇㅇ")

# 문자열 바로 대입
print("I eat %s apples." % "ㅇㅇ")

number = 10
day = "three"
print("I ate %d apples. so I was sick for %s days." % (number, day))

print("Error is %d%%." % 98)

# 정렬과 공백
print("%5s" % "hi")

# 소수점 표현하기
print("%10.4f" % 3.42139234)

# 숫자 대입하기
print("I eat {0} apple." . format(3))

# 문자열 바로 대입하기
print("I eat {0} apples".format("five"))

count = 3
print(f"I eat {count} apples")

# 왼쪽 정렬
print("{0:>10}".format("hi"))

# 공백 채우기
print("{0:=^10}".format("hi"))

# f-string 기본적인 로그/결과 출력
accuracy = 0.9234
f1 = 0.8123
model = "XGBoost"

print(f"[INFO] Model={model}, Accuracy={accuracy: .2%}, F1={f1: .3f}")

# 소수점 표현하기
y = 3.42134234
print("{0:0.4f}".format(y))

name = '홍길동'
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')

age = 30
print(f'나는 내년이면 {age + 1}살이 ㅇ된다.')

d = {'name':'홍길동', 'age':30}
print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]} 입니다.')

# 문자 개수 세기
a = "hobby"
print(a.count("b"))

# 위치 알려 주기 1
a = "Python is the best choice"
print(a.find('b'))

print(a.find('ㅇ'))

# 위치 알려 주기 2
a = "Life is too short"
print(a.index('t'))

# print (a.index('ㅇ'))

# 문자열 삽입

print(",".join('abcd'))

# 문자열이 알파벳으로 되어 있는지 확인

s = "Python"
print(s.isalpha())

s = "Python3"
print(s.isalpha())

s = "Hello World"
print(s.isalpha())

s = "12345"
print(s.isdigit())

s = "1234a"
print(s.isdigit())

s = "12 34"
print(s.isdigit())