# NO TOUCHING==NO TOUCHING==NO TOUCHING==NO TOUCHING #| \
from random import randint                           #|  \
x = randint(-100, 100)                               #|   \
while x == 0:  # make sure x isn't zero              #|    \
    x = randint(-100, 100)                           #|     NO TOUCHING!!!!!! (please)         
y = randint(-100, 100)                               #|    /
while y == 0:  # make sure y isn't zero              #|   /
    y = randint(-100, 100)                           #|  /
# NO TOUCHING==NO TOUCHING==NO TOUCHING==NO TOUCHING #| /

if x > 0 and y > 0:
	print("both positive")
elif x < 0:
	print("x is negative")
else:
	print("y is negative")

if x  <  0 and y  <  0:
	print("both negative")
elif x > 0:
	print("x is positive")
else:
	print("y is positive")

print(x, y)

