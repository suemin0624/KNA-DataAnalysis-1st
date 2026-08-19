# 실습 1) csv 불러오기 워밍업
# 설비 3대 측정값
# 메모장에 쉼표로 데이터 작성 후 csv로 저장
import pandas as pd
import os

filepath = os.path.join("data", "12_metro_small.csv")

try:
    df = pd.read_csv(
        filepath,
        encoding="utf-8",
        index_col="측정시각",
        nrows=5,
        usecols=["측정시각", "가동상태"],
    )
    print(df.shape)  # (30, 7)

except FileNotFoundError:
    print(f"파일이 없습니다 : {filepath}")

print(df.head(1))
# 결과값)
#  측정시각  압축압력  배출압력  저장압력  오일온도  모터전류 가동상태
#   0  2020-02-27 06:38:47   9.3 -0.02   9.3  51.3  6.04   가동

# 실습 2) 설비 센서 CSV 불러오기
# read_csv로 데이터를 불러와 head로 확인

# import후 read_csv로 담고 head로 확인
import pandas as pd

# 12_metro_compressor.csv
# 200행 7열 - 인덱스 3번 행 오일온도가  NaN

import pandas as pd

df = pd.read_csv("data/12_metro_compressor_semicolon.csv", encoding="utf-8")
print(df.head(3))
# 측정시각;압축압력;배출압력;저장압력;오일온도;모터전류;가동상태
# 0    2020-02-27 06:38:47;9.3;-0.02;9.3;51.3;6.04;가동
# 1  2020-02-27 07:28:21;8.55;-0.02;8.55;56.8;0.04;정지
# 2  2020-02-27 08:17:54;8.67;-0.02;8.67;55.7;0.03;정지
print(df.shape)  # (200, 7)

# 세미콜론 구분 파일
# sep 없이 읽으면 200행 1열, sep=";"이면 200행 7열

import pandas as pd

df = pd.read_csv("data/12_metro_compressor_semicolon.csv")
print(df.shape)  # (200, 1)

# 실습 3) 한글.구분자 깨짐 옵션 다루기
import pandas as pd

# 수정 전) df = pd.read_csv("data/12_metro_compressor_semicolon.csv")
# 수정 후)
df = pd.read_csv("data/12_metro_compressor_semicolon.csv", encoding="utf-8", sep=";")
print(df.head(3))
#  측정시각  압축압력  ...  모터전류  가동상태
# 0  2020-02-27 06:38:47  9.30  ...  6.04    가동
# 1  2020-02-27 07:28:21  8.55  ...  0.04    정지
# 2  2020-02-27 08:17:54  8.67  ...  0.03    정지

# 실습 4) 필요한 열만 골라 불러오기
import pandas as pd

df = pd.read_csv(
    "data/12_metro_compressor_semicolon.csv",
    sep=";",
    usecols=["측정시각", "오일온도", "모터전류", "가동상태"],
)

print(df.shape)  # (200, 4)
print(df.head(3))
# 측정시각  오일온도  모터전류 가동상태
# 0  2020-02-27 06:38:47  51.3  6.04   가동
# 1  2020-02-27 07:28:21  56.8  0.04   정지
# 2  2020-02-27 08:17:54  55.7  0.03   정지

# 실습 5)
# data/ 누락, 철자, .csv - 세 종류의 FileNotFoundError

# import pandas as pd

# 수정 전)
# df = pd.read_csv('12_metro_small.csv') # FileNotFoundError
# print(df.shape)

# 수정 후)
import pandas as pd

df = pd.read_csv("data/12_metro_small.csv")
print(df.shape)  # (30, 7)

# 실습 6) read_csv 옵션 종합 연습
# 경로/인코딩/구분자/열 선택을 한 번에 적용

# 세미콜론 + 한글 파일에서 필요한 열만

import pandas as pd
import os

filepath = os.path.join("data", "12_metro_small.csv")
df = pd.read_csv(filepath, encoding="utf-8", sep=",", usecols=["압축압력", "배출압력"])
print(df.shape)  # (30, 2)
print(df.head(5))
# 압축압력  배출압력
# 0  9.30 -0.02
# 1  8.55 -0.02
# 2  8.67 -0.02
# 3  9.76 -0.02
# 4  8.49 -0.02

# 12-02 실습 1) head.tail로 디지털 신호 살펴보기
import pandas as pd

# 다음 코드로부터 시작
df = pd.read_csv("data/12_metro_digital.csv")

# 위 코드가 정상 실행되어 shape가 나오는지 확인부터 하고
# 적절한 숫자들의 줄을 정해서 .head()와 .tail()을 출력하기

print(df.head())
#                   측정시각  압축기  타워  저압스위치
# 0  2020-02-27 06:38:47    0   0      0
# 1  2020-02-27 07:28:21    1   1      0
# 2  2020-02-27 08:17:54    1   1      0
# 3  2020-02-27 09:07:27    1   1      0
# 4  2020-02-27 09:57:01    1   1      0
print(df.tail())
#                     측정시각  압축기  타워  저압스위치
# 115  2020-03-03 17:34:17    1   1      0
# 116  2020-03-03 18:23:51    1   1      0
# 117  2020-03-03 19:13:25    1   1      0
# 118  2020-03-03 20:02:59    1   1      0
# 119  2020-03-03 20:52:32    1   1      0


# 실습 2) head/tail 행 개수 조절

print(df.shape)  # (120, 4)
print(df.head(2))
#                  측정시각  압축기  타워  저압스위치
# 0  2020-02-27 06:38:47    0   0      0
# 1  2020-02-27 07:28:21    1   1      0


print(df.tail(5))
#                    측정시각  압축기  타워  저압스위치
# 115  2020-03-03 17:34:17    1   1      0
# 116  2020-03-03 18:23:51    1   1      0
# 117  2020-03-03 19:13:25    1   1      0
# 118  2020-03-03 20:02:59    1   1      0
# 119  2020-03-03 20:52:32    1   1      0

# 실습 3) 구조 파악 3종 도구
# shape/columns/dtypes로 데이터 뼈대 읽기
print("------ 실습3번 ------")
print(df.shape)  # (120, 4)
print(df.columns)
# Index(['측정시각', '압축압력', '배출압력', '저장압력', '오일온도',
# '모터전류', '가동상태'], dtype='object')
print(df.dtypes)
#   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
# 0   측정시각    120 non-null    object
# 1   압축기     120 non-null    int64
# 2   타워      120 non-null    int64
# 3   저압스위치   120 non-null    int64

# 실습 4) 열 이름/자료형 점검

# 12_metro_compressor.csv 읽어와서 DF에 담기
# .columns 출력 df.columns.tolist() 출력
# DF의 dtypes 출력
df1 = pd.read_csv("data/12_metro_compressor.csv", encoding="utf-8")
print(df1.columns)
print(df1.columns.tolist())

# 실습 5) info로 데이터 건강검진
df3 = pd.read_csv("data/12_metro_digital.csv", encoding="utf-8")
print(df3.info())

# 실습 6) describe로 이상 신호 찾기
# 평균/분위수/최대를 읽어 이상 신호 있는 열 찾기

import pandas as od

# 12_metro_compressor/csv
# 온도, 진동에 이상값 존재

df = pd.read_csv("data/12_metro_compressor.csv")
print(df.shape)  # (200, 7)
print(df.head())
#  측정시각  압축압력  ...  모터전류  가동상태
# 0  2020-02-27 06:38:47  9.30  ...  6.04    가동
# 1  2020-02-27 07:28:21  8.55  ...  0.04    정지
# 2  2020-02-27 08:17:54  8.67  ...  0.03    정지
# 3  2020-02-27 09:07:27  9.76  ...  3.81    가동
# 4  2020-02-27 09:57:01  8.49  ...  0.04    정지
print(df.tail())
#      측정시각  압축압력  ...  모터전류  가동상태
# 195  2020-03-06 15:03:00  8.72  ...  5.81    가동
# 196  2020-03-06 15:52:33  8.85  ...  0.04    정지
# 197  2020-03-06 16:42:06  9.74  ...  3.77    가동
# 198  2020-03-06 17:31:39  9.89  ...  3.82    가동
# 199  2020-03-06 18:21:13  9.87  ...  3.75    가동
df.info()  # print 안에 넣지 않기
#   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
# 0   측정시각    200 non-null    object
# 1   압축압력    200 non-null    float64
# 2   배출압력    200 non-null    float64
# 3   저장압력    200 non-null    float64
# 4   오일온도    199 non-null    float64
# 5   모터전류    200 non-null    float64
# 6   가동상태    200 non-null    object
# STEP1 : describe 후 75%와 max 차이 큰 열 찾기
print(df.describe())
#       압축압력  ...        모터전류
# count  200.000000  ...  200.000000
# mean     9.172200  ...    2.060850
# std      0.583699  ...    2.196505
# min      8.130000  ...    0.030000
# 25%      8.700000  ...    0.040000
# 50%      9.175000  ...    0.040000
# 75%      9.665000  ...    3.812500
# max     10.220000  ...    6.190000


# 실습 7) 통계량 문장으로 묘사
# describe 통계를 자기 말로 풀어 설명

# 설비 센서 데이터의 "한 열(1 column)"을 묘사

import pandas as pd

df = pd.read_csv("data/12_metro_compressor.csv")
df.info()

# 오일온도 컬럼만 떼서 describe 통계 보기
