#This code was made so that if total is over 20000 he gets a discount
pencils = int(input("연필 개수 입력: "))
pens = int(input("펜 개수 입력: "))

total = (pencils * 2000) + (pens * 3000)
if total > 20000:
    print("10% 할인 되었습니다")
    gtotal = total * 0.9
    print(f"총합 : {int(gtotal)}원")

else:
    print(f"총합 : {int(total)}원")

print("----------------------")

#This code was made to find the biggest number
a = int(input("첫 번째 수를 입력하세요 : "))
b = int(input("두 번째 수를 입력하세요 : "))
c = int(input("세 번째 수를 입력하세요 : "))

if a == b == c:
    print("세 수가 모두 동일 합니다")
else:
    max_num = a
    if b > max_num:
        max_num = b
    if c > max_num:
        max_num = c
    print(f"가장 큰 수는: {max_num}")

print("----------------------")

#This code was made to determine if number is divisible or not
a = int(input("첫 번째 숫자를 입력하세요: "))
b = int(input("두 번째 숫자를 입력하세요: "))

if b == 0:
    print("0과 나눌수 없습니다!")
else:
    result = a / b
    print(f"나눗셈 결과는: {result} 입니다")

print("----------------------")

#This code was to made to determine whether the inputer is male or female 
a = int(input("주민번호 7번째 숫자를 입력하세요: "))
if a == 1 or a == 3 or a == 5:
    print("남자!")
else:
    if a == 2 or a == 4 or a == 6:
        print("여자!")
    else:
        print("1~6 사이의 숫자를 입력하세요")



