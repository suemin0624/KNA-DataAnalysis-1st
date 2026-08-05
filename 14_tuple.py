# tuple: 값을 묶어주는 역할
# () 소괄호 안에 쉬표로 나누어서 여러가지 자료형의 값을 저장
# 그리고 마지막 값에는 꼭 ,를 붙여야 Python이 튜플로 인식을 함
# 짝지어진 값을 하나로 묶을 때 사용 가능한 자료형

sensor = ("모터온도", 78)
print("sensor: ", sensor)
print("type(sensor): ", type(sensor))

sensor = ("모터온도", 78)  # 괄호 있고, 끝에 쉼표 없음
print("sensor: ", sensor)
print("type(sensor): ", type(sensor))  # <class 'tuple'>

sensor = "모터온도", 78  # 괄호 없고, 끝에 쉼표 없음
print("sensor: ", sensor)
print("type(sensor): ", type(sensor))  # <class 'tuple'>

sensor = (
    "모터온도",
    78,
)  # 괄호 있고, 끝에 쉼표 있음
print("sensor: ", sensor)
print("type(sensor): ", type(sensor))  # <class 'tuple'>

sensor = 78  # 괄호 없고, 끝에 쉼표 없음
print("sensor: ", sensor)
print("type(sensor): ", type(sensor))  # <class 'int'>

sensor = (78,)  # 괄호 있고, 끝에 쉼표 있음
print("sensor: ", sensor)
print("type(sensor): ", type(sensor))  # <class 'tuple'>

# 쉼표 + 괄호 = 튜플
# ()가 있으면 튜플이다? -> 아님
# 요소 갯수
# 요소 2개 이상: 쉼표가 있다면 튜플
# 요소 1개: 쉼표 여부
# 요소 0개(빈 튜플): () 빈 괄호

# 튜플에서 많이 헷갈려하는 부분
# (1): int
# (1,): tuple

# (1, 2, 3, ) -> 가장 마지막에 쉼표를 붙여서 튜플임을 명시
# (1, 2, 3) -> 튜플 맞음

# 튜플의 인덱스
sensor = ("모터온도", 78)
print(sensor[0])  # 모터온도

# 튜플의 슬라이싱
s = ("a", "b", "c", "d", "e")
print(s[1:4])  # ('b', 'c', 'd')
# 슬라이싱한 결과는 소괄호에 감싸져 있음
# 튜플은 슬라이싱해도 결과가 튜플
print(type(s[1:4]))  # <class 'tuple'>

# 튜플 언패킹
# 튜플에 담긴 값을 변수로 한 번에 분리

# 복습) 복수의 변수 한 번에 선언하기
a, b, c = "a", "b", "c"
print(a)
print(b)
print(c)

unpacking = (
    1,  # 변수 One
    2,  # 변수 two
    3,  # 변수 three
)

unpacking = one, two, three
# one, two, three라는 알 수 없는 변수를
# unpacking 변수에 할당하겠다는 의미
# 동작 X

one, two, three, four = unpacking  # Error 발생
# unpacking이라는 변수에 담긴 튜플 내부의 값들을
# 할당 연산자 왼쪽 one, two, three 변수에 풀어서 담는다는 뜻
#  print("one:", one)
#  print("two:", two)
# print("three:", three)
#  print("four:", four)
# 튜플의 언패킹은 변수의 개수와
# 튜플에 담긴 값의 개수가 동일해야 함

# 리스트 언패킹이 가능할까?
one, two, three, four = [11, 22, 33, 44]
print("one:", one)
print("two:", two)
print("three:", three)
print("four:", four)
# 가능!

# ============================

tup = (
    "normal",
    "normal",
    "warning",
    "normal",
    "warning",
)

# 튜플의 길이
print(len(tup))  # 5

# 특정 값의 갯수 세기
print(tup.count("warnong"))  # 2

# 특정 값이 처음 나온 인덱스 찾기
print(tup.index("warning"))  # 2
# 찾고자 하는 값이 없으면 Error 발생
print(tup.index("Warning"))  # ValueError: tuple.index

# ==============================

# 튜플 리스트
# 리스트 안에 튜플을 담은 것을 표현
# for문으로 리스트를 사용해서 리스트 내부의 튜플에 접근하고
# 튜플에 담긴 값을 사용할 수 있음

# 언패킹을 사용해서 접근한 튜플 내부의 값을
# 변수에 바로 할당해서 접근

# ====================

temps_13 = [
    ("qox_001", 81),
    ("qox_002", 88),
    ("qox_003", 95),
    ("qox_004", 89),
]

warning = 90

for name, temp in temps_13:
    if temp >= warning:
        print("경고", name, "설비 온도 이상")

# 리스트 안의 튜플 갯수가 늘어나면
# for문에서 변수를 여러 개 작성하면 됨

tup_list = [
    ("일", "one", 1, "1"),
    ("이", "two", 2, "2"),
]

# for문에서도 언패킹 할 때는 무조건 튜플의 값 갯수와
# for문의 변수 갯수 통일
# 통일하지 않을 경우 Error 발생
for kor_str, eng_list, num, num_str in tup_list:
    print("kor_str:", kor_str, "eng_list:", eng_list, "num:", num, "num_str:", num_str)

# 튜플 리스트 정렬
# sorted()를 사용하여
# 튜플의 특정 값 기준으로 리스트를 정렬

# temps_13 = [
#            ("qox_001", 81),
#            ("qox_002", 88),
#            ("qox_003", 95),
#            ("qox_004", 89),
#            ]


hot = sorted(temps_13, reverse=True[1])
print(hot)
print("원본:", temp_13)

""" 실습 1 """
tup = ("모터 온도", 78)
print(tup)
print(tup[0])
print(tup[1])
temp, value = tup
print(temp, value)

""" 실습 2"""

sensors = [("sensor_1", 34), ("sensor_2", 53), ("sensor_3", 84)]
for sensor, value in sensors:
    print(sensor, value)
for sensor, value in sensors:
    if value > 90:
        print(sensor, "경고")

sensors = [
    ("모터 온도", 45, (2, 4)),
    ("설비 온도", 37, (3, 1)),
    ("펌프입력", 62, (7, 5)),
]
for sensor, value, tup in sensors:
    x, y = tup
    print(sensor, "위치:", x, y)
for sensor, value, tup in sensors:
    x, y = tup
    if x <= 5:
        print(sensor)
