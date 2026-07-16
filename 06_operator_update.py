# 산술연산자
# + - * / //(몫) %(나머지) **(거듭제곱)
print(3 + 5)  # 8
print(10 - 4)  # 6
print(4 * 5)  # 20
print(20 / 4)  # 5.0 (나눗셈 결과는 항상 float)
print(7 // 3)  # 2
print(7 % 3)  # 1
print(2**5)  # 32

# ===================
# 연산 우선순위와 우선순위 지정
# **(거듭제곱) > *(곱하기) /(나누기) //(몫) %(나머지) > +(덧셈) -(뺄셈)
print(2 + 8 * 3)  # 8*3 연산 후 그 결과를 2와 더함
print((2 + 8) * 3)  # 괄호 안의 연산을 먼저한 뒤 곱하기 계산

# ===================
# 복합연산자

result = 3 * 5
print(result)  # 15

# 복합연산자는 사칙연산 모두 존재
# += : 기존 값에서 오른쪽 값을 더한 뒤 재할당
# -= : 기존 값에서 오른쪽 값을 뺀 뒤 재할당
# *= : 기존 값에서 오른쪽 값을 곱한 뒤 재할당
# /= : 기존 값에서 오른쪽 값을 나눈 뒤 재할당

result += 10  # 25
result -= 5  # 20
result *= 3  # 60
result /= 2  # 30.0 (나누기는 float 값을 가짐)
print(result)  # 30.0

# =============================
# 문자열 연산
print("안녕" + "하세요")  # 안녕하세요

# 만약 "안녕"과 "하세요" 사이에 공백을 1개 넣고싶다면
# 방법 1) , 사용 (, 사용하면 자동으로 한 칸 띄어쓰기)
print("안녕", "하세요")

# 방법 2) 안녕 뒤에 공백 추가
print("안녕 " + "하세요")

# 방법 3) 공백만 있는 문자열 더하기
print("안녕" + " " + "하세요")

# 문자열 곱하기
print("안녕" * 5)  # 안녕안녕안녕안녕안녕

# 문자열에 연산자를 사용할 경우 모두 이어져서 나옴

"""실습 1"""
print(3 + 5)  # 8
print(3 - 5)  # -2
print(3 * 5)  # 15
print(5 / 3)  # 1.6666666666666667
print(5 // 3)  # 1
print(5 % 3)  # 2
print(5**3)  # 125

"""실습 2"""
korean_score = 75
math_score = 100
english_score = 90

mean = (korean_score + math_score + english_score) / 3
# 평균 : 세 과목의 합을 먼저 구한 뒤 나누기 3을 해줌

print(mean)
area = 3**2  # 변의 길이 : 3
print(area)
volume = 3 * 4 * 5  # 가로 : 3, 세로 : 4, 높이 : 5
print(volume)

print("예상결과 :", "평균 :", mean, "넓이 :", area, "부피 :", volume)

# 문자열에 연산자를 사용할 경우 모두 이어져서 나옴

# =====================================
print("=== 비교연산자 ===")

# <(미만), >(초과), <=(이하), >=(이상), ==(같다), !=(다르다)

print(7 < 16)  # True
print(7 > 7)  # False
print(7 <= 7)  # True
print(7 >= 7)  # True
print(7 == 7)  # True
print(7 != 7)  # False

# 비교연산자를 사용해 문자열을 비교할 때 주의사항

# 1. 대소문자 구분
print("hello" == "Hello")  # False

# 2. 공백이 있어도 다르다고 판단
print("정상" == "정상 ")  # False

# 3. 부정연산자 != (not)
print("hello" != "hello")  # False
# 두 값이 동일한데 !로 인해서 값이 반대로 출력됨

# 변수에 문자열을 할당하고, 변수로 문자열 비교
hello = "hi"
print(hello == "hi")  # True
# 위 비교에서 hello는 따옴표로 감싸지지 않아서 "변수"로 취급
# 만약 hello를 "hello"와 같이 따옴표로 감싸면
# string으로 인식헤사 변수 취급을 하지 않음
# ex) "hello"와 "hi"를 비교하는 것

# 변수로 비교연산자 사용
num1 = 123
num2 = 456

print(num1 >= num2)  # False
# print(num1 >= "num2") # TypeError 발생
# TypeError : '>=' not supported between instances of 'int and 'str'

# ===============================

# and / or / not - 논리연산자
# and : 둘 다 True여야 True를 반환
print(5 == 5 and 7 == 7)  # True + True -> True
# 첫 번째 조건이 False라면 뒤에 조건은 확인 안 함
print(5 == 7 and 7 == 7)  # False + True -> False
print(5 == 5 and 7 != 7)  # True + False -> False
# 위 코드는 가능하면 print(7 !== 7 and 5 = 5) 순서로 작성
# or : 하나라도 True라면 True 반환
print(5 == 5 or 7 == 7)  # True + True -> True
print(5 == 7 or 7 == 7)  # False + True -> True
# or은 첫 번째 조건이 True라면 뒤에 조건은 확인 안 함
print(5 == 5 or 7 != 7)  # True + False -> True

# not : 값을 반대로 뒤집음
print(not True)  # False
print(not 5 == 5)  # False
# 5 == 5를 연산하여 True를 반환
# nor True로 동작해서 True를 뒤집어 False를 반환
# 반환받은 False라는 값을 print가 터미널로 출력

"""실습 3"""
print(4 == 23)  # False
print(4 != 23)  # True
print(4 > 23)  # False
print(4 < 23)  # True
print(4 >= 23)  # False
print(4 <= 23)  # True

print(4 == 12.1)  # False int와 float을 같이 연산해도 오류 발생x
print(4 != 12.1)  # True
print(4 > 12.1)  # False
print(4 < 12.1)  # True
print(4 >= 12.1)  # False
print(4 <= 12.1)  # True

"""실습 4"""
temp = 85
print(temp >= 60 and temp <= 90)  # True

pre = 5
print(pre >= 3 and pre <= 7)  # True

print(temp >= 60 and temp <= 90 and pre >= 3 and pre <= 7)  # True

"""실습 5"""
stock = 122
stock += 5  # 입고
print(stock)  # 재고 : 127
stock -= 7  # 출고
print(stock)  # 재고 : 120
stock += 3  # 반품
print(stock)  # 재고 : 123

total = 344
defect = 56
print(defect / total * 100)  # 불량률 : 16.27

run_time = 21
total_time = 24
print(run_time / total_time * 100)  # 가동률 : 87.5

runtime = 500
print(runtime // 60)  # 시간 : 8

print(runtime % 60)  # 분 : 20
