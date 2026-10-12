#This code was made to show formats of python via printing student detail
name = "Lee"
department = "Electrical Enginnering"
student_id = "202621584"
age = "19"
school = "Ajou Univ"
print ("=====사용자 정보 출력=====\n\n[사용자 정보]\n\t이름: " + name + "\n\t학과: " + department + "\n\t학번: " + student_id + "\n\t나이: " + age + "세\n\t학교: " + school + "\n\n ==============")

print("------------------------------------")

#This code was made to show and learn how alightments work in python     
name = "Lionel Messi"
kor, eng, math = 100, 100, 10
print(format('이름', '<8s'), format('국어', '>3s'),
      format('영어', '>3s'), format('수학', '>3s'))
print(format(name, '<8s'), format(kor, '>3d'),
      format(eng, '>3d'), format(math, '>3d'))

print("------------------------------------")

#This code whas the same purpose as previous code but it has average added
name = "Ronaldo"
kor, eng, math = 0, 50, 100
avg = (kor + eng + math) / 3

print("%-10s %6s %6s %6s" % ("이름", "국어", "영어", "수학"))
print("%-10s %6d %6d %6d" % (name, kor, eng, math))
print("평균: %8.2f" % avg)

print("------------------------------------")

name = "Son"
kor, eng, math = 99, 80, 89
total = kor + eng + math
avg = total / 3

print("{:>8} {:>5} {:>6}".format("이름", "총점", "평균"))
print("{:>8s} {:>5d} {:>6.1f}".format(name, total, avg))

