a = 10
b = 25
c = 15

if a >= b and a >= c:
    greatest = a
elif b >= a and b >= c:
    greatest = b
else:
    greatest = c

print("Number 1:", a)
print("Number 2:", b)
print("Number 3:", c)
print("Greatest Number:", greatest)