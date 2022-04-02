import os
import sys
from random import randint



def restart():
    os.execl(sys.executable, sys.executable, *sys.argv)

# Add up all odd numbers between 10 and 20
# Store the result in x:
for x in range(1,21):
    if (x == 4) != (x == 13):
        statis = "unlucky"
    elif x % 2 == 1:
        statis = "odd"
    else:
        statis = "even"
     print(f"{x} is {statis}")



#restart()






