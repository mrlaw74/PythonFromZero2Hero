# import math
from math import * # use * to import all functions from math module
import os, sys
lib_path = os.path.abspath(os.path.join('modules'))
sys.path.append(lib_path)
from mathplus import *
print(sum_2num(2,3))


a = 3.2
print(ceil(a))
print(floor(a))