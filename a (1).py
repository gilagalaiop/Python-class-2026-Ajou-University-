user_id = input("아이디를 입력하세요: ")

if user_id == "ajou":
    pw = input("비밀 번호를 입력하세요 :")

    if pw == "1234":
        print("로그인 성공")
    else:
        print("비밀번호가 틀렸습니다")

else:
    print("등록되지 않은 아이디 입니다")
    
