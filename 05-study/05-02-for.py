test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)

marks = [90, 25, 67, 45, 80] # 성적표

number = 0 # 학생에게 붙여 줄 번호
for mark in marks:
    number += 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)

marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks:
    number += 1
    if mark < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다. " % number)

a = range(1, 11)
print(a)

add = 0
for i in range(1, 11):
    add = add + i

print(add)

for i in range(2, 10):
    for j in range(1, 10):
        print(i*j, end=" ")
    print('')

# 리스트 컴프리헨션
a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num * 3)

print(result)

a = [1, 2, 3, 4]
result = [num * 3 for num in a if num % 2 == 0]
print(result)

result = [x*y for x in range(2,10)
              for y in range(1,10)]
print(result)

# for-else문
for i in range(5):
    print(i)
else:
    print("for 문이 정상 종료되었습니다.")

# for문 break 있으면 정상 종료 안됨.
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("for 문이 정상 종료되었씁니다.")

# enumerate 함수 활용
# 리스트의 인덱스와 함께 구하고 싶을 때 사용한다.
fruits = ['apple', 'banana', 'orange']
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

fruits = ['apple', 'banana', 'orange']
for i, fruit in enumerate(fruits, 5):
    print(f"{i}: {fruit}")

# zip 함수
names = ['홍길동', '김철수', '이영희']
scores = [85, 92, 78]
for name, score in zip(names, scores):
    print(f"{name}: {score}점")

names = ['홍길동', '김철수', '이영희']
korean = [85, 72, 99]
english = [90, 88, 95]
for name, kor, eng in zip(names, korean, english):
    print(f"{name}: 국어 {kor}점, 영어 {eng}점")