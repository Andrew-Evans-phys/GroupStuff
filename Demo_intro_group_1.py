#imports
import Theorems as thm
from Definitions import *
from Errors import *
import os

def gcd(a, b):
    if(b == 0):
        return abs(a)
    else:
        return gcd(b, a % b)

def addition_mod6(a,b): #Need tot generalize this so that changing n changes modulo
    return (a+b)%6

def multiplication_mod_20(a,b): #Need tot generalize this so that changing n changes modulo
    return (a*b)%20

set_Z_6 = [0,1,2,3,4,5]
Z_6 = Group(set_Z_6, addition_mod6)

os.system('clear')
print("A group is a set with a closed binary operation that satisfies the following rules:")
print("1. There exists an element ε such that any element x from G obeys x = e*x = x*e")
print("2. For all x in G there exists an element x_inv such that e = x*x_inv = x_inv*x")
print("3. For all a, b, and c in G (a*b)*c = a*(b*c)\n")


print(f"Z_6 is the set {Z_6._set_to_set()} and the operation addition mod 6\n")
a = 2 
b = 4
print(f"When we add {a} and {b} we find {Z_6._operation(a,b)}\n") #try playing with a and b!

n = 2
print(f"We can create a cyclic subgroup by adding {n} to itself over and over again.\n(This will be proved later as well as a proper definition of subgroup) \n")
gen_n = Cyclic_subgroup(set_Z_6, addition_mod6, n)
print(f"We find the set generated to be <{n}> = {gen_n._set_to_set()}\n")

flag = str(input("press c to continue, anything else to quit: "))

if(flag[0].lower() != "c"):
    raise EndLesson

os.system('clear')
n = 20
set_U_n = [i for i in range(n) if(gcd(i,n) == 1)]
U_n = Group(set_U_n, multiplication_mod_20)
print(f"We are not just limited to addition, consider U({n})\n")
print(f"U({n})'s set is {U_n._set}\n")
a = 19
b = 17

print(f"When we multiply {a} and {b} we find {U_n._operation(a,b)}\n")