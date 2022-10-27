#group

from itertools import permutations


class permutation():
    def __init__(self, name, cycle):
        self.name = name
        self.cycle = cycle

    def permute(self, a):
        a_loc = self.cycle.index(a)
        return self.cycle[a_loc+1]

    def permute_o(self, a):
        a_loc = self.cycle.index(a)
        print(f"A({a}) = {self.cycle[(a_loc+1)%len(self.cycle)]}")

    


test = permutation("test", [1,2,3])
test.permutation(3)
    
