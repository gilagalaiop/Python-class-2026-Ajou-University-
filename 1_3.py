#this code was made to show math formats in python
c = 4
h = 250 * c ** (3.2) - 180/c + 12
print(h)

print("-------------------------")

#this code made to find the nosiest apartment. (formula: y = 0.2467 * distance from the road(m) + 4.159
Apt_A = 15
y = 0.2467 + Apt_A + 4.159
print(y)
Apt_B = 32
y = 0.2467 + Apt_B + 4.159
print(y)
Apt_C = 69
y = 0.2467 * Apt_C + 4.159
print(y)

print("-------------------------")

#This code was made to calculate the amount snacks in diffenret package
snacks = 587
boxes = snacks // 100
remain = snacks % 100
bags = remain // 10
pieces = remain % 10
print(boxes)
print(bags)
print(pieces)

print("-------------------------")

#This code was made to fimd the given seconds in hours minutes and time
Sec = 22222
Hours = (Sec % 3600) // 60
Mins = (Sec % 3600) // 60
Secs = Sec % 60
print("Hrs:", Hours)
print("Mins:", Mins)
print("Secs:", Secs)

print("-------------------------")

#This code was made to check how different functions work
a = 50; a -= 7
print(a)
a = 6; a **= 2
print(a)
a = 29; a //= 5
print(a)
a = 37; a &= 7
print(a)
a = 12; a &= 7
print(a)
a = 25; a ^= 15
print(a)
