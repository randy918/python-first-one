import os
import sys
import random


def restart():
    os.execl(sys.executable, sys.executable, *sys.argv)


demo_list = ["trial", "final", "hub"]
print("\n")
print(demo_list)
print(len(demo_list))

# restart()


people = ["Hanna", "Louisa", "Claudia", "Angela", "Geoffrey", "aparna"]

for x in range(len(people)):
    if people[x] == "Hanna":
        people[x] = people[x] + "h"
    if people[x] == "Geoffrey":
        people[x] = "Jeffrey"
    if people[x] == "aparna":
        people[x] = "Arpana"

    print(people[x])

    numerics = ["one", "two", "three", "four"]

for x in numerics:
    print(x)

i = 0
while i < len(numerics):
    print(numerics[i])
    i += 1
total_sounds = ""
sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]

sounds.extend(["junty", "kop"])

for x in sounds:
    total_sounds += x

print(total_sounds.upper())

instructors = []

instructors.extend(["Colt","Blue", "Lisa"])


print(instructors.sort())

#instructors.clear()

print(len(instructors))
print(instructors)

sounds.pop()
print(sounds)

instructors.remove("Colt")
print(instructors)
instructors.reverse()
print(instructors)

print("-".join(["bu", "tane"]))
