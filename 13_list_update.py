temps = [1, 5, 2, 7, 4, 8, 10, 3]
doubled = []

for t in temp:
    doubled.append(t * 3)

print(doubled)

# 조건에 맞는 값으로 세 리스트 만들기

# temps = [1, 5, 2, 7, 4, 8, 10, 3
high = []
low = []

for t in temps:
    if t < 5:
        low.append(t)
    else:
        high.append(t)

print("high:", high)
print("low:", low)

# 복습) sort(): 원본 배열을 오름차순으로 정렬해줌
# 하지만 변환해주지 않기 때문에 print로 바로 찍으면 None 출력
print(low.sort())

# 정렬된 배열을 출력하고 싶다면 아래처럼
low.sort()
print(low)

""" 실습 4 """
temps = [32, 19, 25, 13, 36]
empty = []
for i in temps:
    if i > 30:
        empty.append(i)
print(empty)
print("개수:", len(empty))

# 정렬된 배열을 출력하고 싶다면 아래처럼
low.sort()
print(low)

""" 실습 5 """
# 방법 1)
c = [35, 24, 42, 29, 25]
empty = []
for i in c:
    f = c * 1.8 + 32
    empty.append(f)
print(empty)

# 방법 2)
c = [35, 24, 42, 29, 25]
empty = []
for i in c:
    empty.append((i * 1.8 + 32))
print(empty)

# 리스트 안의 리스트
rows = [["펌프", 25], ["모터", 32], ["압축기", 28]]
print(rows[0])
print(type(rows[0]))
print(type(rows))
# 중첩된 리스트 안의 값에 접근
print(rows[1][1])
# 1. rows[1]을 찾음 -> ["모터", 32]
# 2. print(["모터", 32][1]) -> [1] 앞의 리스트에서 1번 인덱스 값에 접근
# 3. print(32) -> 32 출력
# 중첩된 리스트 내부의 값은 대괄호를 여러 번 이어서 접근

# 리스트 안의 리스트 온도값만 출력하기
for row in rows:
    print(row[0], "온도", row[1])  # 펌프 온도 25...
    # rows는 리스트를 담고 있는 큰 리스트
    # row는 rows 안에 있는 작은 리스트 예)

""" 실습 6 """
temps = [35, 24, 42, 29, 25]
sum = 0
empty = []
for i in temps:
    sum += i
    empty += temps
    print("전체 평균:", sum / len(temps))
    if i > 30:
        sum += 30
        empty.append(i)
        print("고온 개수:", len(empty))
        print("고온 평균:", sum / len(empty))
