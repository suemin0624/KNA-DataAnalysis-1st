# # 빈 set 만들기

# empty_list = []  # 빈 리스트
# print(type(empty_list))  # <class 'list'>
# empty_tuple = ()  # 빈 튜플
# print(type(empty_tuple))  # <class 'tuple'>
# empty_set = {}  # 빈 세트 -> x, 이건 빈 딕셔너리
# print(type(empty_set))  # <class 'dict'>
# # 빈 중괄호는 딕셔너리라는 다른 자료형으로 생성

# # 빈 셋은 무조건 set() 내장함수를 사용

# real_empty_set = set()  # 빈 세트
# print(type(real_empty_set))  # <class 'set'>

# # 값을 포함한 셋 만들기
# logs = ["S01", "S02", "S03", "S01", "S01"]
# # unique = {logs} # TypeError: cannot use 'list' as a set element (unhashable type: 'list') 타입 에러가 난다.
# # print(type(unique))

# # set() 사용
# unique = set(logs)
# print(type(unique))  # <class 'set'>
# print(unique)  # {'S02', 'S03', 'S01'}
# unique 셋에는 기존 중복되었던 S01이 한 번만 들어감
# 셋은 순서가 없는 값의 묶음
# 인덱스를 이용해서 접근 불가
# print(unique[0]) # TypeError: 'set' object is not subscriptable
# set에서 인덱스 사용 시 Error 발생

# # set에 바로 여러 값을 작성
# unique = set(["S01", "S02", "S03", "S01", "S01"])
# print(type(unique))
# print(unique)

# # set을 사용해서
# # 리스트에 들어있는 값의 종류 수를 알 수 있음
# print(len(unique))  # 3 출력

# # 셋에 값 추가하기
# # 셋.add(추가할 값)
# # 이미 있는 값을 추가할 경우 무시

# alerts = {"S01", "S02"}

# # 경고 상태인 S03이 추가될 경우
# # .add()를 사용해서 추가
# alerts.add("S03")
# print(alerts)


# # S01을 추가할 겨우
# alerts.add("S01")
# print(alerts)  # {'S03', 'S01', 'S02'}
# # S01이라는 값을 또 넣어도 무시하고 한 번만 저장
# # 그래서 독립적인 값을 저장하기에는 아주 편리함

# alerts = {"S01", "S02", "S03"}


# set에 특정 값 포함 여부 확인
# ["S01", "S02", "S03", "S01", "S01"]
# {"SO1", "S02", "S03"}
# 리스트와 셋 비교
# set 길이가 짧음 (중복을 제거하기 때문)
# set은 인덱스가 없음
# 순회 속도가 리스트보다 훨씬 빠름

# print("S01" in alerts)  # True

# # 조건문 활용

# if "S01" in alerts:
#     print("S01 정비 필요")

# # set을 정렬하면
# sorted = sorted(alerts)
# print(sorted)
# print(type(sorted))  # 리스트가 됨

"""실습 4"""

temps = ["S01", "S04", "S04", "S05", "S02", "S03", "S05", "S07"]
unique = set(temps)
print(sorted(unique))  # ['S01', 'S02', 'S03', 'S04', 'S05', 'S07']
print("종류 수:", len(unique))  # 종류 수: 6

# ====================================

# 집합 연산
hour_14 = {"WQR_01", "WQR_06", "WQR_07", "WQR_02"}
hour_15 = {"WQR_01", "WQR_07", "WQR_03", "WQR_09", "WQR_11"}

# 합집합
print(hour_14.union(hour_15))
print(hour_15.union(hour_14))
# {"WQR_01", "WQR_02", "WQR_03", "WQR_06", "WQR_07", "WQR_09", "WQR_11"}
# 짧게 정리: 1, 2, 3, 6, 7, 9, 11
print(hour_14)  # .union은 원본 셋에 변화 x

# | 연산자를 활용해 짧게 작성 가능
print(hour_14 | hour_15)

# 교집합
# union이랑 동일하게 두 코드는 똑같은 결과를 출력
# 앞뒤 순서가 결과에 영향을 미치지 않음
print(hour_14.intersection(hour_15))

# & 연산자 사용 교집합
print(hour_14 & hour_15)

# 3개의 print문은 공통으로 {"WQR_07", "WQR_01"}

# 차집합
# 차집합
# 순서에 따라 결과가 다름
# 앞에 작성된 셋에서
# difference의 인자로 전달된 셋에 있는 값들을
# 제외한 결과를 출력
print(hour_14.difference(hour_15))  # {02, 06}
print(hour_15.difference(hour_14))  # {03, 09}

# - 연산자 사용 차집합
print(hour_14 - hour_15)
print(hour_15 - hour_14)
# 차집합은 순서에 따라 결과가 다른 것 유의
# 14 -15dhk 15- 14는 다름
# 빼는 방형에 따라 값이 달라짐

""" 실습 5 """
line_1 = {"343", "754", "237", "958"}
line_2 = {"341", "237", "958"}
print(line_1.union(line_2))  # {'341', '958', '343', '754', '237'}
print(line_1.intersection(line_2))  # {'237', '958'}
print(line_1.difference(line_2))  # {'343', '754'}

""" 실습 6 """
yes = {"305", "416", "764", "156"}
tod = {"305", "215", "325", "156"}
print("신규 이상:", tod.difference(yes))  # 신규 이상: {'215', '325'}
print("지속 이상:", tod & yes)  # 지속 이상: {'305', '156'}
