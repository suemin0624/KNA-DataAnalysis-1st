# Pandas에서 원본에 변경을 주려며 꼭 .copy()를 하기
# 안 그러면 SettingWithCopyWarning 경고 발생

import pandas as pd

df = pd.read_csv("data/13_diecasting_shot.csv", encoding="utf-8")
df.info()

df_bad = df[df["품질등급"] == "불량"].copy()

# 만약 copy 없이 바로 df_bad의 모든 품질등급을 다른 내용으로 변경한다면?
# 경고가 발생할 수도 있음
df_bad["품질등급"] == "점검"

print(df_bad.head())


""" 실습 5) 위험 순으로 정렬하기 """
print("========실습5===========")
# 데이터를 위험한 순서로 정렬하고 상위만 추출

df = pd.read_csv("data/13_diecasting_shot.csv", encoding="utf-8")
print(df.shape)  # (200, 7)
df.info()  # 비스킷두께 컬럼 발견
#   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   샷       200 non-null    int64
#  1   실린더압력   186 non-null    float64
#  2   주조압력    186 non-null    float64
#  3   사이클타임   186 non-null    float64
#  4   비스킷두께   186 non-null    float64
#  5   형체력     186 non-null    float64
#  6   품질등급    200 non-null    object
print(df.head(3))
#    샷  실린더압력    주조압력  사이클타임  비스킷두께    형체력 품질등급
# 0  1  214.0  1037.0   20.7   10.0  258.0   양품
# 1  2  217.0  1052.0   20.7   11.0  257.0   양품
# 2  3  214.0  1037.0   20.8   11.0  254.0   양품

# sort_values로 비스킷두께를 큰 값부터 내림차순 정렬
# head로 상위 다섯 개만 추출해 값 확인
print(df.sort_values("비스킷두께", ascending=False).head(5))
#        샷  실린더압력    주조압력  사이클타임  비스킷두께    형체력 품질등급
# 197  198  113.0   255.0   36.6   27.0  354.0   불량
# 191  192  113.0   255.0   36.9   26.0  366.0   불량
# 42    43  215.0  1040.0   20.7   21.0  253.0   주의
# 196  197  265.0   595.0   36.2   20.0  355.0   불량
# 170  171  265.0   596.0   36.1   20.0  370.0   주의

# 여러 열을 리스트로 묶어 우선순위 다중 정렬
df_multi = df.sort_values(["품질등급", "형체력"], ascending=[True, False])
print(df_multi.head(5))
#        샷  실린더압력   주조압력  사이클타임  비스킷두께    형체력 품질등급
# 195  196  264.0  594.0   76.3   19.0  381.0   불량
# 198  199  264.0  595.0   36.1   19.0  372.0   불량
# 193  194  113.0  255.0   34.4   19.0  370.0   불량
# 191  192  113.0  255.0   36.9   26.0  366.0   불량
# 192  193  264.0  594.0   36.9   19.0  355.0   불량

""" 실습 6) 필터링과 정렬 연걸 """
print("===========실습 6==============")
# 조건으로 거른 결과에 정렬을 이어 붙이기
df = pd.read_csv("data/13_diecasting_shot.csv", encoding="utf-8")
df.info()
#   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   샷       200 non-null    int64
#  1   실린더압력   186 non-null    float64
#  2   주조압력    186 non-null    float64
#  3   사이클타임   186 non-null    float64
#  4   비스킷두께   186 non-null    float64
#  5   형체력     186 non-null    float64
#  6   품질등급    200 non-null    object

print(df.tail(5))
#        샷  실린더압력   주조압력   사이클타임  비스킷두께    형체력 품질등급
# 195  196  264.0  594.0    76.3   19.0  381.0   불량
# 196  197  265.0  595.0    36.2   20.0  355.0   불량
# 197  198  113.0  255.0    36.6   27.0  354.0   불량
# 198  199  264.0  595.0    36.1   19.0  372.0   불량
# 199  200  108.0  525.0  6170.0   15.0  237.0   불량

# 고정 여부 조건으로 고장 설비만 먼저 거르기
# 품질등급 == 불량
df_bad = df[df["품질등급"] == "불량"]
print(len(df_bad))  # 20
print(df_bad.head())
#        샷  실린더압력    주조압력  사이클타임  비스킷두께    형체력 품질등급
# 180  181  108.0   522.0  652.3   14.0  222.0   불량
# 181  182  214.0  1036.0   93.1   12.0  247.0   불량
# 182  183  215.0  1041.0   21.3    4.0  258.0   불량
# 183  184  216.0  1044.0   21.2   11.0  259.0   불량
# 184  185  219.0  1058.0   21.3    2.0  255.0   불량

# 거른 결과에 sort_values를 점으로 이어 비스킷두께 내림차순 정렬
# head로 상위 다섯 개만 남겨 샷 확인
df_filtered = (
    df[df["품질등급"] == "불량"].sort_values("비스킷두께", ascending=False).head(5)
)
print(df_filtered)
#        샷  실린더압력   주조압력  사이클타임  비스킷두께    형체력 품질등급
# 197  198  113.0  255.0   36.6   27.0  354.0   불량
# 191  192  113.0  255.0   36.9   26.0  366.0   불량
# 196  197  265.0  595.0   36.2   20.0  355.0   불량
# 192  193  264.0  594.0   36.9   19.0  355.0   불량
# 198  199  264.0  595.0   36.1   19.0  372.0   불량

""" 실습 7) 이상 의심 설비 리포트"""
# 불러오기부터 판단 문장까지 전체 워크플로우를 두 데이터에 적용

import pandas as pd

# 분석 워크플로우 5단계 맞춰가기
# 1. 불러오기
df = pd.read_csv("data/13_diecasting_shot.csv", encoding="utf-8")

# 2. 확인하기
df.info()
#   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   샷       200 non-null    int64
#  1   실린더압력   186 non-null    float64
#  2   주조압력    186 non-null    float64
#  3   사이클타임   186 non-null    float64
#  4   비스킷두께   186 non-null    float64
#  5   형체력     186 non-null    float64
#  6   품질등급    200 non-null    object
# 3. 필터링
df_warning = df[(df["비스킷두께"] >= 16) | (df["사이클타임"] >= 100)]
print(len(df_warning))  # 76

# 4. 정렬
df_report = df_warning.sort_values("비스킷두께", ascending=False)
print(df_report.head())
#        샷  실린더압력    주조압력  사이클타임  비스킷두께    형체력 품질등급
# 197  198  113.0   255.0   36.6   27.0  354.0   불량
# 191  192  113.0   255.0   36.9   26.0  366.0   불량
# 42    43  215.0  1040.0   20.7   21.0  253.0   주의
# 196  197  265.0   595.0   36.2   20.0  355.0   불량
# 170  171  265.0   596.0   36.1   20.0  370.0   주의

# 5. 선택 : [[...]] 대괄호 중첩 주의!
df_final = df_report[["샷", "품질등급", "형체력", "사이클타임"]]
print(df_final.head())
#  샷 품질등급    형체력  사이클타임
# 197  198   불량  354.0   36.6
# 191  192   불량  366.0   36.9
# 42    43   주의  253.0   20.7
# 196  197   불량  355.0   36.2
# 170  171   주의  370.0   36.1

print("----------------------")
print("가장 위험 목록")
print(df_final.head())
# 가장 위험 목록
# 샷 품질등급    형체력  사이클타임
# 197  198   불량  354.0   36.6
# 191  192   불량  366.0   36.9
# 42    43   주의  253.0   20.7
# 196  197   불량  355.0   36.2
# 170  171   주의  370.0   36.1
print("가장 위험한 항목")
print(df_final.head(1))
# 가장 위험한 항목
#  샷 품질등급    형체력  사이클타임
# 197  198   불량  354.0   36.6

""" 14_01 실습 1) value_counts로 빈도 세기 """
# 한 열을 골라 value_counts로 값별 개수 세기
import pandas as pd

df = pd.read_csv("data/14_hydraulic.csv", encoding="utf-8")

# 설비 데이터를 불러와 앞부분과 구조 확인
df.info()
# Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   냉각기상태   120 non-null    object
#  1   운전부하    120 non-null    object
#  2   밸브상태    120 non-null    object
#  3   온도      120 non-null    float64
#  4   진동      120 non-null    float64
#  5   압력      120 non-null    float64
#  6   냉각효율    120 non-null    float64
#  7   result  120 non-null    object

print(df.head(3))
#   냉각기상태 운전부하 밸브상태    온도     진동      압력  냉각효율 result
# 0    고장  고부하   정상  35.6  0.577  160.67  39.6     정상
# 1    고장  저부하   정상  47.5  0.604  158.65  17.6     정상
# 2    고장  저부하   정상  50.7  0.640  157.76  18.7     정상

# 설비 옆(컬럼)에 value_counts를 붙여 값별 개수 세기
print(df["밸브상태"].value_counts())
# 밸브상태
# 정상    61
# 지연    20
# 경미    20
# 심각    19

# 교대 열도 같은 방법으로 세어 가장 많은 값 확인
print(df["운전부하"].value_counts())
# 고부하    60
# 저부하    60

""" 실습 2) 비율과 불균형 데이터 """
# qc 합격/불합격 빈도와 비율로 뷸균형 확인
# 합격/불합격 빈도와 비율을 구해 불균형 데이터 확인
df_qc = pd.read_csv("data/14_hydraulic_qc.csv", encoding="utf-8")
df_qc.info()
#   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   검사결과    200 non-null    object
#  1   지표01    200 non-null    float64
#  2   지표02    200 non-null    float64
#  3   지표03    200 non-null    float64
#  4   지표04    200 non-null    float64
#  5   지표05    200 non-null    float64
#  6   지표06    200 non-null    float64
#  7   지표07    200 non-null    float64
#  8   지표08    200 non-null    float64
#  9   지표09    200 non-null    float64
#  10  지표10    200 non-null    float64

print(df_qc.head(3))
# 0   합격  44.7  0.615  159.01  35.7  6.66  2465.3  59.7  107.93  1.81  49.7
# 1   합격  41.9  0.611  159.55  46.3  6.67  2489.1  59.4  108.37  1.87  48.1
# 2   합격  40.1  0.599  159.87  47.0  6.68  2504.2  59.4  108.61  1.92  46.2

# 공정 데이터의 판정 열에 value_counts로 합격/불합격 개수 세기
print(df_qc["검사결과"].value_counts())
# 검사결과
# 합격     188
# 불합격     12

# normalize 옵션으로 각 값의 비율을 소수로 확인
print(df_qc["검사결과"].value_counts(normalize=True))
# 검사결과
# 합격     0.94
# 불합격    0.06

""" 실습 3) 구간으로 묶어 세기"""
# pd.cut으로 수치형 값을 구간으로 묶어 빈도 세기
# 수치형 센서 값을 구간으로 나눠 분포 확인

# 진동 열(컬럼)의 최솟값과 최댓값으로 값의 범위 확인
import pandas as pd

df = pd.read_csv("data/14_hydraulic.csv", encoding="utf-8")
df.info()
#   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   냉각기상태   120 non-null    object
#  1   운전부하    120 non-null    object
#  2   밸브상태    120 non-null    object
#  3   온도      120 non-null    float64
#  4   진동      120 non-null    float64
#  5   압력      120 non-null    float64
#  6   냉각효율    120 non-null    float64
#  7   result  120 non-null    object

print(df.head(3))
#   냉각기상태 운전부하 밸브상태    온도     진동      압력  냉각효율 result
# 0    고장  고부하   정상  35.6  0.577  160.67  39.6     정상
# 1    고장  저부하   정상  47.5  0.604  158.65  17.6     정상
# 2    고장  저부하   정상  50.7  0.640  157.76  18.7     정상

print(df["진동"].max())  # 0.779
print(df["진동"].min())  # 0.53

# pd.cut으로 경계와 이름표를 정해 세 구간으로 묶기
# band = pd.cut(df["진동"], bins=[0.0, 0.6, 0.7, 10.0])
# print(band.value_counts())

# pd.cut 구간 빈도 코드
import pandas as pd

df = pd.read_csv("data/14_hydraulic.csv", encoding="utf-8")
df.info()
print(df.head(3))

print(df["온도"].value_counts())
# 위와 같이 범위 없이 개별 경우의 수를 따지면 62가지나 됨
# 그래서 범위를 설정해 경우의 수를 줄여보기 -> 범주화
# -- [개념] pd.cut으로 수치형을 구간으로 묶어 세기
# 형식: pd.cut(df['수치열'], bins=[경계...], labels=[이름...]) -> 구간 라벨 Series
# 엣지: 경계(bins)는 이름(labels)보다 반드시 하나 많아야 함(경계 4개 -> 구간 3개)
band = pd.cut(df["온도"], bins=[0, 40, 50, 200], labels=["낮음", "보통", "높음"])
print(band.value_counts())
# 온도
# 낮음    41
# 보통    40
# 높음    39

# groupby 기본 코드
import pandas as pd

df = pd.read_csv("data/14_hydraulic.csv", encoding="utf-8")
df.info()
print(df.head(3))
#   냉각기상태 운전부하 밸브상태    온도     진동      압력  냉각효율 result
# 0    고장  고부하   정상  35.6  0.577  160.67  39.6     정상
# 1    고장  저부하   정상  47.5  0.604  158.65  17.6     정상
# 2    고장  저부하   정상  50.7  0.640  157.76  18.7     정상

# '냉각기상태' 컬럼의 내용별로 그룹핑을 하자 -> 분할
# 분할된 DF마다 '온도' 컬럼이 있으니까, '온도'의 평균을 구해보자
print(df.groupby("냉각기상태")["온도"].mean().round(2))
# 냉각기상태
# 고장    54.67
# 저하    45.46
# 정상    35.89

print(df.groupby("냉각기상태")[["온도", "진동"]].mean().round(2))
#         온도    진동
# 냉각기상태
# 고장     54.67  0.69
# 저하     45.46  0.61
# 정상     35.89  0.55

""" 종합 실습 """
import pandas as pd

df = pd.read_csv("data/students_groupby_practice.csv", encoding="utf-8")

# [문제 1] 이 학교의 전체 학생 수를 구하세요. (힌트: len 또는 shape)
print(df.shape)  # (60, 6)

# [문제 2] 학년별 학생 수를 구하세요. (힌트: groupby + count 또는 size)


# [문제 3] 학년 내 각 반별 학생 수를 구하세요. (힌트: 다중 컬럼 groupby)
print(df.groupby("학년")["반"].count())
# 학년
# 1    20
# 2    20
# 3    20

# [문제 4] 각 반(학년, 반 조합)의 국어 점수 평균을 소수점 둘째 자리까지 구하세요.
print(df.groupby(["학년", "반"])["국어"].mean().round(2))
# 학년  반
# 1   A    76.8
#     B    78.8
#     C    66.0
#     D    59.4
# 2   A    64.6
#     B    81.4
#     C    84.6
#     D    72.0
# 3   A    68.6
#     B    81.4
#     C    73.0
#     D    69.8

# [문제 5] 각 학년의 영어 점수 평균을 소수점 둘째 자리까지 구하세요.
print(df.groupby(("학년"))["영어"].mean().round(2))
# 학년
# 1    64.80
# 2    73.35
# 3    69.90

# [문제 6] 학교 전체의 수학 점수 평균을 소수점 둘째 자리까지 구하세요.
print(df["수학"].mean().round(2))  # 68.95
