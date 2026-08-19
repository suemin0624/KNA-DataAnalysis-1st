# Boolean Series 코드
import pandas as pd

df = pd.read_csv("data/13_diecasting_small.csv")
df.info()
# Column Non-Null   Count        Dtype
# ---  ------  --------------  -----
# 0   샷       30 non-null     int64
# 1   실린더압력   30 non-null     float64
# 2   주조압력    30 non-null     float64
# 3   사이클타임   30 non-null     float64
# 4   비스킷두께   30 non-null     float64
# 5   형체력     30 non-null     float64
# 6   품질등급    30 non-null     object
# dtypes: float64(5), int64(1), object(1)

print(df.describe())

s = df["비스킷두께"]  # Series
s.info()
# <class 'pandas.core.series.Series'>
# RangeIndex: 30 entries, 0 to 29
# Series name: 비스킷두께
# Non-Null Count  Dtype
# --------------  -----
# 30 non-null     float64
# dtypes: float64(1)
# memory usage: 372.0 bytes

print("앞-----------------")
print(s.head())
# 0    10.0
# 1    11.0
# 2    21.0
# 3    11.0
# 4    14.0

print("뒤-----------------")
print(s.tail())
# 25    11.0
# 26    12.0
# 27    19.0
# 28    11.0
# 29     2.0

# 비스킷두께 숫자들만 담긴 Series에
# 13 이상인지 따져보는 연산을 시킨다면?
s_boolean = s >= 13
print(s_boolean.head())
# 0    False
# 1    False
# 2     True
# 3    False
# 4     True
# Name: 비스킷두께, dtype: bool

# 위에서 생성된 Boolean Series에서 True값들이 모두 몇 개일까요?
# = 최초 csv 파일에서 '비스킷두께' 컬럼의 값들 중에 13 이상인 경우는 몇 개?
# Boolean Series의 sum() 같은 통계를 낸다면
# True = 1, False = 0 처리
print(s_boolean.sum())  # 6 (True의 갯수)

""" 실습 1) 단일 조건으로 행 추출하기 """
# 조건을 만들고 그 조건으로 원하는 행만 추출
import pandas as pd

df = pd.read_csv("data/13_diecasting_small.csv")
df.info()
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   샷       30 non-null     int64
#  1   실린더압력   30 non-null     float64
#  2   주조압력    30 non-null     float64
#  3   사이클타임   30 non-null     float64
#  4   비스킷두께   30 non-null     float64
#  5   형체력     30 non-null     float64
#  6   품질등급    30 non-null     object
# dtypes: float64(5), int64(1), object(1)
# memory usage: 1.8+ KB


# 비교 연산자로 실린더압력 기준의 조건식을 만들어 Boolean Series 생성
s = df["실린더압력"]
s.info()
s_boolean = s >= 230
s_boolean.info()  # dtypes: bool(1) -> Boolean Series 확인

# sum으로 조건을 만족하는 행 개수 확인
print(s_boolean.sum())  # True = 1, False = 0 -> 합계로 True 갯수 파악
# 결과 : 5
# 만든 조건을 데이터프레임 대괄호에 넣어 행 추출 -> 행의 갯수 출력
# 전체 df를 대상으로 앞서 특정 컬럼에 대한 불리언 시리즈를
# 컬럼 요구하는 [] 사이에 넣어주면,

df_sub = df[df["실린더압력"] >= 230]
df_sub.info()
print(len(df_sub))
# 결과 : 5
# <class 'pandas.core.frame.DataFrame'>
# Index: 5 entries, 7 to 27
# Data columns (total 7 columns):
#   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   샷       5 non-null      int64
#  1   실린더압력   5 non-null      float64
#  2   주조압력    5 non-null      float64
#  3   사이클타임   5 non-null      float64
#  4   비스킷두께   5 non-null      float64
#  5   형체력     5 non-null      float64
#  6   품질등급    5 non-null      object
# dtypes: float64(5), int64(1), object(1)
# memory usage: 320.0+ bytes

# 예상 결과
# 참 개수와 추출 행 수가 같게 출력 (실린더압력 230 이상 19건)

""" 실습 2) 임계값 넘는 설비 골라내기 """
# 실제 제조 데이터에서 위험 임계값을 넘는 설비 추출
import pandas as pd

df = pd.read_csv("data/13_diecasting_small.csv")
df.info()

# 1. df['비스킷두께'] -> 시리즈 추출
# 2. 추출된 시리즈 내용들이 16이상이면 True, 아니면 False -> Boolean Series
# 3. Boolean Series와 비교해서 df의 내용 중에 True와 겹치는 행들을 추출 -> df_sub
df_sub = df[df["비스킷두께"] >= 16]
df_sub.info()  # 5 row 존재 확인 - Index: 5 entries
print(len(df_sub))  # 5 row 존재 확인

print(df_sub.head(3))
# 샷  실린더압력    주조압력  사이클타임  비스킷두께    형체력 품질등급
# 2    3  215.0  1040.0   20.7   21.0  253.0   주의
# 12  13  265.0   596.0   33.9   19.0  354.0   주의
# 17  18  265.0   596.0   33.7   19.0  357.0   주의
# 비스킷두께 열에 비교 연산자로 임계값 기준 조건 생성

# 조건을 대괄호에 넣어 임계값 초과 설비만 추출

# 결과에서 샷와 비스킷두께 열만 골라 확인

import pandas as pd

# 기존에 우리가 알고 있던 파이썬의 "그리고", "또는" 표시
a = 10
b = 5

if a > 5 and b < 3:
    print("이것이 '그리고' 입니다")

if a > 5 or b < 3:
    print("이것이 '또는' 입니다")

# 파이썬의 기본 and와 or은 양쪽 비교대상이 모두 Boolean이 되어야 함
# True/False외의 것은 비교대상이 안 됨

# 그렇다면 DF나 Series에는 and/or로 처리불가?
## -> 불가

df = pd.read_csv("data/13_diecasting_small.csv")
df.info()
#   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   샷       6 non-null      int64
#  1   실린더압력   6 non-null      float64
#  2   주조압력    6 non-null      float64
#  3   사이클타임   6 non-null      float64
#  4   비스킷두께   6 non-null      float64
#  5   형체력     6 non-null      float64
#  6   품질등급    6 non-null      object

df_sub1 = df[df["비스킷두께"] >= 13]
df_sub1.info()  # 6 entries
#   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   샷       5 non-null      int64
#  1   실린더압력   5 non-null      float64
#  2   주조압력    5 non-null      float64
#  3   사이클타임   5 non-null      float64
#  4   비스킷두께   5 non-null      float64
#  5   형체력     5 non-null      float64
#  6   품질등급    5 non-null      object

df_sub2 = df[df["사이클타임"] >= 25]
df_sub2.info()  # 6 entries
#   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   샷       7 non-null      int64
#  1   실린더압력   7 non-null      float64
# 2   주조압력    7 non-null      float64
#  3   사이클타임   7 non-null      float64
#  4   비스킷두께   7 non-null      float64
#  5   형체력     7 non-null      float64
#  6   품질등급    7 non-null      object

""" 실습 3) 두 조건 묶기 """
# 두 조건을 그리고(&) 또는(|)으로 묶어 행을 추출
df_both = df[(df["비스킷두께"] >= 13) & (df["사이클타임"] >= 25)]
df_both.info()
print(len(df_both))  # 5

df_either = df[(df["비스킷두께"] >= 13) | (df["사이클타임"] >= 25)]
df_either.info()
print(len(df_either))  # 7

# &와 | 그리고 괄호 규칙
# 두 조건 모두 만족 -> &
# 하나라도 만족 -> |
# 각 조건은 반드시 괄호로 감싸기
# 괄호를 빼면 &가 비교보다 먼저 계산되려 해서 오류

# 부정 조건
# 물결 기호를 조건 앞에 붙이면 참과 거짓이 뒤집힘
# 복잡한 조건 전체를 통째로 뒤집을 때 특히 편리
# ~isin(목록)으로 목록에 없는 행 추출
# df['품질등급'].isin(['양품', '주의'])

# between으로 범위 조건
# 값이 두 경계 사이에 있는지 한 번에 검사 - 양쪽 경계 모두 포함
# ex) df['비스킷두께'].between(70, 80)

""" 실습 4) 부정/목록/범위 조건 """
# 부정/목록/매칭/범위 조건을 각각 적용
df = pd.read_csv("data/13_diecasting_shot.csv")
df.info()

# 물결 기호로 고장이 아닌 설비만 뒤집어 추출
print(df.tail())  # 품질등급 컬럼에 불량 항목 발견!
print(df[df["품질등급"] == "불량"].head())  # 추려본 내용에 '불량'만 모인듯
print(len(df[df["품질등급"] == "불량"]))  # 20

# 그렇다면 '불량' 아닌 것들은?
print(df[~(df["품질등급"] == "불량")].head())  # '불량' 없는듯
print(len(df[~(df["품질등급"] == "불량")]))  # 180

# isin으로 품질등급이 특정 목록에 속하는 행 추출 - 품질등급 - 양품 또는 주의
print(df[(df["품질등급"] == "양품") | (df["품질등급"] == "주의")].head())
# 샷  실린더압력    주조압력  사이클타임  비스킷두께    형체력 품질등급
# 0  1  214.0  1037.0   20.7   10.0  258.0   양품
# 1  2  217.0  1052.0   20.7   11.0  257.0   양품
# 2  3  214.0  1037.0   20.8   11.0  254.0   양품
# 3  4  217.0  1052.0   20.6   11.0  253.0   양품
# 4  5  217.0  1052.0   20.6   11.0  254.0   양품

# isin으로 품질등급이 특정 목록에 속하는 행 추출
print(df[df["품질등급"].isin(["양품", "주의"])].head())
# 샷  실린더압력    주조압력  사이클타임  비스킷두께    형체력 품질등급
# 0  1  214.0  1037.0   20.7   10.0  258.0   양품
# 1  2  217.0  1052.0   20.7   11.0  257.0   양품
# 2  3  214.0  1037.0   20.8   11.0  254.0   양품
# 3  4  217.0  1052.0   20.6   11.0  253.0   양품
# 4  5  217.0  1052.0   20.6   11.0  254.0   양품
print(len(df[df["품질등급"].isin(["양품", "주의"])]))  # 180

# between으로 실린더압력이 지정 범위에 든 행 추출
print(df[df["실린더압력"].between(210, 230)].head())
print(len(df[df["실린더압력"].between([210, 230])]))  # 89

# 그 외의 것들이 200 - 89 = 111개 나오는지 확인하기
print(len(df[~df["실린더압력"].between(210, 230)]))  # 111

# 예상 결과) 순서대로 192건/94건/108건 출력

# value_counts로 개수 세기
# 한 열에 어떤 값이 몇 번씩 나오는지 자동으로 세는 도구

# value_counts 기본 코드
# 냉각기상태별 사이클 건수 세기
df["냉각기상태"].value_counts()
# 출력: 고장 40, 저하 40, 정상 40

# result 열의 정상/고장 건수 세기
df["result"].value_counts()
# 출력: 정상 67, 고장 53

# 개수를 비율로 바꾸기
# 개수만으로는 많고 적음 판단 어려움
# 전체에서 차지하는 비율로 봐야 비중이 보임
# 규모가 다른 대상을 비교할 때 필수

# normalize로 비율 구하기
df["result"].value_counts(normalize=True).round(3)
# 결과)
# 정상 0.0558
# 고장 0.442
# -> 정상 약 55.8%, 고장 약 44.2%

# 수치형을 구간으로 묶어 세기
# 먼저 묶고, 그 다음에 셈 -> 순서가 핵심

# step1
# pd.cut으로 구간 묶기) 숫자를 정해진 경계에서 잘라 구간으로 묶음
# step2
# value_counts 붙이기) 만든 구간 데이터에 붙여 구간별 빈도 세기

""" 실습 5) 위험 순으로 정렬하기"""
# 데이터를 위험한 순서로 정렬하고 상위만 추출

# sort_values로 비스킷두께를 큰 값부터 내림차순 정렬
# head로 상위 다섯 개만 추출해 값 확인
# 여러 열을 리스트로 묶어 우선순위 다중 정렬

""" 실습 6) 필터링과 정렬 연결 """
# 조건으로 거른 결과에 정렬을 이어 붙이기

# 고장 여부 조건으로 고장 설비만 먼저 거르기
# "품질등급" 컬럼 == "불량"
df_filtered = df[df["품질등급"] == "불량"]
print(df_filtered.head())

# 거른 결과에 sort_values를 점으로 이어 비스킷두께 내림차순 정렬
df_sorted_after_filtered = df[df["품질등급"] == "불량"].sort_values(
    "비스킷두께", ascending=False
)

# head로 상위 다섯 개만 남겨 샷 확인
print(df[df["품질등급"] == "불량"].sort_values("비스킷두께", ascending=False).head(5))

# 예상 결과) 5개 행, 비스킷두께 큰 순 샷 목록 출력
