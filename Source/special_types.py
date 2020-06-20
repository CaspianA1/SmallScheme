# special_types.py


class Procedure:
	def __init__(self, arguments, expression):
		self.arguments = arguments
		self.expression = expression

	def __str__(self):
		return f"{self.arguments} -> {self.expression}"


	def __call__(self, *proc_arguments, recursive_expr = None):

		if recursive_expr is None:
			recursive_expr = deepcopy(self.expression)

		"""
		print("Function has been called")
		print("Arguments:", proc_arguments)
		print("Recursive expression:", recursive_expr)
		"""

		if isinstance(recursive_expr, list):
			for index, item in enumerate(recursive_expr):
				recursive_expr[index] = self.__call__(*proc_arguments, recursive_expr = item)

			# print("Function is doooone! Recursive expr:", recursive_expr)
			return evaluate(recursive_expr)
		else:
			argument_map = dict(zip(self.arguments, proc_arguments))
			# print("Function argument can be examined")
			# print("Argument map:", argument_map)

			if recursive_expr in argument_map:
				return argument_map[recursive_expr]
			else:
				return recursive_expr


class SchemeList:
	def __init__(self, num_list):
		self.num_list = num_list

	def __getitem__(self, start = 0, stop = None, step = 1):
		if stop is None: stop = len(self.num_list)
		return self.num_list[start:stop:step]

	def __len__(self):
		return len(self.num_list)

	def __str__(self):
		string_repr = "("

		for item in self.num_list:
			string_repr += f"{item} "

		return string_repr.rstrip() + ")"

	# car = lambda self: self.num_list[0]
	# cdr = lambda self: self.num_list[1:]
	# cons = lambda self, item: self.num_list.insert(0, item)

class Symbol:
	def __init__(self, *contents):
		if len(contents) - contents.count("'") > 1:
			raise SyntaxError("A symbol cannot contain whitespace")
		self.raw_repr = "".join([str(item) for item in contents])

	def __str__(self):
		return self.raw_repr