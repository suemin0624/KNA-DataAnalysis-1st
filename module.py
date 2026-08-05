# 수학 관련 모듈을 불러오기
import math

# 해당 모듈이름 / 함수() 식으로 호출
result = math.sqrt(16)
print(result)

# 수학 관련 모듈에서 sqrt 기능만 불러오기
from math import sqrt

# 이젠 sqrt만 불러도 됨
result = sqrt(16)
print(sqrt)

# -----------------------------------
# math라는 모듈 이름 다 쓰기 귀찮으니 줄여보기
import math as mt

# 별칭으로 가져온 모듈 이름을 언급
result = mt.sqrt(16)
print(result)  # 4.0

# datetime 모듈을 가져오기
import datetime

# datetime의 now()는 현재의 지역 날짜와 시간을 반환
now = datetime.datetime.now()
print(now)  # 2026-08-05 11:21:08.635605

""" 실습 1 """
# import, from import, import as
import math

result = math.floor(4.6)
print(result)  # 4

from math import floor

result = floor(4.6)
print(result)  # 4

import math as mt

mt = math.floor(4.6)
print(mt)  # 4

# math 표준 라이브러리
# math에서 sqrt, ceil 두 개만 사용한다면 이렇게 써도 가능
from math import sqrt, ceil

print(sqrt(9))
print(ceil(4.2))

print(2**3)

# math에서 sqrt, ceil 두 개만 사용한다면 이렇게 써도 됨
from math import sqrt, ceil

print(sqrt(9))
print(ceil(4.2))

# 표준 라이브러리의 random 모듈
import random

print(random.randint(1, 10))
print(random.choice(["정상", "경고", "위험"]))

# 표준 라이브러리의 datetime 모듈
import datetime

# datetime 모듈 안의 datetime 클래스에서 지원하는 now() 함수 호출
now = datetime.datetime.now()
print(now)  #

# 모듈 도움말 보기 : 참고만 하고 구글링한 웹사이트에서 보기
print(dir(math))
help(math.sqrt)

# 절대경로와 상대경로
# 절대경로의 예 뭐시기저시기

# PATH
# documents/project/data/08_press.csv

# import os

# cwd = os.getcwd()
# print(cwd)
# 표준 라이브러리의 os
# os = Operating System
# os.getcwd()

# 파일이 존재하는지 알아보기
# 운영체제마다 경로를 나타내는 방법이 달라서
# 상황에 맞개 경로문자열을 만들어주는 os의 함수를 사용

import os

print("실행 시작")

path = os.path.join("data", "08_press.csv")
print(path)

if os.path.exists(path):
    print(f"파일 있음: {path}")
else:
    print(f"파일 없음: {path}")

import pandas as pd

df = pd.read_csv("data/08_press.csv")
print(df.head())

print("hi")
