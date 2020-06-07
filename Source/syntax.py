''' these are the types of tokens used '''

"""
class Token:
    def __init__(self):
        pass

class Symbol(Token):
      def __init__(self):
          super.__init__(self)

class Number(Token):
    def __init__(self):
        super.__init__(self)

    def __str__(self):
        pass

class Conditional(Token):
    def __init__(self):
        super.__init__(self)

class Definition(Token):
    def __init__(self):
       super.__init__(self) 

class Procedure(Token):
    def __init__(self):
       super.__init__(self) 

    def __call__(self):
        pass
"""

''' these are the scheme types used '''

Symbol = str
Number = int, float
Atom = Symbol, Number
List = list
Expression = Atom, List
Environment = dict

TYPES = (Symbol, Number, Atom, List, Expression, Environment)
