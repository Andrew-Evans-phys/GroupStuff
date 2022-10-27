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

class permutation():
    def __init__(self, cycle):
        self.cycle = cycle

    def permute(self, a):
        a_loc = self.cycle.index(a)
        return self.cycle[(a_loc+1)%(len(self.cycle))]

    def permute_o(self, a):
        a_loc = self.cycle.index(a)
        print(f"A({a}) = {self.cycle[(a_loc+1)%(len(self.cycle))]}")

def addition_mod_n(a, b, n=5):
    return (a+b)%n  

def comp_of_permuations(a,b):
    result = []
    elements = list(set(a.cycle) | set(b.cycle))
    for i in elements:
        new_cycle = []
        try:
            temp = b.permute(i)
            try:
                temp = a.permute(temp)
                if(temp != i):
                    new_cycle.append(temp)
                else:
                    pass
            except ValueError:
                new_cycle.append(b.permute(i))
        except ValueError:
            try:
                new_cycle.append(a.permute(i))
            except ValueError:
                pass
        result.append(new_cycle)

    return result



a = permutation([1,2,3])
b = permutation([1,2,3])
s3 = group("S3", comp_of_permuations)

s3._o(a,b)
    
