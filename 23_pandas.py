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
