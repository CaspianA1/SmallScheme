# special_types.py

class SchemeList:
	def __init__(self, num_list):
		self.num_list = num_list
		self.representation = "(" + " ".join([str(a) for a in self.num_list]) + ")"

	__len__ = lambda self: len(self.num_list)

	__str__ = lambda self: self.representation

class Symbol:
	def __init__(self, *contents):
		if len(contents) - contents.count("'") > 1:
			raise SyntaxError("A symbol cannot contain whitespace")
		self.raw_repr = "".join([str(item) for item in contents])

	__str__ = lambda self: self.raw_repr