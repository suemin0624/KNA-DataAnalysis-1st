import os
import csv
import sys

csv_path = os.path.join("data", "08_press.csv")

# 위 경로의 파일을 찾지 못하면 강제종료 시키기
if not os.path.exists(csv_path):
    print("파일이 없습니다")
    sys.exit(1)  # 비정상 종료시 보통 0이 아닌 값(예 1) 전달

print("파일이 있습니다")

with open(csv_path, "r", encoding="utf-8") as f:
    print(f.readlines())  # 이제 csv 전문가에게 맡기기
    reader = csv.reader(f)

    for row in reader:
        print(row[0])  # 각 행(row)마다 리스트로 출력됨

csv_path = os.path.join("data", "result.csv")

with open(csv_path, "w", encoding="utf-8") as f:

    pass

csv_path = os.path.join("data", "sample.csv")

with open(csv_path, "w", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["시각", "설비"])
    writer.writerow(["09:00", "PUMP-01"])

with open(csv_path, "w", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    # Dictreader는 첫줄은 컬럼 이름으로 판단하고
    # 각 row를 해당 컬럼이름들을 key로 하는 딕셔너리로 만들어줌
    print(reader)

    for row in reader:
        print(row["설비ID"], row.get("시각"))

with open(csv_path, "r", encoding="utf-8") as f:
    # print(f.readlines()) # 이제 csv 전문거에게 맡기기

    reader = csv.reader(f)

    # DictReader가 아닌 그냥 reader를 사용한다면
    # 보통 csv파일의 첫 줄인 헤더줄도 읽어버림
    # reader에게 첫 줄은 건너뛰라고 말하는 방법이 필요
    # next(reader)는 한 줄 건너뛰고 reader가 반응하게 됨
    header = next(reader)
    # header는 따로 리스트로 챙겨짐
    # ['설비', '시각', '진동X', '진동Y', '전류', '상태']
    print(header)

    for row in reader:
        print(row[0])  # 각 행(row)마다 리스트로 출력됨
