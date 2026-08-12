# except들의 연속과
#  finally 코드

text = "24.5"  # 정상
# text = "영크크" # 비정상

try:
    temp = float(text)

except ValueError:
    print("ValueError 문제가 발생했습니다.")
    temp = 0
except NameError:
    print("NameError 문제가 발생했습니다.")
finally:
    # 오류가 있건 없건 finally의 코드를 실행하여 마무리
    print(temp * 2)

""" 실습 1 (try- finally로 오류가 나도 파일을 반드시 닫기)
try:
    temp = int("안녕하세요")

except TypeError:
    print("TypeError 문제가 발생했습니다.")

finally:
    print("안녕하세요.") """

# 반복문 안에서 예외처리

my_list = ["123", "456", "영크크", "32", "53"]
problems = 0
for text in my_list:
    # 반복을 하는 중에 문제가 생긴 경우만 건너뛰고
    # 계속 반복을 이어서 진행시키기
    try:
        my_number = int(text)
        print(my_number)
    except:
        # print("문제발생")
        # 문제가 생겼다면 더 이상 반복문 안의 출려까지 이어가면 안되겠다
        # 그래서 여기서 끊고 다음 내용 처리하게 반복문 넘기기

        # 갈 때 가더라도 문제상황 카운팅 정도는 좋잖아
        problems += 1
        continue

    print(my_number)

    print(f"{problems}개는 문제가 있어서 건너뜀")

""" 실습 2. """
# 소숫점 이하의 숫자가 포함된 숫자들을 20개 정도 만들어 리스트에 담기
# 그 사이에 엉뚱한 글자들이 포함된 내용도 포함시키기
# 리스트 데이터를 사용해서 문제 풀기

num = [
    12.4,
    23.5,
    34.6,
    45.7,
    "사나이정민♥︎김수민",
    56.8,
    67.9,
    78.0,
    89.1,
    42.5,
    53.6,
    64.2,
    75.3,
    86.4,
    97.5,
    108.6,
    119.7,
    130.8,
    141.9,
    "영크크",
    152.0,
]
problems = 0
for text in num:
    try:
        my_number = float(text)
        problems += 1
    except:
        continue

print(f"정상값의 합{problems}입니다.")

""" 실습 3 (여러 파일 묶어 처리하기) """
# 다음과 같은 식의 리스트를 만들어 반복문으로 처리
# for문으로 리스트의 문자열을 꺼내어 해당 이름의 파일들을 열어보기 시도하면 됨

file_names = [
    "08_press.csv",
    "09_ict_inspection.csv",
    "09_ict_inspection_dirty.csv",
    "김수민의 남자 찾기.csv",
]
count = 0
for file_name in file_names:
    try:
        f = open(file_name, "r", encoding="utf-8")
        count += 1
        print(f"{file_name} 열기 성공")
        f.close()

    except FileNotFoundError:
        continue

print(f"{count}개의 파일을 열었습니다.")


# 학생들의 점수를 가져와서
# 각 학생별 합께와
# 모든 학생들의 평균 점수를 내는 코드

import os
import sys
import csv

# 0. 미리 전체 합산 점수 낼 준비를 한다.
total_all = 0
students_count = 0
# 1. 파일을 연다.
file_path = os.path.join("data", "student_scores.csv")

if not os.path.exists(file_path):
    print("파일을 찾지 못했습니다.")
    sys.exit(1)

with open(file_path, "r", encoding="utf-8") as f:

    # print(reader)
    # 2. 파일 내용으로부터 리스트 데이터를 얻는다.
    reader = csv.DictReader(f)

    for row in reader:
        name = row.get("\ufeff이름", "(이름없음)")
        kor = int(row.get("국어", "0"))
        eng = int(row.get("영어", "0"))
        math = int(row.get("수학", "0"))
        total = (kor + eng + math) / 3
        print(f"{name} | {kor} | {eng} | {math} | {total}")
        # 3. 점수 계산 (합계, 평균)
        students_count += 1
        total_all += total

# 4. 결과를 화면에 보여주기
avg_all = total_all / students_count

print(f"전체 {students_count}명 | 평균 {avg_all}점")


""" 제출 한 하는 실습"""
# 10_student_score.csv를 기반으로
# 실행 끝날 때 최고점 학생, 최저점 학생도 찾아서 출력하기
# 실행 끝날 때 각 과목별 평균도 출력하기

import os
import sys
import csv

file_path = os.path.join("data", "student_scores.csv")

if not os.path.exists(file_path):
    print("파일을 찾지 못했습니다.")
    sys.exit(1)

kor_total = 0
eng_total = 0
math_total = 0
students_count = 0

with open(file_path, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        name = row.get("\ufeff이름", "(이름없음)")
        kor = int(row.get("국어", "0"))
        eng = int(row.get("영어", "0"))
        math = int(row.get("수학", "0"))
        mean_score = (kor + eng + math) / 3
        max_score = max(float(mean_score))
        min_score = min(float(mean_score))
        for max_score in mean_score:
            print(f"최고점 학생 : {name}")
            for min_score in mean_score:
                print(f"최저점 학생 : {name}")
        kor_total += kor
        eng_total += eng
        math_total += math

        print(
            f"{name} | {kor_total / students_count} | {eng_total / students_count} | {math_total / students_count} | {total}"
        )

        students_count += 1
        total_all += total
