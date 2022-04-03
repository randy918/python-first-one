import os
import sys
import random


def restart():
    os.execl(sys.executable, sys.executable, *sys.argv)


restart()
