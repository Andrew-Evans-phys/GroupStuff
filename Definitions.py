#imports


#Group definition

class Group:

    def __init__(self, _set, _operation) -> None:
        identity = None
        identity_found = False
        for e_test in _set: #what happens if this ends and finds no identity? -> Error
            if(e_test == _operation(e_test, e_test)): #identity test x = x^2 => x = e
                identity_found = True
                identity = e_test
                break

        if(identity_found == False):
            raise FailsIdentity

        inverses = [] #stored as a list of set of pairs of x and x_inv
        for x in _set:
            x_inv_found = False
            for x_inv in _set:
                inv_pair = {x, x_inv}
                if(identity == _operation(x_inv, x) and identity == _operation(x, x_inv)):
                    inverses_contained = bool(inverses.count(inv_pair))
                    if(inverses_contained):
                        x_inv_found = True
                        pass
                    else:
                        inverses.append(inv_pair)
                        x_inv_found = True

            if(x_inv_found == False):
                raise FailsInverse

        set_form = set(_set)
        for a in _set:
            for b in _set:
                ab = _operation(a,b)
                if(ab not in set_form):
                    raise FailsClosure
                for c in _set:
                    if(not(_operation(ab,c) == _operation(a,_operation(b,c)))):
                        raise FailsAssociativity


        #Assuming all the above conditions were met you now have a brand new group!
        self._set = _set
        self._operation = _operation

    def _operation(self, a, b): #type should be looked into, varible function return?
        ab = self._operation(self._set, a, b)
        set_form = set(self._set)
        if(ab not in set_form):
            raise NotAnElement
        return self._operation(self._set, a, b)

#Errors
class FailsIdentity(Exception):
    "Raised when the group does not contain ε"
    pass

class FailsInverse(Exception):
    "Raised when the group does not contain inverse of an element"
    pass

class FailsAssociativity(Exception):
    "Raised when the group is not associative"
    pass

class FailsClosure(Exception):
    "Raised when the group is not closed under operation"
    pass

class NotAnElement(Exception):
    "Raised when element input is not in group"
    pass