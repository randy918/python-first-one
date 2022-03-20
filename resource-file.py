import os
import sys

def restart():
	os.execl(sys.executable, sys.executable, *sys.argv)

age = input("How old are you: ")

if age.isdigit():
	age = int(age)
	if age >= 18 and age < 21:
		print("wristband")
		restart()
	elif age >= 21 and age <=100:
		print("drink, no wristband")
		restart()
	else: print("Go Away")
	restart()
else:
	#restart
	print("Try Again")
	restart()