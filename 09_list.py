# list는 python의 자료형 중 하나
# 여러 개의 값을 [대괄호]에 감싸서 순서대로 저장
# 나열된 값들은 자동으로 각자의 인덱스 번호를 순서대로 가지게 됨

temps = [35, 36, 37, 38]  # int 인덱스
float_temps = [36.4, 36.5, 36.6, 36.7]  # float 리스트
machines = ["펌프", "압축기", "모터"]  # string 리스트

# 리스트는 자료형이 달라도 한 리스트에 담을 수 있음
mixed = ["펌프", 78, True]

# 리스트에 자동으로 순서 인덱스가 붙는다면?
print(temps[2])  # 37 > 인덱스로 해당 순서에 위치한 요소 뽑아내기 가능

# 리스트 안에 몇 개의 값이 담겼는지 모르지만 마지막 요소를 뽑고 싶다면?
print(temps[-1])  # 가장 마지막 요소 출력

# 빈 리스트
empty = []

# 리스트에 담긴 값의 갯수 세기
# len() 내장함수 사용
print(len(temps))  # 4
print(len(empty))  # 0

# 리스트에 담긴 값의 갯수 변수에 저장
temps_length = len(temps)  # 변수에 4라는 값이 할당
print(temps_length)  # 4

"""실습 1"""
temps = [34, 36, 34, 37, 38]
print(temps)  # [34, 36, 34, 37, 38]
print(len(temps))  # 5

empty = []
print(empty)  # []
print(len(empty))  # 0

# 리스트의 인덱스
print(temps[0], temps[-1])  # 가장 첫 번째 요소, 가장 마지막 요소
# -1을 사용하는 이유는 최신 값은 대체로 뒤에 추가가 됨
# 가장 최신 값은 결국 마지막 인덱스의 요소
# len 함수를 사용해서 리스트 길이 01로 계산이 가능하지만
# 이 작업이 번거로워 -1을 가장 많이 사용

# 없는 인덱스 호출
# temps 리스트는 길이가 5
# print(temps[5]) # IndexError: list index out of range
# 인덱스 범위를 벗어나지 않도록 유의

""" 실습 2 """
line = [123, 34, 67, 27, 94, 452]
print(line[0])  # 123
print(line[2])  # 67
print(line[-1])  # 452

""" 실습 3 """
line = [123, 34, 67, 27, 94, 452]
line_1 = line[0]
line_2 = line[-1]
print(line_1 + line_2)  # 575
print((line_1 + line_2) / 2)  # 287.5

# f 스트링 활용해서 똑같은 값 출력하기
print(f"temps[0]: {temps[0]}")  # 34
print(f"type(temps[0]: {type(temps[0])})")  # type(temps[0]: <class 'int'>)

# 인덱싱 vs 슬라이싱
# 인덱싱 temps[0]은 값 하나(35)
# temps[999]와 같이 없는 인덱스를 사용 시 에러
# 슬라이싱 temps[0:2]은 리스트([35, 36])
# 슬라이싱은 영역을 잘라내는 역할이기 때문에 리스트를 반환하는 것
# temps[100:999] 에러 발생하지 않음
# 슬라이싱은 '있는 만큼만' 잘라내기 때문에 애러 발생하지 않음

# 인덱스로 특정 값 바꾸기
# temps = [35, 36, 37, 38]

print("원본:", temps)
temps[2] = 999
print("2번 인덱스 값 변경 결과:", temps)
""" 실습 4 """
temps = [23, 44, 24, 46, 56, 76, 84, 56, 25, 36]
print(temps[:3])  # [23, 44, 24]
print(temps[-3:])  # [56, 25, 36]
print(len(temps[:3]))  # 3

""" 실습 5 """
temps = [23, 44, 24, 46, 56, 76, 84, 56, 25, 36, 52, 57]
first = temps[:6]
print(len(first))  # 6
second = temps[-6:]
print(len(second))  # 6

""" 실습 6 """
temps = [35, 36, 370, 38, 39]
print(370 in temps)  # True
mis = temps.index(370)
temps[mis] = 37
print(temps)  # [35, 36, 37, 38, 39]
print(370 in temps)  # False

# 리스트 값 추가
# .append(추가할 값)
# 리스트의 가장 마지막에 값을 추가
# 리스트 원본이 수정 (재할당 필요 X)
nums = [1, 2, 3, 4, 5]

nums.append(999)
print(nums)

# 원본 리스트를 복사해서 리스트 수정 진행
# nums = [1, 2, 3, 4, 5, 999]
new_nums = nums
print(new_nums)

new_nums.append(111)
print("원본 nums 리스트:", nums)
print("복사본 new_nums에 111 append 결과:", new_nums)

# 복사하 메모리 주소에 append를 했기 때문에 원본까지 영향을 받음
new_nums2 = nums.copy()
new_nums2.append(222)  # nums 배열에 영향을 미치지 않고 사용
print("원본 nums 리스트:", nums)
print("복사본 new_nums2에 222 append 결과:", new_nums2)

# .insert(위치, 값)
# 리스트에서 원하는 위치에 값을 삽입
# 원본 배열에 바로 삽입
# 기존 배열에서 삭제는 되지 않고, 해당하는 인덱스 값이 삽입 (뒤에 요소들은 인덱스 + 1)
nums.insert(3, 333)
print(nums)

# extend()
# 다른 리스트의 값들을 풀어서 이어붙임
data = [1, 2, 3]
new_data = [7, 8, 9]
sum_data = data.extend(new_data)
# data.extend(new_data) 똑같은 결과가 나옴
print(sum_data)
print("===")

# 함수의 반환 개념을 안 뒤에 확인할 내용
print(data.extend(new_data))
# 기대 출력 결과 :[1, 2, 3, 7, 8, 9]
# 실제 결과 : None
# extend() 메서드는 data라는 리스트를 "수정" 이를 반환하지 않음
# 반환값이 없어서 print를 할 것이 없는 것
print(data)  # [1, 2, 3, 7, 8, 9]

# 정리
# 오늘 꼭 알아야 하는 리스트 수정 메서드와 개념
# .append(추가할 값) : 리스트의 가장 마지막에 값을 추가
# .insert(위치, 값) : 첫 번째 인자인 위치 인덱스에 값을 삽입
# .extend(합칠 리스트) : 두 리스트를 하나의 리스트로 합체
# 위 세가지 메서드들은 원본 리스트 자체를 수정

# 리스트를 수정하는 메서드는 모두 반환값이 없는가?
print(data.append(123))  # None
print(data.insert(0, 123))  # None
print(data.extend(new_data))  # None
# 일단 현재 배운 메서드들은 반환값이 없음

""" 실습 7 """
empty = []
empty.append(4)
print(empty)  # [4]
empty.insert(0, 15)
print(empty)  # [15, 4]
empty.extend([22, 41])
print(empty)  # [15, 4, 22, 41]

# 위 세 가지 메서드들은 원본 리스트 자체를 수정

# 리스트에서 요소 삭제
# .remove(값) : 위치는 모르고 삭제할 "값"만 알 때 사용하는 요소 삭제 메서드
list1 = [1, 2, 3, 4, 5, 6]
list1.remove(5)
print(list1)  # [1, 2, 3, 4, 6]

list2 = ["딸기", "사과", "배", "포도", "수박", "망고"]
list2.remove("수박")
print(list2)

# .pop(인덱스): 인덱스로 특정 요소를 삭제할 때 사용
# 삭제한 인덱스의 값을 반환
list1.pop(0)
print(list1)
print(list1.pop(2))  # 삭제한 인덱스 2번의 값인 포도 출력
# 삭제도 하고, 삭제한 인덱스 값도 출력
print(list1)
# del: 인덱스로 리스트의 요소 삭제 (슬라이싱으로 영역 삭제 가능)
del list1[0]
print(list1)

# 없는 인덱스로 값 삭제 시도 -> 삭제 불가
# list1.pop(999)
# print(list1) # Index Error 발생

# del list[:]
# print(list1)  # [] > 빈 리스트가 됨

# del 건너뛰기
list2 = ["빨강", "노랑", "초록", "파랑", "보라", "남색", "보라"]
del list2[::2]  # "빨강", "초록", "남색"을 삭제하겠다는 의미
print(list2)  # ['노랑', '파랑', '보라]

del list2[100:300]  # 슬라이싱 할 값이 없기 때문에 그대로 유지 > Error 나지 않음
print(list2)

""" 실습 8 """
num = [144, 354, 666, 999, 643, 678]
num.remove(999)
print(num)  # [144, 354, 666, 643, 678]
num.pop(2)
print("꺼낸 값", num)  # 꺼낸 값 [144, 354, 643, 678]
del num[0]
print(num)  # [354, 643, 678]

# 리스트 정렬하기
# 리스트.sort()
# 데이터 정렬
# 기본적으로 오름차순(작은 숫자부터 큰 숫자까지)
# 내림차순으로 정렬하고 싶은 경우에는 .sort(reverse = True)

n = [37, 2, 8, 109, 1004, -1, 22]
print("n 리스트 원본:", n)

# 오름차순 정렬
n.sort()  # 원본 리스트 수정
print("n 리스트 오름차순 정렬 결과:", n)

# 내림차순 정렬
n.sort(reverse=True)
print("n 리스트 내림차순 정렬 결과:", n)

# 리스트 순서 뒤집기
# .reverse()
# 값의 크기대로 정렬은 해주지 않음
# 뒤로 계속 쌓인 결과(최신)을 앞에서부터 보고싶을 때 사용

n = [37, 2, 8, 109, 1004, -1, 22]
print("n 리스트 원본:", n)

n.reverse()
print("n 리스트 순서 뒤집기 결과:", n)

# 리스트 안 값의 갯수 구하기
# .count(찾을 값)

f = ["텀블러", "일회용컵", "일회용컵", "텀블러", "텀블러", "일회용컵"]
print(f.count("일회용컵"))
print(f)  # 원본 배열에 변화 없음

# 특정 값의 위치 찾기
# .index(위치를 찾을 값)
# 리스트에서 가장 첫 위치만 찾아줌
print(f.index("일회용컵"))  # 1
print(f)  # 원본 배열에 변화 없음

""" 실습 9 """
temps = [25, 43, 25, 40, 14, 31]
temps.sort()
print(temps)  # [14, 25, 25, 31, 40, 43]
temps.reverse()
print(temps)  # [43, 40, 31, 25, 25, 14]
print(temps.count(25))  # 2
print(temps.index(25))  # 3
