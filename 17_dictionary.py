# 리스트로 크루 이름 나열해 보기
data_class_list = ["ㅇㅇ", "ㅅㅅ", "ㄴㄴ"]

# 딕셔너리로 정확하게 역할까지 부여해보기
data_class_dict = {"반장": "ㅇㅇ", "부반장": "ㅅㅅ", "당번": "ㄴㄴ", "기타": "길동"}

# 센서로부터 얻는 예시 데이터로 딕셔너리를 만들어보기
sensors = {"센서이름": "보일러", "모터온도": 78, "진동": 0.5}
print(sensors)  # {'센서이름': '보일러', '모터온도': 78, '진동': 0.5}
print(type(sensors))  # <class 'dict'>
empty = {}  # 빈 딕셔너리 생성
print(type(empty))  # 딕셔너리 타입 확인

# print(sensors{"센서이름"}))
# print(sensors{"모터온도"})
# print(sensors{"진동"})

# 기존에 있던 key의 값을 변경
sensors["센서이름"] = "펌프"  # 센서이름 값 변경
print(sensors)

# 더 이상 필요넚는 ket와 그 value를 삭제
del sensors["모터온도"]
# 기존에 없던 key의 값을 추가
sensors["펌프입력"] = 95
sensors["유량"] = 42

print(sensors)

# print(sensors["모터온도"])  # 더 이상 없는 key를 호출하면 에러 발생
# KeyError: '모터온도'

print(sensors.get("센서이름"))
# print(sensors.get("모터온도")) # 더 이상 없는 key를 호출하면 None 반환

# motor_degree에는 숫자가 담길거라 생각했는데
motor_degree = sensors.get("모터온도", 0)


# motor_degree에 숫자가 안 담기면 에러 발생
motor_degree = sensors.get("모터온도")
# next_degree = motor_degree + 10
# print(next_degree)

# 위 코드는 보통 이렇게 쓰임
if "모터온도" in sensors:
    print("그런 키 있어요!")
else:
    print("그런 키 없어요!")

# keys를 가져와보기
print(sensors.keys())
# value를 가져와보기
print(sensors.values())
# len을 통해 몇 개의 key-value 조합들이 있는지 살펴보기
print(len(sensors))

for key, value in sensors:
    print(key)
    print(value)

# 위와같이 사용하기 보다는, 의미있는 이름으로 사용
for key, value in sensors:
    print(key)
    print(value)

if len(sensors):
    
# sensors = {"모터온도": 78, "진동": 0.5, "입력": 95}
# print(len(sensors))

# 재미난 사례를 추가로 만들어보기
# 나라 이름들로 정리
# 유럽: 스페인(ESP), 프랑스(FRA), 독일(GER), 스위스(SUI), 네덜란드(NED)
# 아시아: 한국(KOR), 일본(JPN), 중국(CHN), 사우디(SAU), 이란(IRN)
# 남미: 아르헨티나(ARG), 브라질(BRA), 칠레(CHI), 콜롬비아(COL), 우루과이(URU)

korea = {"국가명:", "대한민국", "약칭:", "KOR"}
japan = {"국가명:", "일본", "약칭:", "JPN"}
print(korea)
# 아시아 나라들을 하나의 리스트로 모아보기
aisa= {korea, japan}
print(asia)

# 유럽 나라들을 하나의 리스트로 모아보기
europe = [{"국가명": "스페인", "약칭": "KOR"},
          {"국가명": "프랑스", "약칭": "KOR"},
          {"국가명": "독일", "약칭": "KOR"},
          {"국가명": "스위스", "약칭": "KOR"},
          {"국가명": "네덜란드", "약칭": "KOR"}]
print(europe)

for country in europe:
   print(country.get("국가명","없음"))

   for key, value in country.items():
      print(f"{keys}: {value}")
# 결과값

# 스페인
# 국가명: 스페인
# 약칭: KOR
# 프랑스
# 국가명: 프랑스
# 약칭: KOR
# 독일
# 국가명: 독일
# 약칭: KOR
# 스위스
# 국가명: 스위스
# 약칭: KOR
# 네덜란드
# 국가명: 네덜란드
# 약칭: KOR
   

'''조별과제'''
# 포켓몬 1, 2, 3 진화단계들을 딕셔너리로 만들고
# 그 포켓몬 딕셔너리들이 모인 배열을 만들기
# 그 배열 데이터를 화면에 import 하기
# 가능하면 그 배열의 데이터들을 for-in을 사용해서 하나씩 꺼내 print 하기

poketmon = [{"1단계": "파이리", "2단계":"리자드", "3단계":"리자몽"},
            {"1단계": "꼬부기", "2단계":"어니부기", "3단계":"거북왕"},
{"1단계": "이상해씨", "2단계":"이상해풀", "3단계":"이상해꽃"},
{"1단계": "고오스", "2단계":"고우스트", "3단계":"펜텀"},
 {"1단계": "랄토스", "2단계":"킬리아", "3단계":"가디안"},
  {"1단계": "미뇽", "2단계":"신뇽", "3단계":"망나뇽"},
  {"1단계": "딥상어동", "2단계":"한바이트", "3단계":"한카리아스"},
   {"1단계": "모노두", "2단계":"디헤드", "3단계":"삼삼드래"},
{"1단계": "불꽃숭이", "2단계":"파이숭이", "3단계":"초염몽"},
   {"1단계": "팽도리", "2단계":"팽태자", "3단계":"엠페르트"}]

# 리스트 전체 출력
print(pokemon)

print("-------------------------")

# for-in으로 하나씩 꺼내 출력 1)
for p in pokemon:
  for po in p.items():
    print(po)
print("==========================")

# for-in으로 하나씩 꺼내 출력 2)
for p in pokemon:
    print("1단계:", p["1단계"])
    print("2단계:", p["2단계"])
    print("3단계:", p["3단계"])
    print("========================")

# 두 딕셔너리를 하나씩 꺼내어 key, value 조합으로 하나씩 꺼내어 비교하기
# 다음의 두 딕셔너리는 같은 key들을 가지고 있음
# 실제 데이터
values = {"모터온도": 95, "압력": 88}
# 임계치 데이터
limits = {"모터온도": 90, "압력": 90}

for name, value in values.items():
    print(f"{name} : {value}") # 모터온도 : 95 / 압력 : 88

    if value > limits[name]:
       print(name, "경고") # 모터온도 : 95 / 모터온도 경고 / 압력 : 88

# limits 딕셔너리에도 name의 key가 있다면, 가져와서 비교하기
    #if value > limits.get(name, 0):
       # print(name, "경고")
sensors = {"모터온도": 78, "진동" : 0.5}
new_data = {"모터온도": 80, "유량": 42}
sensors.update(new_data) # 기존 딕셔너리에 새로운 딕셔너리의 key-value 조합을 추가
print(sensors)
# {'모터온도': 80, '진동': 0.5, '유량': 42}

# zip으로 key들의 배열과 values의 배열을 묶어서 새로운 딕셔너리를 만들기
names = ["모터온도", "진동", "압력"]
values = [78, 0.5, 95]
sensors = dict(zip(names, values))
print(sensors)

# 딕셔너리 안에 value로 딕셔너리를 사용하기
kbo = [
   { "구단명": "삼성",
    "마스코트": "라이온스",
    "구장": {
       "1구장": "대구라이온스파크",
       "2구장": "포항야구장"
    }
    },
    {
       "구단명": "두산",
       "마스코트": "베어스",
       "구장": {
       "1구장": "잠실야구장",
       "2구장": "베어스파크" 
       }
    }
]
print(kbo[0]["마스코트"]) # 라이온스
print(kbo[0]["구장"]) # {'1구장': '대구라이온스파크', '2구장': '포항야구장'}
print(kbo[0]["구장"]["2구장"]) # 포항야구장


''' 종합 실습 '''
# 실습 1)
# 1-1) 센서명을 키(key), 측정값을 값(value)으로 딕셔너리 저장
sensors = {"모터온도": 78, 
           "진동": 0.5
           }
# 1-2) 키로 값을 꺼내고 새 키로 추가, 기존 키로 수정
print(sensors("진동")) # 값 꺼내기
print(sensors("진동", 0)) # 값 더 안전하게 꺼내기

sensors["압력"] = 95 # 없던 키를 언급하면 추가
sensors["진동"] = 0.3 # 있던 키를 언급하면 수정

print(sensors)

# 1-3) get으로 없는 키를 기본값으로 조회, in으로 키 존재 확인
print(sensors.get("면적", -1)) # 면적 key는 존재하지 않아서 -1로 대체
print("진동" in sensors) # 존재하는 key
print("면적" in sensors) # 존재하지 않는 key

# 내 방안)
sensors["압력"] = 5 # 추가
sensors = {"모터": 35, "설비": 64, "회로": 48}
print(sensors["모터"]) # 35
print(sensors["설비"]) # 64
print(sensors["회로"]) # 48
sensors["모터"] = 92 
print(sensors) # {'모터': 92, '설비': 29, '회로': 48}
sensors["설비"] = 29
del sensors["모터"]
del sensors["설비"]
sensors["모터"] = 35
sensors["설비"] = 64
print(sensors.get("유량")) # None
if "모터" in sensors:
   print(sensors.get("모터")) # 35

# 실습 2)
sensors = {"모터": 35, "설비": 64, "회로": 48}
new_data = {"유량": 94, "진동": 83}
sensors.update(new_data)
print(sensors) # {'모터': 35, '설비': 64, '회로': 48, '유량': 94, '진동': 83}
del sensors["모터"]
print(len(sensors)) # 4

# 실습 3) 버려버려 
sensors = {"모터": 35, "설비": 64, "회로": 48}

avg = sum(sensors.values()) / len(sensors)
print("평균:",avg)

for name, value in sensors.items():
   print("최댓값 센서:", max())

# 실습 4)
names = {"모터", "설비", "회로"}
values = {47, 26, 78}
sensors = dict(zip(names, values))
print(sensors) # {'회로': 26, '설비': 78, '모터': 47}
for name, value in sensors.items():
   print(f"{name}: {value}") #회로: 26 / 설비: 78 / 모터: 47

# 실습 5)
sensors = {"모터": 35, "설비": 64, "회로": 48}
limits = {"모터": 28, "설비": 50, "회로": 65, "압력": 83}
empty = []
for name, value in sensors.items():
   if value > limits[name]:
      empty.append(sensors[name])
print("경고 센서:",empty) # 경고 센서: [35, 64]

# 실습 6)
machine = {
   "1번 모터" : {
       "온도": 59 ,
       "설비": 53
   },
   "2번 모터" : {
      "설비": 36,
       "압력": 83
   }
}
print(machine["1번 모터"]["온도"]) # 59

# 실습 7) 버려버려
plant = ["온도", 78, "압력", 38, "진동", 94]
for name, value in plant:
   new_plant = plant.split(",")
   name = new_plant[::2]
   value = new_plant[1::2]
   print(f"name""value")

# 실습 8)
sensors = {"모터": 35, "설비": 64, "회로": 48}
limits = {"모터": 28, "설비": 50, "회로": 65}
empty = []
avg = sum(sensors.values()) / len(sensors)
print("평균:", avg) # 평균: 49.0
for name, value in sensors.items():
   if value > limits[name]:
      empty.append(sensors[name])
print("경고 센서:", empty) # 경고 센서: [35, 64]

# 딕셔너리 예제
# 보통 리스트 안에 딕셔너리들이 있다면,
# 그 딕셔너리들은 같은 key들을 갖는 게 일반적
location_dict = {
    "시": [
        {"이름": "서울특별시", "기초단체": ["종로구", "중구", "마포구"]},
        {"이름": "대구광역시", "기초단체": ["중구", "수성구", "달서구"]},
    ],
    "도": [
        {"이름": "경기도", "기초단체": ["수원시", "안양시", "안산시"]},
        {"이름": "경상북도", "기초단체": ["포항시", "경주시", "김천시"]},
    ],
}
# 전체 출력
print(location_dict)
print("-----------------")

# 시와 도 단위 딕셔너리들을 각각 출력하기
print(location_dict["시"])
print(location_dict.get("도"))

# 각 시 도 마다 세부 딕셔너리들을 출력하기
for basic_dict in location_dict["시"]:
  print(basic_dict.get["이름"])
  print(basic_dict.get["기초단체"])
  print("-------------------------")

for basic_dict in location_dict["도"]:
  print(basic_dict.get["이름"])
  print(basic_dict.get["기초단체"])
  print("-------------------------")

# 위 코드를 보면 두 개의 for문이 사실상 같은 일을 함
# 그래서 중복되는 부분을 묶고, 다른점만 외부에서 지적해 시키면 돌아가는
# "함수(fuction)"를 만들면 효율성이 높아짐