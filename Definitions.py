#imports
import sys
from Errors import *
import itertools

#Group definition
class Group:
    def __init__(self, _set, _operation_var) -> None:
        identity_test = lambda x, f: x == f(x,x) #x = x^2 => x = e
        is_identity = [identity_test(element, _operation_var) for element in _set] #list of booleans checking for if the identity has been found
        identity_found = any(is_identity) #boolean that is true if there exists an identity
        if(identity_found): 
            identity = _set[is_identity.index(True)]
        else:
            raise FailsIdentity

        inverses = [] #stored as a list of set of pairs of x and x_inv
        inverses_dict = {}
        for x in _set:
            x_inv_found = False
            for x_inv in _set:
                inv_pair = {x, x_inv}
                if(identity == _operation_var(x_inv, x) and identity == _operation_var(x, x_inv)):
                    inverses_contained = inverses.count(inv_pair) != 0
                    inverses_dict.update({x:x_inv})
                    if(inverses_contained):
                        x_inv_found = True
                    else:
                        inverses.append(inv_pair)
                        x_inv_found = True
            if(not x_inv_found):
                raise FailsInverse

        set_form = set(_set)
        cayley_table = []
        for a in _set:
            row = []
            for b in _set:
                ab = _operation_var(a,b)
                row.append(ab)
                if(ab not in set_form):
                    raise FailsClosure
                #defining boolean lambda function for associativity test
                assoc = lambda a, b, ab, c, f: f(ab,c) == f(a,f(b,c))
                is_associative = [assoc(a,b,ab,c, _operation_var) for c in _set]
                if not all(is_associative):
                    FailsAssociativity
            cayley_table.append(row)

        #Assuming all the above conditions were met you now have a brand new group!
        self._set = _set
        self._operation_var = _operation_var
        self.inverses_dict = inverses_dict        
        self.order = len(_set)
        self.identity = identity
        self.cayley_data = cayley_table

    def _operation(self, a, b): #type should be looked into, varible function return?
        """Method of the class Group that takes in two inputs and performs the group operation (in order of inputs).
        Checks to make sure data type of inputs are the same as elements in Group before execution.


        Args:
            a (Group Element): Arbitrary element of Group.
            b (Group Element): Arbitrary element of Group.

        Raises:
            NotAnElement: Raised when a or b is not an element of the Group.  
            
        Returns:
            Group Element: Value of (a * b).
        """
        set_form = self._set_to_set()
        if(a not in set_form or b not in set_form):
            raise NotAnElement
        return self._operation_var(a, b)

    def _set_to_set(self):
        """Method of the class Group that takes a list of Group elements and converts into a set of Group elements.

        Returns:
            set: A set containing the elements of the group.
        """
        return set(self._set)

    def inverse(self, a):
        """Method of the class Group that validates a single input as an element of the group before finding
        its corresponding inverse.

        Args:
            a (Group Elememt): Arbitrary element of the Group.

        Raises:
            NotAnElement: Raised when a is not an element of the Group.

        Returns:
            Group Element: Inverse element of a, a^(-1), defined by: a * a^(-1) = a^(-1) * a = e
        """
        if(a not in self._set_to_set()):
            raise NotAnElement
        return self.inverses_dict.get(a)

    def e_order(self, a) -> int:
        """Method of the class "Group" that returns the order of an element.

        Args:
            a (Group Element): Element of the group the method is acting on.

        Returns:
            int: Order of the element.
        """
        #need to implement type protection
        n, a_n = 1, a
        while(a_n != self.identity):
            n += 1
            a_n = self.power(a, n)
        return n

    def power(self, a, pow):
        """Method of the class "Group" that results in multiplying a by itself n times, a * a * ... * a = a^n.
        Args:
            a (Group Element): Element of the group that method is acting on.
            pow (int): Exponent. Number of times a will be multiplyed by itself.

        Returns:
            Group Element: Group element mapped to after taking a^n.
        """
        if(pow == 0):
            return self.identity
        elif(pow == 1):
            return a
        else:
            return self._operation(a, self.power(a, pow-1))

    def powers_of_(self, a):
        return [self.power(a, i) for i in range(self.e_order(a))]

    def display_cayley_table(self) -> None:
        output = "|x |"
        for i in self._set:
            output += f"{i}|"
        output += "\n"
        for i in range(len(self.cayley_data)):
            output += f"|{self._set[i]}|"
            for ab in self.cayley_data[i]:
                output += f"{ab}|"
            output += "\n"
        print(output)

    def latex_cayley_table(self) -> None:
        centers = ""
        for i in range(self.order):
            centers += " c"
        output = "\\begin{center}\n\\noindent\\begin{tabular}{c | "+ centers +"}\n \t"
        for i in self._set:
            output += f" & {i}"
        output += "\\\\ \n\t\\cline{1-"+str(self.order+1)+"}\n"
        for i in range(len(self.cayley_data)):
            output += f"\t{self._set[i]}"
            for ab in self.cayley_data[i]:
                output += f" & {ab}"
            output += "\\\\ \n"
        output += "\end{tabular}\n\\end{center}"
        print(output)

def EDP(group_list) -> Group:
    set_op_list = [(group._set, group._operation_var) for group in group_list]
    _sets_list, _operation_list = zip(*set_op_list)
    elements = list(itertools.product(*_sets_list)) #all combinations of elements in tuple form

    def operation(a,b):
        a = list(a)
        b = list(b)
        if(len(a) == len(_sets_list) and len(b) == len(_sets_list)):
            return tuple([_operation_list[i](a[i],b[i]) for i in range(len(_sets_list))])
        else:
            raise IncorrectInputLength

    return Group(elements, operation)

def init_cylic(group, a) -> Group:
    new_set = group.powers_of_(a)
    return Group(new_set, group._operation_var)

def create_element(perm, n) -> tuple: #for the init of S_n
    element = [perm[i] for i in range(n)]
    return tuple(element)

def compose(a, b) -> tuple: #comp restricted to S_n
    a = list(a)
    b = list(b)
    product = [a[i-1] for i in b]
    return tuple(product) 

def init_D_(n) -> Group:
    r = [f"R{i}" for i in range(n)]
    f = [f"F{i+1}" for i in range(n)]
    elements = r+f

    def D_n_compose(a, b) -> str:
        R0 = [i for i in range(1,n+1)]
        rotations = [tuple(R0)]
        for k in range(n-1):
            new_R = []
            for j in R0:
                new_R.append(((j+k)%n)+1)
            rotations.append(tuple(new_R))

        #converting to dict 
        rotations_dict = {f"R{i}" : rotations[i] for i in range(n)}

        #making flips
        F1 = tuple(reversed(R0))
        flips = [compose(i, F1) for i in rotations]

        #converting to dict
        flips_dict = {f"F{i+1}" : flips[i] for i in range(n)}

        #merging flips and rotations into one dict
        elements = rotations_dict
        elements.update(flips_dict)

        a = list(elements[a])
        b = list(elements[b])
        product = [a[i-1] for i in b]
        inv_D_n_map = {v : k for k, v in elements.items()}
        return inv_D_n_map[tuple(product)]

    return Group(elements, D_n_compose)

def init_Z_(n) -> Group:
    set_Z_n = [i for i in range(n)]
    addition_mod_n = lambda a, b : (a + b)%n
    return Group(set_Z_n, addition_mod_n)

def init_U_(n) -> Group:
    multiplication_mod_n = lambda a, b : (a * b)%n
    set_U_n = [i for i in range(n) if(gcd(i,n) == 1)]
    return Group(set_U_n, multiplication_mod_n)

def init_S_(n) -> Group:
    perm_list = list(itertools.permutations(range(1, n+1)))
    elements = [create_element(perm, n) for perm in perm_list]
    return Group(elements, compose)

def gcd(a, b):
    if(b == 0):
        return abs(a)
    else:
        return gcd(b, a % b)