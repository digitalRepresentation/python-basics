def add(a, b):
    return a + b

print(add(5, 6))

# 반환 값이 없는 함수
def add(a ,b):
    print("%d, %d의 합은 %d입니다." % (a, b, a+b))

add(4,5)

# 아규먼트를 지정해주기
add(b=6, a=4)

# 인수 제한 해제
def add_many(*args):
    result = 0
    for i in args:
        result += i
    return result

result = add_many(1, 2, 3, 5, 5)
print(result)

def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result += i

    elif choice == "mul":
        result = 1
        for i in args:
            result *= i
    return result

result = add_mul('add', 1,2,3,4,5)
print(result)

result = add_mul('mul', 1,2,3,4,5)
print(result)

# 키워드 매개변수, kwargs
# kwarge를 사용할 때  딕셔너리 형태로 사용할 때는**를 붙인다.
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1, b=2)
print_kwargs(name='foo', age=3)
print_kwargs(name='홍길동', age=25, city='서울', job='개발자')

def create_profile(**info):
    print("=== 프로필 정보 ===")
    for key, value in info.items():
        print(f"{key}: {value}")

create_profile(이름='김철수', 나이=30, 직업="프로게이머", 취미='독서')

def add_and_mul(a,b):
    return a+b, a*b

print(add_and_mul(3,4))

result1, result2 = add_and_mul(3,4)
print(result1)
print(result2)

def say_myself(name, age, man=True):
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살입니다." % age)
    if man:
        print("남자입니다")
    else:
        print("여자입니다.")

say_myself("김진영",31)

# 함수 안에서 선언한 변수의 효력 범위
a = 1
def vartest(a):
    a += 1

print(vartest(a))
print(a)

# 함수 안에서 함수 밖의 변수를 변경하는 방법
a = 1
def vartest(a):
    a += 1
    return a

a = vartest(a)
print(a)

# global 명령어 사용하기
a = 1
def vartest():
    global a
    a = a+1

vartest()
print(a)

# 리스트나 딕셔너리는 함수에서 변경이 가능하다
def change_list(my_list):
    my_list.append(4)

a = [1, 2, 3]
change_list(a)
print(a)

# lambda 예약어
add = lambda a, b: a+b
result = add(3, 4)
print(result)

# 함수의 독스트링(Docstring)
def add(a, b):
    """
    두 숫자를 더하는 함수

    Parameters:
    a (int, float): 첫 번째 숫자
    b (int, float): 두 번째 숫자

    Returns:
    int, float: 두 숫자의 합
    """

    return a + b

# 독스트링 확인하기
print(add.__doc__)
