# int - 정수형
# 소수점 없이 딱 떨어지는 수
count = 3
age = 29
tall = 173

# 0과 음수도 정수에 포함됨

temp = -30
zero = 0

# =====================

# float - 실수
# 소수점이 붙은 숫자
# 5.0처럼 딱 떨어지는 수이지만 소수점이 없다면 무조건 float

tired = 99.99999
height = 17.2

# ====================

# str - 문자열
# 따옴표에 감싸져있는 모든 닶

hello = "안녕하세요~!"
emoji = "@ㅅ@"
empty = ""  # 따옴표만 있고 아무것도 작성되지 않아도 str (빈 문자열)
fake_num = "12345"
fake_num2 = "5.0"
# 따옴표가 ""와 '' 둘 다 사용할 수 있는 이유는
# 문자열 안에 따옴표가 필요한 경우가 있기 때문
# 이럴 경우 사용하지 않는 따옴표로 쌍을 맞춰 가장 바깥에 감싸줘야 함
illit = "It's me"

# ===============================

# bool - 불리언형
# True 또는 False만
# 첫 글자는 대문자, 따옴표 없이 작성

ok = True
no = False


# 비교할 경우 bool로 출력
print(100 < 5)  # False
print(5 == 5)  # True

# ==========================
print("=== type() ===")  # 터미널에서 출력 결과 확인할 때 가독성을 위한 코드

# type()  - 자료형 확인
# type(확인하고자 하는 것) > 입력한 것의 자료형을 알려줌

type(5)  # 터미널에서 확인 불가 > print하지 않았기 때문

print(type(5))
print(type("센서A"))  # <class 'str'>
print(type(True))  # <class 'bool'>
print(type(3 > 2))  # <class 'bool'>
# 1. print 함수의 내부를 확인
# 2. print 한수에 또 함수가 있는 것을 확인하고 type 함수의 내부를 확인
# 3. type 함수의 내부에 연산자가 있는 것을 확인하고 연산 진행
# 4. 3 > 2의 연산 결과는 True이기 때문에 type(True)로 바뀜
# 5. type(True)의 결과인 <class 'bool'>이 print로 안해 터미널에 출력

print(3, type(3))  # 3, <class 'int'>

num = 123
fake_num = "123"
str = "문자열"
ok = True

# 값과 결과를 동시에 확인
print(num, type(num))

# 내가 터미널에서 출력된 결과 중에서
# type()을 사용해서 출력된 자료형을 쉽게 확인 할 수 있는 방법
print(num, ">>>", type(num))  # 123 >>> <class 'int'>
print("num :", type(num))  # 123 : <class 'int'>

# ============================
print("=== 자료형마다 동작이 다른 것 확인하기 ===")

print(3 + 5)  # 8 (int) > 숫자끼리 더하기는 계산
print("3" + "5")  # 35 > str끼리 더하기는 이어 붙이기
print("안녕하" + "세요")  # 안녕하세요

# ================================
print("=== 자주 하는 실수 ===")

print(0.1 + 0.8)  # 0.9
# 위 상황에서는 출력되지만
# 가끔 컴퓨터 내부 연산 과정에서 아주 작은 오차가 발생하는 경우도 있음

# 작은 오차 해결법
# round() 사용해서 반올림
print(round(0.1 + 0.8, 2))  # 소수 둘째 자리를 반올림해서 0.9 출력

# str과 int/float은 덧셈 불가
# print("123" + 456)  # TypeError 발생

print(10 / 2)  # 5.0 (나눗셈은 결과가 딱 떨어져도 무조건 float)
print(type(10 / 2))  # <class 'float'>

"""실습 1"""
age = 24  # int
print(age)
print("age")
tall = 169.1  # float
print(tall)
print("tall")
korea = "서울"  # str
print(korea)
print("korea")
YES = True  # bool
print(YES)
print("YES")

"""실습 2"""
age = 24  # <class 'int'>
print(type(age))
tall = 169.1  # <class 'float'>
print(type(tall))
korea = "서울"  # <class 'str'>
print(type(korea))
YES = True  # <class 'bool'>
print(type(YES))

"""실습 3"""

# 100의 자료형 예측 -> int
print(type(100))  # <class 'int'>
# 100.0의 자료형 예측 -> float
print(type(100.0))  # <class 'float'>
# "100"의 자료형 예측 -> str
print(type("100"))  # <class 'str'>
"""실습 4"""
print(3 + 5)  # 8
print("3" + "5")  # 35
print("35" + "45")  # 3545

"""실습 5"""
# 3 > 2 인지 예측
print(3 > 2)  # True
print(type(3 > 2))  # <class 'bool'>

# 5 == 5 인지 예측
print(5 == 5)  # True
print(type(5 == 5))  # <class 'bool'>

"""실습 6"""
age = 24
print(age, type(age))  # 24 <class 'int'>

height = 112.4
print(height, type(height))  # 112.4 <class 'float'>

friend = "79"
print(friend, type(friend))  # 79 <class 'str'>

"""실습 7"""
device_temp = 42.3  # float

check_count = 3  # int

device_name = "google"  # str

is_normal = True  # bool
