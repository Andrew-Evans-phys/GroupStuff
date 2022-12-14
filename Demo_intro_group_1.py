#imports
import Theorems as tf
from Definitions import *


def operation(a,b):
    return (a+b)%5

set_Z_5 = [0,1,2,3,4]
Z_5 = Group(set_Z_5, operation)

print(Z_5._operation(0,1))
print(Z_5._operation(2,3))
