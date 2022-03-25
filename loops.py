import os
import sys
from random import randint



def restart():
    os.execl(sys.executable, sys.executable, *sys.argv)

for x in range(9, 99):
    print(x)
#restart()


