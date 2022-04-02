import os
import sys
from random import randint



def restart():
    os.execl(sys.executable, sys.executable, *sys.argv)

smiles = "\U0001f600"

lines = 9

for x in range(lines + 1):
    markers = lines - x
    print("")
    while markers < lines:
        print(smiles, end = " " )
        markers += 1
# while lines < 10:
#     print("")




#restart()






