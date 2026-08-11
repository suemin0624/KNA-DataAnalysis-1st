# 1. 현재 경로에 가상환경 생성

# 2. 가상환경 활성화
# python -m venv .venv
# source .venv/bin/activate
# pip3 install numpy

import numpy as np

a = np.array([70, 72, 71, 95, 73])
print(a[0], a[-1])  # 70 73
print(a[1:4])  # [72 71 95]

b = np.array([[70, 2.1], [72, 2.3], [71, 1.9]])
print(b.shape)  # (3,2)
print(b[1])  # [72.   2.3]
print(b[0][1])  # 2.1

print(b[:, 0])  # [70. 72. 71.]
# 모든 배열의 0 자리에 위치 한 값을 배열로 만들어 줌

# 실습 1) 스핀들 회전수(RPM) 센서 배열 실습
rpm = np.array([1551, 1408, 1498, 1433, 1425, 1558, 2861, 1410])
print(rpm[0], rpm[-1])  # 1551 1410
print(rpm[1:4])  # [1408 1498 1433]
print(rpm[::2])  # [1551 1498 1425 2861]

# 실습 2) 행.열 단위로 추출하기
data2 = np.array([[1551, 42.8], [1408, 46.3], [2861, 4.6], [1410, 65.7]])
print(data2[2])  # [2861.     4.6]
print(data2[:, 0])  # [1551. 1408. 2861. 1410.]
print(data2[:, 1])  # [42.8 46.3  4.6 65.7]

import numpy as np

# 배열의 산술 연산
# 두 배열을 같은 위치끼리 한 번에 계산
x = np.array([1, 2, 3])
y = np.array([10, 20, 30])
print(x + y)  # [11 22 33]
print(x * 2)  # [2 4 6]
print(x * y)  # [10 40 90]

# 배열 안의 섭씨 온도들을 화씨 온도로 바꿔 출력하기
celsius = np.array([20.0, 25.0, 30.0])
# 화씨온도 = 섭씨온도 * 1.8 + 32
f = celsius * 1.8 + 32
print(f)  # [68. 77. 86.]

# 스칼라 연산은 위 예제처럼
# 배열 전체에 항목마다 계산시켜 다시 새로운 배열 만들기

# 브로드 캐스팅
# 한 줄짜리 기준값이 모든 행에 퍼져서 계산
table = np.array([[72, 2.3], [95, 6.8]])

base = np.array([70, 2.0])

# table의 각 행에서 기준값(base)을 빼기
print(table - base)  #  [25.   4.8]]

# 실습 3) 세서값 정규화 하기
# 화전 수 측정 배열 준비
rpm3 = np.array([1551, 1408, 1498, 1433, 1425, 2861])

# 최솟값과 최댓값을 min, max로 확인
print(rpm3.min())  # 1408
print(rpm3.max())  # 2861

# 정규화 공식을 브로드캐스팅으로 적용해 변환
# 정규화 공식
# 정규화된 x =(비교대상 - 최솟값) / (최댓값 - 최솟값)
rpm_min = rpm3.min()
rpm_max = rpm3.max()
normalized = (rpm3 - rpm_min) / (rpm_max - rpm_min)
print(normalized)  # [0.09841707 0.         0.06194081 0.01720578 0.01169993 1.        ]
# 소숫점 이하값이 너무 길어진다면 numpy 배열에서 제공하는 round 기능을 활용
print(np.round(normalized, 2))
# [0.1  0.   0.06 0.02 0.01 1.  ]

# 비교 연산과 불리언 배열
v = np.array([70, 95, 71, 88, 73])
print(v > 85)  # [False  True False  True False]

# Boolean indexing
# 불리언 배열로 조건에 맞는 값만 골라내기
print(v[v > 85])  # [95 88]

# np.where
# 조건에 따라 값을 둘 중 하나로 바꾸기
# - 조건/참/거짓 ... 세 가지 인자
# 조건이 참이면 1(위험)
# 거짓이면 0(정상)
print(np.where(v > 85, 1, 0))  # [0 1 0 1 0]

# 다중 조건 결합
print(v)  # [70 95 71 88 73]
v_step1 = v[v > 70]
print(v_step1)  # [95 71 88 73]
v_step2 = v_step1[v_step1 < 90]
print(v_step2)  # [71 88 73]

v_mixed = v[(v > 70) & (v < 90)]
print(v_mixed)  # [71 88 73]

# 참고, 조건 대신 True를 준다면?
print(v[True])  # [[70 95 71 88 73]]

# 실습 4)
# 조건에 맞는 이상 센서값만 불리언 인덱싱으로 선별

# 회전수와 토크 배열 준비
rpm4 = np.array([1551, 1408, 1498, 2861, 1425, 1410])
torque4 = np.array([42.8, 46.3, 49.4, 4.6, 41.9, 65.7])
# 비교 연산으로 회전수가 기준을 넘는 조건 생성 -> 2000 이상
print(rpm4[rpm4 > 2000])

# 다중 조건으로 회전수 과다 또는 초크 과소 위험 시점 필터링
# -> rpm[0] 데이터와 torque[0] 데이터는 같은 시기의 상황을 다룸
print((rpm4 > 2000) | (torque4 < 10))

# 예상 결과
# 기준 초과 회전수 값과, 위험 조건을 만족하는 위치가 출력
# [False False False  True False False]

# 실습 5) 조건별 개수와 비율 세기
# 조건을 만족하는 값의 개수와 전체 대비 비율 계산
torque5 = np.array([42.7, 46.3, 49.4, 4.6, 41.9, 65.7, 40.2, 60.7])
# 토크 배열 준비
# 비교 조건으로 참/거짓 불리언 배열 생성
high5 = torque5 > 50  # 문제에서 요구하는 코드
print(high5)

print(torque5[torque5 > 50])  # 참고 코드 [65.7 60.7]

# 불리언 배열의 합(sum)으로 개수. 평균(mean)으로 비율 계산
print(high5.sum())  # 2
print(round(high5.mean(), 2))  # 0.25

# 예상 결과
# 조건을 만족하는 값의 개수와 비율이 출력

temp = np.array([11.23242, 453.212421412, 3242.121222])
print(np.round(temp, 2))

# 합계와 평균(mean)
s = np.array([70, 72, 71, 95, 73])
print(s.sum())  # 합계: 381
print(s.mean())  # 평균: 76.2
# 평균의 약점 : 유난히 크거나 작은 값(이상치)에 휘둘림


# 다른 통계와 달리 np.median() 이용
print(np.median(s))  # 중앙값: 72.0
# 중앙값의 강점 : 이상치에 흔들리지 않음

# 최대/최소 범위
print(s.max())  # 최댓값: 95
print(s.min())  # 최솟값: 70
print(s.max() - s.min())  # 범위: 25

# 분산
stables = np.array([70, 71, 70, 72, 71])
unstables = np.array([60, 85, 65, 95, 70])

print(stables.var())  # 0.5599999999999999
print(round(stables.var(), 2))  # 0.56

print(unstables.var())  # 170.0
print(round(unstables.var(), 2))  # 170.0
# 분산의 한계: 값을 제곱해 구하므로 단위가 달라짐

# 표준편차
s2 = np.array([70, 72, 71, 95, 73])
print(round(s2.var(), 2))  # 분산: 89.36
print(round(s2.std(), 2))  # 표준편차: 9.45

# axis 개념 (행과 열의 방향)
mat = np.array([[70, 2.1], [72, 2.3]])

print(mat.mean())  # 36.6
# axis = 0 -> 열별 결과
print(mat.mean(axis=0))  # 열별 평균 : [71.   2.2]
# axis = 1 -> 행별 결과
print(mat.mean(axis=1))  # 행별 평균 : [36.05 37.15]

# 실습 6) 센서별 기초 통계 구하기
# 표 모양 데이터에서 센서별(열별) 통계 계산
fac = np.array([[45, 2], [53, 6]])
print(fac.mean(axis=0))  # [49.  4.]
print(fac.std(axis=0))  # [4. 2.]

# 실습 7) 파일 데이터로 기초 통계 구하기
# np.loadtxt로 회전수 열을 파일에서 불러오기
rpm7 = np.loadtxt("data/10__mct_tool.csv", delimiter=",", skiprows=1, usecols=4)
print(rpm7.mean())
print(rpm7.std())

# 실습 8) 필터링과 통계 결합하기
# 조건으로 값을 골라낸 뒤 그 값들의 통계 계산
data_bool = np.array([35, 37, 54, 75, 81])
data_bool_final = data_bool[data_bool > 50]
