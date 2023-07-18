#imports 

#Errors
class FailsIdentity(Exception):
    "Raised when the group does not contain e"
    
    def __init__(self, message="Group does not contain e"):
        self.message = message
        super().__init__(self.message)

class FailsInverse(Exception):
    "Raised when the group does not contain inverse of an element"
    
    def __init__(self, message="x has no inverse"):
        self.message = message
        super().__init__(self.message)

class FailsAssociativity(Exception):
    "Raised when the group is not associative"
    
    def __init__(self, message="Group is not associative"):
        self.message = message
        super().__init__(self.message)

class FailsClosure(Exception):
    "Raised when the group is not closed under operation"

    def __init__(self, message="Group is not closed"):
        self.message = message
        super().__init__(self.message)

class NotAnElement(Exception):
    "Raised when element input is not in group"
    
    def __init__(self, message="Element operated on is not in the group"):
        self.message = message
        super().__init__(self.message)

class EndLesson(Exception):
    "Raised when the user does not hit c to continue"

    def __init__(self, message="Lesson aborted"):
        self.message = message
        super().__init__(self.message)

class IncorrectInputLength(Exception):
    "Raised when an element in the EDP product has the incorrect length"
    
    def __init__(self, message="Element in the EDP product has the incorrect length"):
        self.message = message
        super().__init__(self.message)