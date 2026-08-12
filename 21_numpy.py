numbers = [1, 2, 3, 4, 5]

numbers_10 = []

for number in numbers:

    # print(number)
    numbers_10.append(number * 10)

print(numbers_10)

# 파이썬에서 기본 제공하는 기능들 의미
# 다양한 외부 라이브러리들을 가져오려면
# pypi.org 사이트에서 검색부터 하기

# 터미널에서 바로 pip로 설치를 시도하면 (pip install numpy)
# 전체 시스템에 영향을 주는 설치로 생각되어 거절당함
# 그래서 개발 Working Directory마다 별도의 환경을 구축해
# 그 안에 개별 프로젝트가 사용할 pip 라이브러리들을 따로 받아 쓰게 함
# 이것이 바로 가상환경(view)

# 1. 현재 경로에 가상환경 생성
# python -m venv .venv

# 2. 가상환경 활성화
# source .venv/bin/activate
# (이후에는 가상환경 안에서 터미널 명령 실행 가능)

# 3. (작업/실행 끝나고) 가상환경 종료
# deactivate

import numpy as np

numbers = [1, 2, 3, 4, 5]
# 위 int값들의 리스트를 사용해서 numpy의 배열 만들기
np_numbers = np.array(numbers)
print(np_numbers)

numbers = [1, 2, 3, 4, 5]

numbers_10 = []

for number in numbers:

    # print(number)
    numbers_10.append(number * 10)

print(numbers_10)

# 파이썬에서 기본 제공하는 기능들 의미
# 다양한 외부 라이브러리들을 가져오려면
# pypi.org 사이트에서 검색부터 하기

# 터미널에서 바로 pip로 설치를 시도하면 (pip install numpy)
# 전체 시스템에 영향을 주는 설치로 생각되어 거절당함
# 그래서 개발 Working Directory마다 별도의 환경을 구축해
# 그 안에 개별 프로젝트가 사용할 pip 라이브러리들을 따로 받아 쓰게 함
# 이것이 바로 가상환경(view)

# 1. 현재 경로에 가상환경 생성
# python -m venv .venv

# 2. 가상환경 활성화
# source .venv/bin/activate
# (이후에는 가상환경 안에서 터미널 명령 실행 가능)

# 3. (작업/실행 끝나고) 가상환경 종료
# deactivate

import numpy as np

numbers = [1, 2, 3, 4, 5]
# 위 int값들의 리스트를 사용해서 numpy의 배열 만들기
np_numbers = np.array(numbers)
print(np_numbers)


import numpy as np

# 파이썬의 리스트로부터 Numpy 배열 만들기
temp = np.array([70.5, 69.8, 73.7])

print(temp)  # [70.5 69.8 73.7] 항목 사이에 콤마 없음 주의

# 배열의 항목들마다 +5씩 더하려면?
# 리스트였다면 for문으로 돌려서 항목마다 직접 처리했어여야 함
# Numpy라면 간단하게
print(temp + 5)  # [75.5 74.8 78.7]

# 소숫점 이하가 없는 숫자 타입들로 가득한 배열
print(np.array([1, 2, 3, 4, 5]))  # [1 2 3 4 5]

# 소숫점 이하가 있는 것 없는 것이 섞여 있다면
# 모두 소숫점 이하가 있는 것으로 배열 생성
print(np.array([1, 3, 5, 3.14, 6.7, 4]))
# [1.   3.   5.   3.14 6.7  4.  ]

# 실습 1을 위한 참고 코드
# 미국식 속도(miles)를 우리가 쓰는 속도(km)로 변환시켜주는
# Numpy 배열 예제 코드

import numpy as np

miles = np.array([94.7, 104.5, 105.5])
# 속도(km/h)=속도(mph)x1.60934

print(miles * 1.60934)
# [152.404498 168.17603  169.78537 ]

import numpy as np

# 0부터 4까지 생성 (5는 제외)
under_five = np.arange(5)
print(under_five)  # [0 1 2 3 4]

# 0부터 8까지 2씩 간격
gab_two = np.arange(0, 10, 2)
print(gab_two)  # [0 2 4 6 8]

import numpy as np

# linspace
# 개수 중심 균등 분할
# 시작과 끝 구간을 지정한 개수만큼 정확히 나눔
# 간격은 알아서 계산하도록 함

# 0부터 1까지 5개로 균등 분할
div_five = np.linspace(0, 1, 5)
print(div_five)  # [0.   0.25 0.5  0.75 1.  ]

# 0으로 채우기
block_zeros = np.zeros(5)
print(block_zeros)  # [0. 0. 0. 0. 0.]

# 명시적으로 7.0처럼 float값을 지정해줘야
# float 타입 값으로 채워지는 배열이 만들어짐
block_seven = np.full(4, 7)
print(block_seven)  # [7 7 7 7]

""" 실습 2 """
# 0부터 30까지 6 간격으로 배열 채워만들기

import numpy as np

# 0부터 숫자 6 씩 증가시켜가면서 30보다 작은 값들일 때 배열에 붙여나감
gab_six = np.arange(0, 30, 6)

# 0부터 30까지 6등분 나누어 배열 내용 채우기
div_six = np.linspace(0, 30, 6)
print(div_six)  # [ 0.  6. 12. 18. 24. 30.]

""" 실습 3 """
# 측정 시간축 배열 만들기
import numpy as np

# 특정 시간 시각과 끝 시각을 정해서
# 특정 간격 시간들이 지난다면
# 언제 언제 체크포인트가 만들어지나를
# numpy의 배열로 알아보기

# 예를 들어 0초부터 60초 사이에
# 5초 간격으로 체크를 한다면
# 실제로는 몇 초, 몇 초... 체크하는 지점이 생기나 알아보기
checks = np.arange(0, 60, 5)
print(checks)  # [ 0  5 10 15 20 25 30 35 40 45 50 55]

# 2차원
import numpy as np

# 기존 파이썬 리스트로 2차원을 표현
dim_2_list = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [2, 4, 6, 8, 10],
    [3, 6, 9, 3, 6],
]
print(dim_2_list[0][0])  # 1
print(dim_2_list[1][1])  # 7

# 실습1)
import numpy as np

c = np.array([17, 25, 34, 40])
print("화씨 온도:", c * 1.8 + 32)  # 화씨 온도: [ 62.6  77.   93.2 104. ]

# 실습 2)
import numpy as np

div_eight = np.linspace(0, 28, 8)
print(div_eight)  # [ 0.  4.  8. 12. 16. 20. 24. 28.]

# 실습 3)
import numpy as np

checks = np.arange(0, 45, 9)
print(checks)  # [ 0  9 18 27 36]

checks_1 = np.arange(0, 35, 7)
print(checks_1)  # [ 0  7 14 21 28]

# 실습 4)
attri = np.array([[24, 35, 56], [35, 75, 89]])

print("차원", attri.ndim)  # 차원 2
print("형태:", attri.shape)  # 형태: (2, 3)
print("개수:", attri.size)  # 개수: 6

# 실습 5)
flo = np.array([22.4, 53.2, 75.6, 85.9])
print(flo.dtype)  # float64
print(flo.astype(int))  # [22 53 75 85]
