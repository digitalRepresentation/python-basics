# a = input()
# print (a)

# print(input("안내_문구"))

# number = input("숫자를 입력하세요: ")
# print(number)

# 인풋은 모든 문자열을 string형태로 저장한다.
# print(type(number))

# age = input("나이를 입력하세요: ")
# age = int(age)
# print(age + 1)

# age = int(input("나이를 입력하세요: "))
# print(type(age))

# print 자세히 알기
a = 123
print(a)

a = "Python"
print(a)

a = [1, 2, 3]
print(a)

print("life" "is" "too short")

print("life"+"is"+"too short")

print("life", "is", "too short")

# sep 매개변수로 구분자
print("2025", "08", "17", sep="-")

print("점프", "투", "파이썬", sep=" TO ")

for i in range(10):
    print(i, end=' ')

# print("=== 간단한 계산기 ===")
#
# num1 = float(input("첫 번째 숫자를 입력하세요: "))
# num2 = float(input("두 번째 숫자를 입력하세요: "))
#
# # 계산 출력 결과
# print(f"{num1} + {num2} = {num1 + num2}")
# print(f"{num1} - {num2} = {num1 - num2}")
# print(f"{num1} * {num2} = {num1 * num2}")
#
#
# if num2 != 0:
#     print(f"{num1} / {num2} = {num1 / num2}")
# else:
#     print("0으로 나눌 수 없습니다.")

# f = open("새파일.txt", 'w')
# f.close()
#
# f = open("C:\doit\새파일.txt", 'w')
# f.close()

# f = open("새파일.txt", 'w', encoding='utf-8')
# for i in range(1, 11):
#     data = "%d번째 줄입니다.\n" % i
#     f.write(data)
# f.close()

print('')

# readline
# f = open("새파일.txt", 'r', encoding='utf-8')
# while True:
#     line = f.readline()
#     if not line: break
#     print(line)
# f.close()

# readlines
# f = open("새파일.txt", 'r', encoding='utf-8')
# lines = f.readlines()
# for line in lines:
#     print(line)
# f.close()

# 줄 바꿈(\n) 문자 제거하기
# f = open("새파일.txt", 'r', encoding='utf-8')
# lines = f.readlines()
# for line in lines:
#     line = line.strip() # 줄 끝의 줄 바꿈 문자를 제거한다.
#     print(line)
# f.close()

# read 함수
# f = open("새파일.txt", 'r', encoding='utf-8')
# data = f.read()
# print(data)
# f.close()

# 파일 객체를 for 문과 함께 사용하기
# f = open("새파일.txt", 'r',encoding='utf-8')
# for line in f:
#     line = line.strip()
#     print(line)
# f.close()

# 파일에 새로운 내용 추가
f = open("새파일.txt", 'a', encoding='utf-8')
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

# with 문과 함께 사용하기
f = open("foo.txt", 'w', encoding='utf-8')
f.write("Life is too short, you need python")
f.close()

with open('foo.txt', "w") as f:
    f.write("Life is too short, you need python")

# 함수 스코프: 함수 안에서 선언된 변수는 함수 밖에서 접근할 수 없다.
def my_function():
    func_var = "함수 안의 변수"

my_function()
# print(func_var) # 오류! 함수 밖에서는 접근 불가

# 블록 스코프: if, for, while, with 등의 블록 안에서 선언된 변수는 블록 밖에서도
# 접근할 수 있다.

# if문 블록의 예
if True:
    if_var = "if 블록 안의 변수"

print(if_var)

for i in range(3):
    loop_var = "반복문 안의 변수"

print(i)
print(loop_var)

with open ("test.txt", "w") as f:
    content = "Hello, Python!"
    f.write(content)

print(content)

with open("한글파일.txt", "w", encoding="utf-8") as f:
    f.write("안녕하세요, 파이썬!")

with open("한글파일.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)