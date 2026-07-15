# 변수 : 값에 이름을 붙여 다시 꺼내 쓰는 도구
# 같은 값을 이름 하나로 재사용
# 값이 바뀌어도 한 곳만 수정
# 변수이름 = 값 (오른쪽 값을 왼쪽 이름에 저장하라는 명령)

# 변수 선언 방법
# 변수이름 = 값
# 오른쪽 값을 왼쪽 이름에 "저장"하라는 코드
# temp = 36  # 숫자로 저장하고 싶다면 따옴표 금지
name = "센서 A"  # 글자는 무조건 따옴표로 감싸기

print(temp)  # 36
print("temp")  # temp

# =은 "같다"가 아니라 "저장"하는 것
# 비교는 ==을 사용

# ===================================
print("=== 변수 사용 활용 ===")

x = 5
x = x + 5
# 변수를 "재활용"할 때 변수 기존 자신의 값을 활용할 수 있음
# 변수에 할당할 때 오른쪽을 먼저 계산한 뒤 x에 값을 재할당
print(x)  # 10

# y = y + 5  # 오류 발생 (y가 선언되지 않았기 때문)

# ====================================
print("==== 재할당 =====")

print("재할당하기 전 temp:", temp)
# temp = 15  # 위에서 할당했던 36이라는 값을 15로 재할당(수정)
Temp = 15  # temp와 다른 변수로 동작
print("temp:", temp)
print("TempL", Temp)

# 재할당은 지금까지 실행된 가장 마지막으로 저장된 값을 불러옴
# print(score)  # NameError 발생
score = 10
print(score)  # 10
score = 20
score = 30
print(score)  # 30

# =====================================
print("==== 값 복사 =====")

a = 10
b = a  # b 변수에는 10이 저장 (저장할 때의 그 순간의 a 값을 b에 복사)
a = 100  # a 변수를 재할당해도
print(b)  # 10 b 변수의 값은 10이 그대로 유지됨

# ======================================
print("===== 여러 변수 한 번에 선언 및 할당 ======")

# 형식: 변수1, 변수 2, ... = 값1, 값2, ... > 변수와 값이 갯수가 같아야 함
width, height = 10, 20  # widthsms 10, height는 20이 할당됨
print("width", width, "height", height)

# x, y, z = 10, 20  # 변수 3개, 값 2개 > ValueError 발생

# =======================================
print("====== 주석으로 변수 설명 ======")

# temp = 25  # 온도(섭씨)
count = 3  # 센서 개수
# temp = 1000000000 # 주석처리된 코드는 동작하지 않음
print(temp)  # 25

# 실습 1
# temp = 25
# print(temp)

name = "센서A"
print(name)

# 실습 2
# temp = 25
# print(temp)
# temp = 30
# print(temp)
temperature = 25
print(temperature)

name = "센서A"
print(name)

# 실습 3
my_number = 624
print(my_number)

mood = "그냥 그럼"
print(mood)

# 실습 4
age = 24
label = "나이"
print(label)
print(age)

# 실습 5
x = 10
print(x)

x = x + 5
print(x)

x = x * 2
print(x)

# 실습 6
a = 100
b = a
a = 999
print(a)
print(b)

# 실습 7
# (오류 발생)
print(temp)
score = 90
print(Score)

# (오류 고치기)
temp = 25
print(temp)
score = 90
print(score)

# 실습 8
temp = 25 # 온도(섭씨)
count = 3 # 센서 개수
# temp = 100  # 실행 안 됨
print(temp) # 25

# 실습 9
x = 5
x = 10
x = x + 1
print(x) # 11

# 실습 10
name = "이수민"
temp = 38
print("이름")
print(name)
print(temp)

# 실습 11
a = 24
age = 24
device_temp = 34
print(age)
print(device_temp)

# 실습 12

# 한 줄에 변수 세 개 만들기
x, y, z = 14, 54, 33

# 한 줄에 변수 두 개 만들기
width, height = 43, 76
print(width)
print(height)