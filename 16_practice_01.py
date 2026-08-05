# 종합 실습 1
print("==================================================")
print("             설비 종합 모니터링 리포트           ")
print("==================================================")
sensors = [
    ("컨베이어_01", 78, 2.1),
    ("용접기_02", 92, 5.4),
    ("절단기_03", 85, 3.2),
    ("건조로_04", 101, 6.8),
    ("냉각탑_05", 67, 1.5),
    ("도장부스_06", 88, 4.1),
    ("성형기_07", 90, 2.9),
]
i = []  # 위험
j = []  # 주의
k = []  # 정상

all_temps = []
max_temp = 0
max_temp_sensor_name = ""

for name, temp, vibe in sensors:
    all_temps.append(temp)
    if temp > max_temp:
        max_temp = temp
        max_temp_name = name

    if temp > 90 or vibe > 5.0:
        print(name, "| 온도", temp, "| 진동", vibe, "| 위험 🚨 ")
        i.append(name)
    elif temp >= 80 or vibe >= 3.0:
        print(name, "| 온도", temp, "| 진동", vibe, "| 주의 ⚠️")
        j.append(name)
    else:
        print(name, "| 온도", temp, "| 진동", vibe, "| 정상 ✅")
        k.append(name)
print("------------------------------------------------")
print("총 설비:", len(sensors))
print("정상:", len(k), "/ 주의:", len(j), "/ 위험:", len(i))
print("이상 설비 비율:", round((len(i + j) / len(i + j + k) * 100), 1), "%")
print("평균 온도:", round(sum(all_temps) / len(all_temps), 1), "℃")
print("최고 온도 설비:", max_temp_name, "(", max_temp, "℃ )")
print("위험 설비 목록:", i)
print("=================================================")
