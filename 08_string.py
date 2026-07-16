# 작성하는 개발자가 보기 편한 방식으로 출력했을 때 문제
notice = """ 설비 점검 안내
1. 전원 확인
2. 센서 점검 """


print(notice)
# 설비 점검 안내
# 1. 전원 확인
# 2. 센서 점검
#
# 개발자가 보기 편한 방식으로 작성하면 생각과 다른 결과물이 나옴
# ''' ''' (삼중 따옴표를 사용할 시 그 내부의 모든 줄바꿈이 다 반영되어 출력)

# 탭
notice = """ 설비 점검 안내
1. 전원 확인
2. 센서 점검 """

print(notice)
# 삼중 따옴표는 탭도 그대로 유지됨

# =============================
# notice 이스케이프 사용해서 개선
# 이스케이프 문자
# \n -> 줄바꿈
# \t -> 탭(간격)
# \\ -> 역슬래시

notice = "설비 점검 안내\n1.전원 확인\n2.센서 점검"  # 줄바꿈으로 변경하기
print(notice)

tap = "이름\t상태"  # 탭으로 간격 변경하기
print(tap)

backslash = "이름\\상태"  # 백슬래시로 \ 끼워넣기
print(backslash)  # 이름\상태 -> 첫 번째 \는 이스케이프 문자라는 것을 알리는 용도

quotes = "It's me"  # 감싸는 따옴표와 str 내부 따옴표의 종류가 같을 때는 \를 사용
print(quotes)

# 빈 문자열과 공백 문자열의 차이
# "" 따옴표로 감싸졌지만 아무것도 작성되지 않았다먄 "빈 문자열"
# 빈 문자열은 글자 수 0, 길이 0
# " " 따옴표 안에 공백(스페이스바)이 있는 경우는 "공백 문자열"
# 공백(스페이스바)의 수 만큼 글자가 있고, 길이가 세어짐
# 빈 문자열과 공백 문자열은 컴퓨터에게 다른 값으로 인식됨
print("" == " ")  # False

""" 실습 1 """
# 설비 : PUMP_A
# 상태 : 정상
# 가동 : 1200
# 시간 : 2026-07-16

equip = "PUMP_A"
state = "정상"
run = 1200  # 숫자형이기 때문에 str로 감싸주기
hours = "2026-07-16"
card = "설비:" + equip + "\n상태:" + state + "\n가동:" + str(run) + "\n시간:" + hours
print(card)

# ========================
# 인덱싱 - 위치 번호로 글자를 하나 꺼내기
# 문자열[인덱스번호]
# 문자열에 첫 글자 인덱스는 0

word = "PYTHON"
print(word[0], word[3], word[5])  # P H N

# print(word[100]) -> IndexError
# word 변수에 저장된 문자열의 길이보다 큰 인덱스를 호출했기 때문

alpha = "abcdefghijklmnopqrstuvwxyz"
# 자기 이름 출력하기 (성 빼고)
print(alpha[-8] + alpha[-6] + alpha[12] + alpha[8] + alpha[13])  # sumin

# 음수 인덱스는 뒤에서부터 역순으로 순서 숫자가 붙음
# 주의사항은 음수 인덱스는 가장 마지막 글자가 -1부터 시작

# ===================================
print("=== 슬라이싱 ===")

# 슬라이싱 - 구간으로 잘라내기
# 문자열[시작:끝]
# 시작 인덱스 글자는 포함해서 출력
# 끝 인덱스 글자는 제외하고 출력

print("word[3:5] 결과:", word[3:5])  # HO
print("word[3:6] 결과:", word[3:6])  # HON
# 슬라이싱은 end가 포함되지 않고 출력하기 때문에 없는 인덱싄 6도 사용할 수 있음

# print(word[6])  # 인덱싱은 정확하게 마지막 인덱스까지만 쓸 수 있고, 넘치면 Error

# 슬라이싱 - start 생략
# 처음부터 특정 인덱스까지 구간을 뽑아내고 싶을 때 사용
print(word[:4])  # print(word[0:4])와 동일한 동작

# 슬라이싱 -end 생략
# 특정 인덱스부터 끝까지 구간을 뽑아내고 싶을 때 사용
print(word[2:])  # 2번 인덱스부터 끝까지 출력
# print(word[2:6])과 동일한 동작

# 슬라이싱 - 전체 생략
print(word[:])  # print(word[0:6])와 동일한 동작
# :을 사용하고  start와 end를 모두 생략하면 모든 인덱스의 구간을 뽑아냄

# 슬라이싱 - 음수 인덱스 사용
print(word[-3:])  # HON
# 음수 인덱스 작성 시 그냥 그 인덱스부터 정방향으로 출력함
print(word[:-1])  # PYTHO
# 처음부터 -1(5번 인덱스)를 제외한 구간을 뽑아냄
# 역순 아님 주의
# 음수 인덱스 사용 시 컴퓨터가 알아서 정수 인덱스 찾아 치환해서 동작

# PYTHON
# step으로 건너뛰기
# 문자열[시작:끝:간격(step)]
print(word[0:6:2])  # PTO
# PYTHON에서 첫 번째 글자는 명시했으니 거기서부터 출력
# step이 2이기 때문에 Y 뛰고, T (두번째 점프) 출력
# H 뛰고, 0 (두번째 점프) 출력
# N 뛰고 끝
# 두 글자를 뛰는게 아니라 두 번 뛰는 것 (뛴 그 자리 글자를 출력)

print(word[0:6:1])  # PYTHON 전체 출력

# start와 end를 생략하고 step만 입력
print(word[::2])  # PTO
# word 변수의 모든 글자를 두 칸씩 뛰면서 출력

# 순서 뒤집기
print(word[::-1])  # NOHTYP
# step은 인덱스가 아니고, 음수 입력 시 문자열의 순서를 뒤집음

# 슬라이싱은 범위를 벗어나도 오류가 발생하지 않음
print("범위를 벗어난 슬라이싱", word[0:100])  # PYTHON을 정상 출력

""" 실습 2"""
word = "bigdata"
print(word[:3])  # big
print(word[2:])  # gdata

""" 실습 3"""
word = "posco"
print(word[-3:])  # sco

""" 실습 4 """
word = "eclipse"
print(word[::2])  # elpe

""" 실습 5 """
word = "coffee"
print(word[::-3])  # ef

# ==========================
# 문자열의 길이 반환
# len()
# len(문자열)

# print(len("Hello World!"))  # 12 (공백도 모두 글자 취급)
# print(len(""))  # 0 (빈 문자열은 0 출력)

# var = "여러분 ~! 한 시간 남앗앙"
# print(len("이것도") - len("가능할까?"))
# # print()은 int를 반환하기 때문에 연산 가능

# print("abc 변수의 길이:", len(abc), "/ 마지막 인덱스 번호:", len(abc) - 1)

# # 음수 인덱스를 사용하지 않고 마지막 인덱스 문자를 뽑고 싶을 때
# print(abc[len(abc) - 1])

""" 실습 """
call_number = "01012345678"
print(len(call_number))  # 11

# =========================
print("=== in 활용 ===")

# in - 특정 문자가 문자열에 포함되었는지 여부 확인
# '여부'를 확인하기 때문에 True 또는 False (bool)으로 결과 반환
# 찾을 문자열 in 문자열
print("고장" in "설비 고장 발생")  # True
print("정상" in "설비 고장 발생")  # False
print("설비에서 고장" in "설비 고장 발생")  # False
print("설비에서 고장" in "설비에서 고장이 났습니다.")  # True

# not in - in의 정반대 동작
print("고장" not in "설비 고장 발생")  # False
print("정상" not in "설비 고장 발생")  # True
print("설비에서 고장" not in "설비 고장 발생")  # True
print("설비에서 고장" not in "설비에서 고장이 났습니다.")  # False

print(" " in "설비 고장 발생")  # True
# 따옴표로 감싼 공백(스페이스바)는 정말 "한 글자"로 취급

# ==========================
# print("=== count() ===")

# # .coount() - 문자열에 특정 글자의 수(int)를 반환
# # 문자열.count("찾을 글자")
# print("banana".count("a"))  # 3
# print("010-1234-1234".count("-")) # 2
# print("layla@spreatics.com.count("@)") # 1

word = "cellphone"
print(word.count("e"))  # 2

# =======================
print("=== find() ===")
# 전달받은 글자가 "첫 번째"로 나오는 위치 인덱스 반환
# 찾는 글자가 없다면 -1을 반환

email = "hong@company.com"
at = email.find("@")  # @ 위치의 인덱스인 4가 할당
user_id = email[:at]  # hong이라는 사용자의 아이디만 추출
print(user_id)
