days_dictionery = {1: 31, 2: 28, 3: 31, 4: 30, 5:31, 6: 30, 7: 31, 8:31, 9:30, 10:31, 11:30, 12:31}
month = int(input("달을 입력하시오: "))

days = days_dictionery.get(month)

if days is not None:
    print(f"{month}의 일수는 {days}일 입니다.")

else:
    print("1에서 12사이의 달을 입력하세요.")
