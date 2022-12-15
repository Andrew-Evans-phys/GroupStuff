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

def display(lesson) -> None:
    os.system('clear')
    lesson()
    flag = str(input("press c to continue, anything else to quit: "))
    if(flag[0].lower() != "c"):
        raise EndLesson
    os.system('clear')

def menu(lesson, lessons = 1) -> int:
    os.system('clear')
    lesson()
    print("\nq to quit, or a number to skip to that lesson.")
    flag = input("Any other input will continue: ")
    if(flag == "q"):
        raise EndLesson
    elif(int(flag) in range(1, lessons +1)): 
        os.system('clear')
        return int(flag)
    os.system('clear')
    return 0

def lesson0() -> None:
    print("This lesson will cover the introduction to groups!")

def lesson1() -> None:
    print("Lesson 1\n")
    print("A group is a set with a closed binary operation that satisfies the following rules:")
    print("1. There exists an element ε such that any element x from G obeys x = e*x = x*e")
    print("2. For all x in G there exists an element x_inv such that e = x*x_inv = x_inv*x")
    print("3. For all a, b, and c in G (a*b)*c = a*(b*c)\n")

def lesson2(n = 10, x = 2, y = 4, g = 2) -> None:
    #n is the number of elements in Z_n
    #x is the first input
    #y is the second input 
    #g is the generator of <g>
    set_Z_n = [i for i in range(n)]
    addition_mod_n = lambda a, b : (a + b)%n
    Z_n = Group(set_Z_n, addition_mod_n)
    print("Lesson 2\n")
    print(f"Z_{n} is the set {Z_n._set_to_set()} and the operation addition mod {n}\n")
    print(f"When we add {x} and {y} we find {Z_n._operation(x,y)}\n") #try playing with a and b!
    print(f"We can create a cyclic subgroup by adding {g} to itself over and over again.\n(This will be proved later as well as a proper definition of subgroup) \n")
    gen_g = Cyclic_subgroup(set_Z_n, addition_mod_n, g)
    print(f"We find the set generated to be <{g}> = {gen_g._set_to_set()}\n")

def lesson3(n = 20, x = 13, y = 3) -> None:
    #n is the the value that the U(n) group is being created with 
    #x is the first input 
    #y is the second input
    multiplication_mod_n = lambda a, b : (a * b)%n
    set_U_n = [i for i in range(n) if(gcd(i,n) == 1)]
    U_n = Group(set_U_n, multiplication_mod_n)
    print("Lesson 3\n")
    print(f"We are not just limited to addition, consider U({n})\n")
    print(f"U({n})'s set is {U_n._set}\n(positive integers (i) less than {n} with gcd(i,{n})=1)\n")
    print(f"When we multiply {x} and {y} we find {U_n._operation(x,y)}\n")

goto = menu(lesson0, 3)
if(goto <= 1):
    display(lesson1)
if(goto <= 2):
    display(lesson2)
if(goto <= 3):
    display(lesson3)