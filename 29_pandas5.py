"""15_02 실습 1) dropna로 행/열 삭제"""

import pandas as pd

df = pd.read_csv("data/15_02_사출성형_공정.csv", encoding="utf-8")
df.info()
#   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   측정시각    250 non-null    object
#  1   불량여부    250 non-null    int64
#  2   사출기     250 non-null    object
#  3   사이클시간   250 non-null    float64
#  4   성형사이클   250 non-null    float64
#  5   배럴온도1   250 non-null    float64
#  6   배럴온도2   250 non-null    float64
#  7   배럴온도3   250 non-null    float64
#  8   배럴온도4   250 non-null    float64
#  9   호퍼온도    250 non-null    float64
#  10  스크루속도   249 non-null    float64
#  11  사출압력    247 non-null    float64
#  12  스크루위치   245 non-null    float64
#  13  전환위치    241 non-null    float64
#  14  계량시간    241 non-null    float64
#  15  계량시작위치  216 non-null    float64
#  16  계량시작점   216 non-null    float64
#  17  최소쿠션    216 non-null    float64
#  18  최대사출압   190 non-null    float64
#  19  전환압력    182 non-null    float64
#  20  최대사출속도  141 non-null    float64
#  21  감압시간    141 non-null    float64

# 결측 있는 행과 열을 삭제하고 크기 변화 확인

# 원본 크기를 shape로 확인
print(df.shape)  # (250, 22)

# dropna로 결측 있는 행을 모두 삭제
print(df.dropna().shape)  # (76, 22)

# 방향을 열로 바꿔 결측 있는 열을 삭제
print(df.dropna(axis=1).shape)  # (250, 10)

# 예상 결과
# 250x22 -> 행삭제 76x22, 열삭제 250x10

""" 실습 2) dropna 옵션 조절 """
# how/thresh/subset로 삭제 기준을 세밀하게 조절

# how로 완전히 빈 행만 삭제하는 기준 적용 -> how = 'all'
print(df.dropna(how="all").shape)  # (250, 22)
# 250개 row가 다 살아남았다는 의미
#  : NaN으로 모든 컬럼 내용이 다 채워진 row가 없다는 뜻

# thresh로 값이 일정(예, 20개) 개수 "이상"인 행만 남기기 -> thresh = 20
print(df.dropna(thresh=20).shape)  # (162, 22)
# 250 - 162 = 88개 row는 NaN이 3개 이상이라는 뜻

# subset으로 특정 컬럼이 빈 행만 삭제
# 예, 불량여부 컬럼에 NaN이 있는 row들만 제거 -> subset = ['불량여부']
print(df.dropna(subset=["불량여부"]).shape)  # (250, 22)
# '불량여부' 컬럼에는 NaN이 하나도 없다고 판단 가능

# 예상 결과
# 완전 결측 행만 삭제는 거의 유지, 임계값 20은 162행

import pandas as pd

df = pd.read_csv("data/15_02_사출성형_공정.csv", encoding="utf-8")
print(df.shape)  # (250, 22)
print(df.isna().sum())
# 측정시각        0
# 불량여부        0
# 사출기         0
# 사이클시간       0
# 성형사이클       0
# 배럴온도1       0
# 배럴온도2       0
# 배럴온도3       0
# 배럴온도4       0
# 호퍼온도        0
# 스크루속도       1
# 사출압력        3
# 스크루위치       5
# 전환위치        9
# 계량시간        9
# 계량시작위치     34
# 계량시작점      34
# 최소쿠션       34
# 최대사출압      60
# 전환압력       68
# 최대사출속도    109
# 감압시간      109

""" 실습 3) 결측 비율 기준 컬럼 제거 """
# 결측 비율이 높은 컬럼만 골라 제거

# 단계
# · 컬럼별 결측 비율을 계산
df_rate = df.isna().sum() / len(df)
print(df_rate)
# 측정시각      0.000
# 불량여부      0.000
# 사출기       0.000
# 사이클시간     0.000
# 성형사이클     0.000
# 배럴온도1     0.000
# 배럴온도2     0.000
# 배럴온도3     0.000
# 배럴온도4     0.000
# 호퍼온도      0.000
# 스크루속도     0.004
# 사출압력      0.012
# 스크루위치     0.020
# 전환위치      0.036
# 계량시간      0.036
# 계량시작위치    0.136
# 계량시작점     0.136
# 최소쿠션      0.136
# 최대사출압     0.240
# 전환압력      0.272
# 최대사출속도    0.436
# 감압시간      0.436

# · 비율이 기준을 넘는 컬럼 이름만 목록으로 뽑기
# -> 40% 이상 NaN으로 채워진 컬럼 목록
df_terminates = df_rate[df_rate > 0.4]
print(df_terminates)
# 최대사출속도    0.436
# 감압시간      0.436

# 최초 컬럼 이름들이 df_terminates의 index labels가 되었다.
list_terminates = df_terminates.index.tolist()  # ['최대사출속도', '감압시간']
print(list_terminates)
# ['최대사출속도', '감압시간']

# · 그 컬럼들을 drop으로 제거하고 크기 확인
# drop에 컬럼을 제시하면 기본동작 : 컬럼을 지워버림
df_final = df.drop(columns=list_terminates)
df_final.info()
#   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   측정시각    250 non-null    object
#  1   불량여부    250 non-null    int64
#  2   사출기     250 non-null    object
#  3   사이클시간   250 non-null    float64
#  4   성형사이클   250 non-null    float64
#  5   배럴온도1   250 non-null    float64
#  6   배럴온도2   250 non-null    float64
#  7   배럴온도3   250 non-null    float64
#  8   배럴온도4   250 non-null    float64
#  9   호퍼온도    250 non-null    float64
#  10  스크루속도   249 non-null    float64
#  11  사출압력    247 non-null    float64
#  12  스크루위치   245 non-null    float64
#  13  전환위치    241 non-null    float64
#  14  계량시간    241 non-null    float64
#  15  계량시작위치  216 non-null    float64
#  16  계량시작점   216 non-null    float64
#  17  최소쿠션    216 non-null    float64
#  18  최대사출압   190 non-null    float64
#  19  전환압력    182 non-null    float64

# 예상 결과
# 40% 초과 센서19·20 제거 → 250×20

# ==================================

""" 실습 4) 삭제 손실 비교 """
# 삭제 방식별 남는 행 수와 손실률을 표로 비교

# 단계
# · 원본·행삭제·thresh 각 방식의 남는 행 수 구하기
# · 방식과 행 수를 하나의 표로 모으기

비교 = pd.DataFrame(
    {
        "방식": ["원본", "행삭제", "thresh20"],
        "행": [len(df), len(df.dropna()), len(df.dropna(thresh=20))],
    }
)

비교["손실률"] = ((1 - 비교["행"] / len(df)) * 100).round(2)

print(비교)
#          방식    행   손실률
# 0        원본  250   0.0
# 1       행삭제   76  69.6
# 2  thresh20  162  35.2

# 위 코드는 너무 고급기술 - DF의 더 깊은 이해 경험 필요
# 여러분은 그냥 개별 3가지 항목들을 따로따로 계산시켜 출력해도 괜찮아요


# · 원본 대비 손실률을 백분율로 계산해 나란히 보기

# 예상 결과
# 행삭제 손실 약 70%, thresh 손실 약 35%

# ====================================

""" 실습 5) fillna 평균·중앙값 대체 """
# 결측을 평균과 중앙값으로 채우고 차이 이해
print(df["최대사출압"].isna().sum())  # 60개 NaN 확인

# · 대상 컬럼의 평균과 중앙값을 각각 구해 비교
# · fillna로 평균을 채운 결과 만들기
mean = df["최대사출압"].mean()
print(f"최대사출압의 평균 : {mean}")
# 최대사출압의 평균 : 1241.6723684210526

s_fillmean = df["최대사출압"].fillna(mean)
print(s_fillmean)
# 0      1241.672368
# 1      1241.672368
# 2      1235.220000
# 3      1240.090000
# 4      1241.672368
#           ...
# 245    1237.590000
# 246    1238.090000
# 247    1241.672368
# 248    1241.672368
# 249    1232.610000

df["최대사출압"] = s_fillmean
print(df["최대사출압"].isna().sum())  # 최대사출압 컬럼의 NaN 0개

# · fillna로 중앙값을 채운 결과 만들기(이상치에 강함)
median = df["최대사출압"].median()
print(f"최대사출압의 중앙값 : {median}")
# 최대사출압의 중앙값 : 1240.84

s_fillmedian = df["최대사출압"].fillna(median)
print(s_fillmedian)
# 0      1241.672368
# 1      1241.672368
# 2      1235.220000
# 3      1240.090000
# 4      1241.672368
#           ...
# 245    1237.590000
# 246    1238.090000
# 247    1241.672368
# 248    1241.672368
# 249    1232.610000

df["최대사출압"] = s_fillmedian
print(df["최대사출압"].isna().sum())  # 최대사출압 컬럼의 NaN 0개

# 예상 결과
# 센서17 평균 466.26·중앙값 465.9로 대체, 남은 결측 0

# =============================================

""" 실습 6) 최빈값·앞뒤 값 대체 """
# 범주형은 최빈값, 시계열은 앞뒤 값으로 채우기

# · 범주형 열의 최빈값을 구해 채우기
# 사출기 컬럼은 1혹기~3호기 범주형으로 판단
print(df["사출기"].isna().sum())  # 억지로 3개 만들어봤어요!
print(df["사출기"].mode()[0])  # 1호기가 가장 많다고 함

df["사출기"] = df["사출기"].fillna(df["사출기"].mode()[0])
print(df["사출기"].isna().sum())  # 다시 채워서 0개!

# · 측정시각 순으로 정렬해 시계열 순서 만들기
df = df.sort_values("측정시각")

# · ffill로 앞 값, bfill로 남은 앞쪽 결측까지 채우기
print(df["전환압력"].isna().sum())  # 68개 NaN 확인
df["전환압력"] = df["전환압력"].ffill().bfill()  # 자주 볼 시계열 채우기 패턴
print(df["전환압력"].isna().sum())  # 0개 NaN 확인

# 예상 결과
# 설비명은 최빈값(절삭기A), 온도는 앞뒤 값으로 대체

# ==============================================

""" 실습 7) 그룹별 대체 """
# 그룹별 평균으로 채워 집단 특성 반영

# · 제품유형으로 그룹을 나누기
print(df.groupby("사출기")["감압시간"].mean())
# 사출기별로 감압시간 평균이 다른 것 확인
# 1호기    0.322179
# 2호기    0.322368
# 3호기    0.322400

# · 각 그룹의 평균으로 그 그룹의 결측을 채우기

# 사출기별로 그룹을 나누고
# 그룹마다 갑압시간의 시리즈를 뽑아서
# 그 시리즈의 NaN들을 그 시리즈의 평균들로 채운다
df["감압시간"] = df.groupby("사출기")["감압시간"].transform(
    lambda s: s.fillna(s.mean())
)

print(df["감압시간"].isna().sum())  # 0

# · 남은 수치 결측은 전체 중앙값으로 마무리하고 검증
# 이런 코드는 실제로 할 가능성이 전혀 없음 - 컬럼의 특성고려 없이 NaN을 다 채운다?
df_numbers = df.select_dtypes("number")
df[df_numbers.columns] = df_numbers.fillna(df_numbers.median())

print(df.isna().sum())
# 측정시각      0
# 불량여부      0
# 사출기       0
# 사이클시간     0
# 성형사이클     0
# 배럴온도1     0
# 배럴온도2     0
# 배럴온도3     0
# 배럴온도4     0
# 호퍼온도      0
# 스크루속도     0
# 사출압력      0
# 스크루위치     0
# 전환위치      0
# 계량시간      0
# 계량시작위치    0
# 계량시작점     0
# 최소쿠션      0
# 최대사출압     0
# 전환압력      0
# 최대사출속도    0
# 감압시간      0

print(df.isna().sum().sum())  # 0

# 예상 결과
# 토크를 유형별 평균으로 대체, 남은 결측 0

# ======================================

""" 실습 8) 제거 vs 대체 비교 """
# 같은 데이터에 제거와 대체를 적용해 결과 비교

# · 결측 심한 컬럼을 먼저 뺀 기준 데이터 만들기
print(df.isna().sum())
# 최대사출속도    109
# 감압시간      109
기준 = df.drop(columns=["최대사출속도", "감압시간"])
기준.info()  # 최대사출속도, 감압시간 컬럼 제거 확인
print(기준.shape)  # (250, 20)

# · 기준 데이터에서 결측 행을 삭제한 제거 버전 만들기
제거판 = 기준.dropna()
print(제거판.shape)  # (110, 20)

# · 기준 데이터의 결측을 중앙값으로 채운 대체 버전 만들기
대체판 = 기준.fillna(기준.median(numeric_only=True))
print(대체판.shape)  # (250, 20)

# 예상 결과
# 제거 버전 110행, 대체 버전 250행(모두 유지)

# =======================================

""" 실습 9. SECOM·AI4I 종합 처리 """
# 제거와 대체를 조합해 전체 결측을 처리하고 저장

# · 결측 비율 높은 컬럼을 제거하고 나머지는 중앙값으로 채우기
# 앞서 처리한 대체판 재사용!

# · 처리 후 남은 결측과 크기를 확인하고 파일로 저장
print(대체판.isna().sum().sum())  # 0
대체판.to_csv("data/15_02_사출성형_공정_clean.csv", index=False, encoding="utf-8")

# · 같은 절차를 AI4I 데이터에도 반복해 결측 0 확인

# 예상 결과
# SECOM 결측 0·저장, AI4I 결측 0
