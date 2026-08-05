# while은 특정 조건(횟수 X)이 False가 될 때까지
# 반복해야 하는 경우 사용

# 무한루프 유의
# count = 1

# while count <= 3:
# print(count)
# while문은 조건이 거짓이 되는 플래그를 꼭 세워야 함
# 무한루프 강제 종료: command + c

# while문 사용 체크리스트
# 1. 반복 전 변수(시작값) 존재 여부
# 2. 반복을 하다가 언젠가 False가 될 수 있는 종료 조건을 포함 여부
# 3. 변수가 거짓 방향으로 값이 변경되는지

count = 1  # 1번

while count <= 3:  # 2번
    # count = 0 # 반복문 안에 count 변수를 계속 0으로 재할당해서 에러
    print(count)
    count += 1  # 3번

# 반복 횟수를 모를 때 while
answer = 7
guess = int(input("맞혀 보세요:"))
while guess != answer:
    guess = int(input("맞혀 보세요:"))
print("정답")

""" 실습 1 """
plan = 234
start = 54
while start != plan:
    start = int(input("상태 값을 입력하세요.: "))
print("정답입니다!")

# break
# 반복을 그만 돌고 싶을 때
# 예 1) [1, 1, 3, 3, 2 ,1 ,1 ,1]
# 위 리스트를 돌면서 10 이상이 되면 중단하고 싶을 때
# 예 2) 사용자 입력값을 누적하다가 누적값이 총 15를 넘으면
# 종료하고 싶을 때
# break 사용 시 즉시 for문을 나감

input_sum = 0
while True:  # 조건만 보면 무한반복하는 코드
    user_input = int(input("값을 입력하세요. 값의 누적이 15를 넘으면 종료합니다:"))
    input_sum += user_input  # 누적값 업데이트

    if input_sum > 15:
        print("누적 합계:", input_sum, "입력을 종료합니다.")
        break  # 누적 합계가 15를 넘으면 반복 종료
print("break를 통해 while문을 나가면 이후 코드가 실행됨")

# 사용자 입력값을 확인만 하고 저장할 필요가 없는 경우
while True:
    # 변수 x는 반복을 돌 때마다 재할당되기 때문에 휘발되지만
    x = input("입력 (종료는 q를 입력하세요):")
    # 현재 입력값이 뭔지는 확인할 수 있음
    if x == "q":
        break
    print("입력받은 값", x)

# =========================
n = int(input("횟수: "))

for i in range(n):
    v = int(input("측정값: "))

    if v > 80:
        print("이상 발생")
        print("가동 쵯수:", n)
        break
    else:
        print("정상 처리")

# 실습 up down 게임
# 1~50 중 하나의 숫자를 정답으로 저장
# 사용자의 입력값 기준으로 정답이 up인지 down인지 출력
# 정답이 나오면 정답이고, 게임이 종료되었다고 출력

answer = 35
num = 0

while answer != num:
    num = int(input("수를 입력하세요: "))

    if num > answer:
        print("down")

    elif num < answer:
        print("up")
print("정답입니다. 게임을 종료합니다.")

# =============================

# 최댓값 찾기
first = int(input("1번째 입력값: "))

# 첫 번째 입력값은 자동으로 최댓값이 됨 (비교할 다른 값이 없기 때문)
max_value = first

# for문을 사용해서 사용자 입력을 4번 받고
# 입력 받은 값 중에서 가장 큰 값을 출력
for i in range(4):
    v = int(input(f"{i + 2}번쩨 입력:"))
    # 위에서 1번째 입력을 받고, i는 0부터 시작하기 때문에 2를 더해서 출력

    # max_value에는 현 시점 최댓값
    # v에는 방금 사용자가 입력한 값
    # max_value와 v의 값을 비교해 더 큰 값을 max_value에 재할당
    if v > max_value:
        max_value = v
        print("최댓값:", max_value)  # for 반복문 종료 후 최종 최댓값 출력

for i in range(3):
    value = int(input("값을 입력하세요.: "))
    if value < 5:
        max_value = value
        print("거짓 / 합계:", 0)

    elif value > 5:
        max_value += value
        print("참 /. 합계:", max_value)

total = 0
for i in [4, 7, 6]:
    if i > 5:
        total += i
    print("합계:", total)

count = int(input("반복 횟수: "))
found = False
for i in range(count):
    value = int(input("측정값: "))
    if value > 80:
        found = True
        break

if found:
    print("발견")

else:
    print("없음")


""" 실습 1 """
total = 0
for i in [34, 35, 28, 15, 29]:
    if i >= 30:
        total = i
        print("고온: ", total)

""" 실습 2 """
hours = [3, 8, 12, 6, 10, 4, 9]
for h in hours:
    if h >= 5 and h <= 10:
        print(h)

""" 실습 3 """

temps = [34, 35, 28, 15, 29]
sum = 0
count = 0
for i in temps:
    if i > 30:
        sum += i
        count += 1
print("평균", sum / count)
