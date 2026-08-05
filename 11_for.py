# 반복문은 동일한 작업을 특정 횟수만큼 반복해야 할 때
# 코드를 길게 쓰지 않고 반복시킬 수 있음

# for 변수 in range(횟수):
# 반복시킬 코드 (들여쓰기 한 칸 필수)
# 같은 코드를 복사 붙여넣기로 여러 번 작성하는 대신
# "N번 실행하라"는 의미

for i in range(3):
    print("안녕하세요!")  # range에 전달한 인자 3만큼 3번 반복
    # for문 안에서 i를 쓰지 않아도 됨 -> 목적이 "3번 반복"일 때

# 0부터 10까지의 숫자 자체가 필요하거나 출력할 때
for i in range(11):
    print(i)
    # i는 증가값을 지정하지 않는 이상 반복할 때마다
    # 자동으로 +1이 적용됨

# 0부터 10까지 짝수만 필요할 때
for i in range(0, 11, 2):  # range(시작, 끝, 증가값)
    print(i)  # 반복할 때마다 i가 2씩 자동으로 증가

# 1부터 10까지 홀수만 출력
for i in range(1, 11, 2):
    print(i)

# 역순으로 출력
for i in range(10, 0, -1):
    print(i)

# 10부터 1까지 짝수만 역순으로 출력
for i in range(10, 0, -2):
    print(i)

for i in range(0, 10, -2):
    print(i)
# 동작 안 함
# 시작값인 0에서 -2를 했을 때 끝 값이 포함되지 않아서 반복문 종료

N = int(input("끝 숫자를 입력하세요. :"))
for i in range(1, N + 1):
    print(i)

for i in range(2, N + 1, 2):
    print(i)

for i in range(N, 0, -1):
    print(i)

# range 함수에 전달한 두 번째 인자인 끝 값 11은 반복 횟수가 아님

# 실습) 369 게임
# 사용자에게 범위를 입력받아 3의 배수 출력하기
# 예)
# 사용자 입력값: 20
# 출력값: 3, 6, 9, 12, 15, 18
# for문, if문, 나머지연산자
# i % 3 == 0

n = int(input("범위를 위한 숫자를 입력하세요.: "))
for i in range(1, n + 1):
    if i % 3 == 0:
        print(f"입력한 1~{n}사이 3의 배수 출력: {i}")
    elif i % 5 == 0:
        print(
            f"입력한 1~{n}사이 5의 배수 출력: {i}"
        )  # else를 사용하는 경우에는 3의 배수가 아닌 수들을 모두 출력하게 됨
# 15와 같이 3의 배수이면서 5의 배수인 경우는 3의 배수라고만 출력

# 누적변수

total = 0
for i in range(1, 6):
    total += i
    # total = total + i
print("합계:", total)  # 합계: 15

for i in range(1, 6):
    total2 = 0  # 반복을 돌 때마다 새로이 변수에 값이 0으로 할당
    total2 += i
print("합계:", total2)  # 합계: 5

# total = 0 의 위치에 따라 합계가 달라짐

# 번외
if 3 == 3:
    hi = "안녕"
print(hi)  # 안녕
# Python에서는 if문 안의 변수도 어디서든 호출 가능한 변수로 선언됨

# 누적변수는 for문 밖에다가 선언하기

# 1~15 사이의 4의 배수만 누적
total3 = 0
for i in range(1, 16):
    if i % 4 == 0:
        total3 += i
print("1~15 사이의 4의 배수 누적 결과:", total3)  # 누적 결과: 24

# 개수 세기 패턴
count = 0
for i in range(1, 11):
    if i > 5:  # 5보다 큰 값만
        count += 1  # 만족할 때 1 증가
print("개수:", count)  # 5

# 평균 구하기 패턴
total = 0
count = 0
for i in range(1, 6):
    total += i
    count += 1  # ;은 한 줄에 여러 문장을 쓸 때 구분하는 기호
    # total += i
    # count += 1 과 같은 의미
if count > 0:
    print("평균:", total / count)  # 3.0

# 반복 변수 i 활용하기
for i in range(1, 4):
    print(i, "의 제곱은", i * i)  # 1, 4, 9

for i in range(3):
    print(i + 1, "번 항목")  # 1, 2, 3번

# enumerate (낱낱이 세다)
temps = [33, 23, 45, 32, 28]
for t in enumerate(temps):
    print(t)
# (0, 33)
# (1, 23)
# (2, 45)
# (3, 32)
# (4, 28)
# 범위를 지정하지 않아도 enumerate()에 전달한 리스트의 모든 요소 순환
# 문제는 형식이 (인덱스, 해당인덱스 요소값)로 출력
# enumerate를 사용할 때는 변수를 2개 전달

# for idx, t in enumerate(temps):
# 위와 같이 2개의 변수를 전달하면
# enumerate가 temps 리스트를 순회하면서
# 반환해준 (인덱스, 해당인덱스의값)을
# 각자 idx에 인덱스 값을 할당, t에 해당 인덱스의 값을 할당
# 두 개의 값을 바로 사용할 수 있게 해줌

temps = [33, 23, 45, 32, 28]
for idx, t in enumerate(temps):
    print(f"idx: {idx}, t: {t}")
# idx: 0, t:33
# idx: 1, t:23
# idx: 2, t:45
# idx: 3, t:32
# idx: 4, t:28

for a, b in enumerate(temps):
    print(f"a: {a}, b: {b}")

for idx, t in enumerate(temps):
    print(f"현재 인덱스: {idx}")
    print(f"{idx}인덱스의 값: {t}")
    print(f"{idx + 1}번째 반복 끝")

# 안녕의 인덱스 출력
# 이를 위해서는 값을 비교하기 위해 모든 리스트의 값이 필요
# 그리고 그 값의 인덱스를 알아야 출력
list = ["안녕", "hi", "hi", "안녕", "hi", "안녕"]

# 리스트의 모든 요소에 접근을 해야 하는 경우가 잦음
# 그래서 Python이 반복문에서 이를 쉽게 할 수 있도록
# enumerate라는 내장 함수를 제공
# enumerate은 리스트의 모든 요소를 앞에서부터
# 순서대로 하나씩 찍어가면서 접근
# 접근해서 각자의 인덱스와 그 값을 뽑아줌 -> 돌려주는 값은 2개
# 값을 2개 받으니 우리도 변수를 2개 준비하면
# 각 변수에 쏙쏙 값이 할당
# 돌려주는 순서는 인덱스, 값
# 그렇기 때문에 우리는 enumerate를 사용할 때
# for 뒤에 변수를 2개 전달
for index, value in enumerate(list):
    print(value)
# for value, index in enumerate(list): # 순서가 바뀌어도 같음

for i in range(len(list)):
    print(list[i])

# 사실 이 두 가지는 동일한 동작을 함

# 1~9단 사이 2의 배수 단만 구구단 출력
# 2, 4, 6, 8단만 출력
# range에 간격 전달
# if문 전달
for dan in range(2, 10):
    for su in range(1, 10):
        if dan % 2 == 0:
            print(dan, "x", su, dan * su)
