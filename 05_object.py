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

print(num, type(num))
print(num, ">>>", type(num))  # 123 >>> <class 'int'>
