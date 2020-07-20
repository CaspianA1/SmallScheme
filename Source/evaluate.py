# neo_evaluate.py

from inspect import signature
from Source.standard_library import ENVIRONMENT
from Source.special_types import *
from copy import deepcopy

symbol_table = {}

class Procedure:
	def __init__(self, arguments, expression):
		self.arguments = arguments
		self.expression = expression

		self.representation =f"{self.arguments} -> {self.expression}"
		for key, value in {"[": "(", "]": ")", "'": "", ",": ""}.items():
			self.representation = self.representation.replace(key, value)

	__str__ = lambda self: self.representation

	def __call__(self, *in_args, recursive_expr = None):  # make a recursion-ended flag
		if type(recursive_expr) in (str, int, float, SchemeList, Symbol):  # end of recursion
			return recursive_expr

		arg_map = dict(zip(self.arguments, in_args))

		if recursive_expr is None:
			recursive_expr = deepcopy(self.expression)

		for index, item in enumerate(recursive_expr):
			if isinstance(item, list):  # s-expression
				value = self.__call__(*in_args, recursive_expr = item)
				recursive_expr[index] = value  # will be evaluated by evaluate later
				continue

			value = find_var(item)

			if item in arg_map:  # argument
				recursive_expr[index] = arg_map[item]

			if value == ENVIRONMENT["if"]:
				cond, stmt_1, stmt_2 = recursive_expr[index + 1: index + 4]
				cond_is_true = self.__call__(*in_args, recursive_expr = cond)
				stmt_to_eval = stmt_1 if cond_is_true else stmt_2
				result = self.__call__(*in_args, recursive_expr = stmt_to_eval)
				return result  # maybe put this here?

		return evaluate(recursive_expr)

def find_var(var_name):
	if var_name in ENVIRONMENT: return ENVIRONMENT[var_name]
	elif var_name in symbol_table: return symbol_table[var_name]
	else: return var_name  # is a literal value

# make the repl in curses

def evaluate(parsed_code):
	global symbol_table
	if not isinstance(parsed_code, list):
		return find_var(parsed_code)

	else:
		procedure_name = parsed_code[0]
		arguments = parsed_code[1:]

	for i, argument in enumerate(arguments):
		if argument == "'":
			if isinstance(arguments[i + 1], list):
				arguments[i] = SchemeList(arguments[i + 1])
				del arguments[i + 1:]
			else:
				arguments[i] = Symbol(arguments[i + 1])
				del arguments[i + 1]

	if procedure_name == "define":
		symbol_table[arguments[0]] = evaluate(arguments[1])
		return  # make "define" return something

	elif procedure_name in ("lambda", "λ"):
		return Procedure(arguments[0], arguments[1])

	elif procedure_name == "cond":  # does not work with 'else' clause
		print("Arguments:", arguments)
		for index, cond_set in enumerate(arguments):
			if index == len(arguments) - 1 and (list, list) != tuple(map(lambda v: type(v), cond_set)):
				return evaluate(cond_set)
			condition, val = cond_set
			if evaluate(condition):
				return evaluate(val)

	elif procedure_name == "symbols":
		for var, value in symbol_table.items():
			print(var, "::", value)
		return

	procedure = find_var(procedure_name)

	if isinstance(procedure, str):
		raise TypeError(f"{procedure} is not a procedure")

	return procedure(*[evaluate(arg) for arg in arguments])