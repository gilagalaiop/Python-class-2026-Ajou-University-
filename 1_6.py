#This code was made to learn f-string and escape string \t
name = "Peter Parker"
kor, eng, math = 19, 50, 46

total = kor + eng + math
avg = (kor + eng + math) / 3

print(f"{'이름':<7s}\t{'국어':>3}\t{'영어':>3}\t{'수학':>3}\t")
print(f"{name:<7}\t{kor:>3}\t{eng:>3}\t{math:>3}\t")
print(f"총점:{total:>4}\t평균:{avg:>10.3f}")

print("-------------------")

#This code was made to calculate cost of travel using input function 
print ("여행 경비 계산")
flight = int(input("항공권 가격 :"))
hotel_per_day = int(input("숙박(1박) 요금 :"))
food_per_day = int(input("식비(1일) 비용 :"))
no_of_days = int(input("여행 일수 :"))

total_food = 5 * food_per_day
total_accommodation = 5 * hotel_per_day
total = flight + total_food + total_accommodation

print(f"\n총 여행 경비 : {total:,}원")
print(f"숙박비 비율 {(total_accommodation / total) * 100:.2f}%")
