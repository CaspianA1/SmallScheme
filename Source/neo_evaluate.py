# neo_evaluate.py

from Source.standard_library import ENVIRONMENT
from copy import deepcopy

class Procedure:
	def __init__(self, arguments, expression):
		self.arguments = arguments
		self.expression = expression

	def __str__(self):
		return f"{self.arguments} -> {self.expression}"
		# presentable = lambda seq: "".join([f"{a} " for a in seq if isinstance(a, list) else "|a|"]).rstrip()
		# return f"{presentable(self.arguments)} -> {presentable(self.expression)}"


	def __call__(self, *proc_arguments, recursive_expr = None):

		if recursive_expr is None:
			recursive_expr = deepcopy(self.expression)


		print("Function has been called")
		print("Arguments:", proc_arguments)
		print("Recursive expression:", recursive_expr)

		if isinstance(recursive_expr, list):
			for index, item in enumerate(recursive_expr):
				recursive_expr[index] = self.__call__(*proc_arguments, recursive_expr = item)

			print("Function is doooone! Recursive expr:", recursive_expr)
			return evaluate(recursive_expr)
		else:
			argument_map = dict(zip(self.arguments, proc_arguments))
			print("Function argument can be examined")
			print("Argument map:", argument_map)

			if recursive_expr in argument_map:
				return argument_map[recursive_expr]
			else:
				return recursive_expr


symbol_table = {}

def find_var(var_name):
	if var_name in ENVIRONMENT: return ENVIRONMENT[var_name]
	elif var_name in symbol_table: return symbol_table[var_name]
	else: return var_name  # is a literal value

def evaluate(parsed_code):
	global symbol_table
	if not isinstance(parsed_code, list):
		print("Will return code, which is:", parsed_code)
		return find_var(parsed_code)

	else:
		procedure_name = parsed_code[0]
		arguments = parsed_code[1:]

		print("Procedure name:", procedure_name)

	if procedure_name == "define":
		symbol_table[arguments[0]] = evaluate(arguments[1])
		return

	elif procedure_name == "check":
		print(symbol_table)
		return

	procedure = find_var(procedure_name)

	return procedure(*[evaluate(arg) for arg in arguments])