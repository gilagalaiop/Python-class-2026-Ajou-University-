#this code was made to calculate volume and compare with constant c and print 1 if bigger, 0 if same and -1 if smaller
a = 5
b = 4
h = 3
c = 65
vol = a * b * h
result = (vol > c) - (vol < c)
print("result 1 =", result)

c = 50
vol = a * b * h
result = (vol > c) - (vol < c)
print("result 2 =", result)

c = 60
vol = a * b * h
result = (vol > c) - (vol < c)
print("result 3 =", result)

print("--------------------------")

#this code was made to print True and False
#1. if same number
a = 6
b = 6
result1 = (a ^ b) == 0
print("result1 =", result1)
#2. if different number
a = 6
b = 5
result2 = (a ^ b) == 0
print("result2 =", result2)
