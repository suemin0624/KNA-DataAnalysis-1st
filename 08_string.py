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

# SQE-00Q8이라는 설비의 SQE만 뽑아내기 (find와 슬라이싱 사용)
sqe = "SQE-00Q8"

# sqe_index = sqe.find("SQE")
# print(sqe_index) # 0

sqe_index = sqe.find("-")
print(sqe_index)  # 3
sqe_fin = sqe[:sqe_index]  # sqe[0:3] > SQE
print(sqe_fin)  # SQE

# find에서 했던 SQE 뽑아내기 실습 # index 사용으로 바꾸기
sqe_index = sqe.index("-")

# sqe_find = sqe.index("/") # /가 없으니 Error 나고 중단
# ===============================================

email = "suemin0624@gmail.com"
at = email.index("@")  # 5
print(email[0:at])  # suemin0624
print(email[:at])  # 시작 번호가 0이라면 start 생략 가능
print(email[at:])  # 시작 번호가 0이라면 start 생략 가능
print(email[at + 1 :])  # 끝까지 출력하고 싶고, 뒤에 몇 글자가 있는지 모르니 생략

# ====================================

# 문자열에서 특정 문자열의 갯수 세기

str = "a, b, c, d, e, a, a"

# a의 갯수 세기
print(str.count("a"))  # 3

# ,의 갯수 세기
print(str.count(","))  # 6

print(str.count(", "))  # 5 # count로 찾는 문자열과 완전히 동일해야 갯수를 셈

# ==========================
print("=== startswith() ===")

# 특정 문자열로 시작하는지 검사
# True/False (불리언)

# EQP로 시작하는지 검사하기
print("EQP-001".startswith("EQP"))

# 변수 활용
eqp = "EQP"
print("EQP-001".startswith(eqp))
# 주의사항) 변수명은 따옴표 감싸기 금지

# ============================
print("=== endswith() ===")

# 특정 문자열로 끝나는지 확인
# True / False로 변환

str2 = "월요일입니다 ! 여러분은 할 수 있어요!"

print(str2.endswith("!"))  # True
print(str2.endswith("요!"))  # True
print(str2.endswith("음!"))  # False
print(str2.endswith("월요일입니다 ! 여러분은 할 수 있어요!"))  # True
print(str2.endswith("월요일입니다 !     여러분은 할 수 있어요!"))  # False
print(str2.endswith("월요일입니다 ! 여러분은 할 수 있어요! "))  # False
print(str2.endswith(" 월요일입니다 ! 여러분은 할 수 있어요!"))  # True

print(str2)  # 원래 할당한 문자를 결과로 출력

""" 실습 startswith / endswith 학습 """
file = "sensor_log.csv"
print(file.startswith("sensor"))  # True
print(file.endswith(".csv"))  # True

# =================================
print("=== 값은 객체다 ===")

print(type("잊어먹으면 안돼!!!"))  # <class 'str'>
print(len("이렇게 썼죠??"))
# endswith와 len의 차이는?
# endswith는 .으로 연결
# .으로 연결하는 이런 도구들은 "메서드"
# 문자열이나 int, float처럼 특정 자료형(객체) 내부에 포함된 기능
# len은 . 사용 안 함
# () -> 함수
# len과 같이 개발자가 직접 선언하지 않은 기본 제공 함수 "내장 함수"

# "str.startswith("s)"
# 123.startswith(1)
# .으로 사용하는 메서드들은 특정 자료형(객체 타입)마다 다름
# int 자료형의 객체에는 startswith라는 메서드가 없음

# print(len(123)) # len 내장함수는 길이를 반환하기 때문에 int 자료형 사용 불가
# 메서드 : 문자열마다 딸린 정리.검색 기능 (대문자 바꾸기, 공백 떼기)

# ===================================
# 재할당 복습
num = 1
num = num + 1  # 2
num += 1  # 3
# += 은 복합할당연산자 원래 내 자신의 값에 다음 오는 연산자와 값을 적용해서 재할당

# =====================================
str3 = "abcdefg"
print(str3)  # abcdefg

str3.upper()  # ABCDEFG > 반환은 대문자인데, 값에 재할당은 X
print(str3)  # abcdefg > 기존 str3의 값인 소문자를 그대로 출력

# 앞으로 계속 대문자로 변환한 값을 사용하고 싶다면
# 변수의 재할당
# 변수 재할당에서 변수 스스로를 부르는 것이 가능
# 재할당해서 변수 스스로 값을 부르려면 무조건 "재할당"이어야 함
str3 = str3.upper()

# str4 = str4.upper()
# 최초 변수 할당 시에는 저장된 값이 없어서
# 변수 스스로 값을 불러와 할당 불가능

prepare = "ready"
start = prepare.upper()
print(start)  # READY

# ===========================
user_name = "kim chul soo"

# capitalize는 문자열의 첫 글자만 대문자로 변환
print(user_name.capitalize())  # Kim chul soo

# title은 띄어쓰기 기준으로 각 단어의 첫 글자들을 모두 대문자로 변환
print(user_name.title())  # Kim Chul Soo

# '를 사용한 경우 다른 단어로 인식
print("i'm full".title())  # I'M Full
print("i'm full".title())  # I'M Full

""" 실습 1 """
print("ABC".isupper())  # True
print("abc".isupper())  # False
print("Abc".isupper())  # False
print("ABC".islower())  # False
print("abc".islower())  # True
print("Abc".islower())  # False

""" 실습 5 """
file = "Sensor_LOG.csv"
new_file = file.lower()
print(new_file.startswith("sensor"))  # True
print(new_file.endswith("csv"))  # True

""" 실습 2 """
a = "WARNING"
b = a.lower()
print(b)  # warning

# 공백 제거
# .strip(): 앞과 뒤의 모든 공백 제거 (중간 띄어쓰기는 그대로 유지)
# .lstrip(): 왼쪽 공백만 제거
# .rstrip(): 오른쪽 공백만 제거

raw = "  정상   "
print(raw.strip())  # "정상"
print(raw.lstrip())  # "정상   "
print(raw.rstrip())  # "   정상"

# 문자열의 가운데 공백은 strip으로 지우지 못 함
print("   정   상   ".strip())  # "정   상"

print(raw)  # "   정상   "
# strip은 재할당이나 새 변수에 할당하지 않는 이상 휘발

# strip으로 문자 제거
str4 = "===정상==="
print(str4.strip("="))  # 정상
# 인자로 전달한 양 끝의 =이 모두 지워짐

str5 = "=정상========="
print(str5.strip("="))  # 정상
# 갯수 상관 없이 인자로 전달한 문자를 무조건 삭제

print(str5.strip("= "))  # 정상
# strip 자체가 공백을 지우는 것이기 때문에
# 공백 상관없이 양 끝의 해당 문자열 삭제

str6 = "==정==상===="
print(str6.strip("="))  # 정==상
# 글자 중간에 있는 문자열은 건드리지 않음


""" 실습 7 """
a = " 가동중 "
print(a.strip())  # 가동중

# 메서드 연결해서 쓰기 (체이닝)
# 메서드 뒤에 또 메서드를 점으로 이어 붙이기
# ex) text.strip().lower()
# 읽는 순서는 왼쪽에서 오른쪽으로

# 체이닝 X
raw = "      NORMAL      "
step1 = raw.strip()  # "NORMAL"
step2 = step1.lower()  # "normal"

# 체이닝 X, 기존 변수에 재할당
raw = raw.strip()  # "NORMAL"
raw = raw.lower()  # "normal"
# 체이닝 O
chain = raw.strip().lower()  # "normal"

# 기존 변수에 재할당도 가능
raw = raw.strip().lower()

# 변수에 할당하지 않고 사용 가능
print(raw.strip().lower())

""" 실습 11 """
str = "     Warning     "
print("[" + str.lower().strip() + "]")  # "[warning]"


str1 = str.lower()
print("[" + str1 + "]")  # "[   warning   ]"
str2 = str1.strip()
print("[" + str2 + "]")  # "[warning]"


# strip() 메서드에 인자로 들어가는 문자열은
# 완전히 동일하지 않아도 전부 삭제
str8 = "aaab 이렇게? cd"
print(str8.strip("abcd"))  # " 이렇게?"
print(str8.strip("abcd "))  # "이렇게?"

# 지금 출력 결과는 " 이렇게? " 이렇게 나오고 있어서
# 생각했을 때 ==처럼 정확하게 "abcd" 순서가 아니라
# strip이 안 될 줄 알았는데 실험 결과를 보니 순서랑 상관없이
# 인자로 전달한 문자열에 해당하는 글자가 확인하는 문자열 양 끝에
# 하나라도 있으면 동작하는 것 같아
# 내가 이해한 게 맞아?
# 그렇다면 왜 이렇게 동작하는 거야?

# ====================================
print("=== replace() ===")

# 특정 문자열을 제거하거나 치환할 때 사용
# .replace("바꾸고 싶은 문자열", "바꿀 문자열")
# 제거할 때는 인자의 두 번째를 ""(빈 문자열)로 작성
print("정 상 작 동".replace(" ", ""))  # 정상가동 (중간 공백 제거)
print("   정     상  가동".replace("  ", ""))  # 정상가동 (모든 공백 제거)
print(
    "   정     상  가동".replace("   ", "")
)  # 정 상 가 동 (공백이 2칸 붙어있는 경우만 제거)
# " 정 상 가 동"
print("고장".replace("고장", "fault"))  # fault
print("고장".replace("고", "fault"))  # fault장

# 단어 치환
str9 = "설비 정상 가동"
print(str9.replace("정상", "점검"))  # 설비 점검 가동

# replace() 체이닝
num = "   010-1234-1234   "
num = num.replace(" ", "").replace("-", "")
print(num)

# ======================================
# 문자열 자르기
# 결과는 대괄호에 감싸진 "리스트" 자료형
# 리스트는 순서가 있기 때문에 왼쪽에서부터 0으로 시작하는 인덱스가 자동 생성

drinks = "에스프레소 아메리카노 카페라떼"
print(drinks.split())  # 인자를 보내지 않음
# "'띄어쓰기"를 기준으로 나뉘어진 세 개의 문자열을 대괄호에 감싸서 반환

# 구분자를 특정하고 싶은 경우
fruits_list = "딸기, 거봉, 키위, 사쿠란보"  # 문자열 콤마를 기준으로 분할
print(fruits_list.split(","))
# 거봉만 출력하기
print(fruits_list[3])

# ['딸기', '거봉', '키위', '사쿠란보'] > 공백 그대로 유지
# fruits2 = "딸기, 거봉, 키위, 사쿠란보"
# print(fruits2.split(","))  # 문자열 콤마+공백 1칸을 기준으로 분할
# ['딸기', ' 거봉', ' 키위', ' 사쿠란보']

"""실습 2"""
# a = "PUMP A 03"  # split - 공백 기준으로 나누기
# print(a.split())  # ['PUMP', 'A', '03']

"""실습 3"""
word = "a, b, c, d"
print(word.split(","))  # ['a', ' b', ' c', ' d']

"""실습 5"""
list = ["2025", "01", "15"]
print("-".join(list))  # 2025-01-15

"""pyThon"""
a = "python"  # pyThon 출력
print(a[:2] + a[2].upper() + a[3:])  # pyThon

# 다른 방법
print(a.split("t"))  # ["py", "hon"]
print("T".join(a.split("t")))  # "pyThon"
print(a[2].upper().join(a.split("t")))  # "pyThon"

# ==============================
print("=== print 함수의 sep, end ===")

print("2026", "07", "27")  # 2026 07 27 (기본적으로는 공백 1칸)

# sep 속성을 사용하면 구분을 공백이 아닌 특정 문자열로 가능
print("2026", "07", "27", sep="살해")  # 2026살해07살해27
# 공백 대신 sep 소성에 전달한 문자열이 삽입되어 이어짐

print("안녕", "하세")  # 안녕 하세
print("안녕", "하세", end="요")  # 안녕 하세요
# end 속성 사용 시 출력문 마지막에 해당 문자열이 삽입 됨
# print("안녕", "하세", end="요", "ㅎㅎ") # end 속성 뒤에 인자 추가 불가

# print 함수 + 사용 시 sep과 end
print("안녕" + "하세", end="요" + "이렇게?")  # 정상 동작

# 기본적으로 print문에는 sep으로 공백 한 칸,
# end로 \n(줄바꿈)이 적용되어 있음
# 근데, 개발자가 각 속성을 직접 부여할 경우
# 기본값이 아닌 전달받은 속성값을 사용
# print("이런식으로 쓰죠?", "근데 안 보이는 기본값이 있어요", sep =" ", end ="\n")

"""실습 7"""
date = "2026/07/27"
new_date = date.split("/")
print("-".join(new_date))  # 2026-07-27

"""실습 8"""
machine = "1, NORMAL,25.3"
update = machine.split(",")
update_1 = update[1].strip().lower()
print(update_1)

""" 실습 1"""
# 출력 결과: 설비 PUMP_A, 온도 36도
# 기존 방식
# name = "PUMP_A"
# temp = 87
# print("설비" + name + ", 온도 " + str(temp))

# f string 사용
name = "PUMP_A"
temp = 87
print(f"설비{name}, 온도{temp}도")
# 따옴표 밖에 f 작성하기
# 변수명은 꼭 {중괄호}에 감싸기

# f-string 연산
hour = 10

# 우리는 하루에 8시간 수업을 듣고, 이는 480분입니다.
print(f"우리는 하루에 {hour}시간 수업을 듣고, 이는 {hour * 60}분입니다.")

""" 실습 2 """
score_1 = 75
score_2 = 58
score_3 = 96

print(f"평균 : {(score_1 + score_2 + score_3) / 3}")

""" 실습 3 """
value = 87.456
print(f"{value}")
print(f"{value:.1f}")  # 소수점 첫째자리까지 출력
print(f"{value:.2f}")  # 소수점 둘째자리까지 출력

""" 실습 4"""
data = " 5, sensor_2, WARNING, 0.78912 "
parts = data.strip().split(",")
sensor = parts[1].strip()
status = parts[2].strip().lower()
value = float(parts[3].strip())
print(f"[센서 {sensor}] 상태 {status},측정값 {value:.2f}")
