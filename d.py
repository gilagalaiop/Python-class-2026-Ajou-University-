month = int(input("달을 입력하시오: "))

match month:
    
    case 4|6|9|11:
        print(f"{month}월의 일수는 30일 입니다")

    case 2:
        print(f"{month}월의 일수는 28일 입니다")

    case 1|3|5|7|10|12:
        print(f"{month}월의 일수는 31일 입니다")

    case _:
        print("1에서 11 사이의 달을 입력하세요")
        
