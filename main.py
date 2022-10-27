#group

class group():
    def __init__(self, name, func):
        self.name = name
        self.func = func

    def _(self, a, b): #group operation
        return self.func(a, b)

    def _o(self, a, b):
        print(f"{a}∘{b} = {self._(a,b)}")

    def print_name(self):
        print(f"Name:{self.name}")


def addition_mod_n(a, b, n=5):
    return (a+b)%n

Int_mod_n = group("Integers mod 5", addition_mod_n)
Int_mod_n.print_name()


for i in range(5):
    Int_mod_n._o(0, 4*i)
