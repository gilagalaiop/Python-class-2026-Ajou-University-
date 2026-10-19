num = input("번호 입력(1:온도, 2. 무게, 3. 길이): ")

if num == "1":
    temp = float(input("변환할 값 입력: "))
    cal_1 = (temp - 32) / 1.8
    print(f"변환 결과: {cal_1:.2f}도(c)")

elif num == "2":
    mass = float(input("변환할 값 입력: "))
    cal_2 = mass * 0.453592
    print(f"변환 결과: {cal_2:.2f}kg")

elif num == "3":
    length = float(input("변환할 값 입력: "))
    cal_3 = length *  2.54
    print(f"변환 결과: {cal_3:.2f}cm")

else:
    print("메뉴 선택 오류")
    
