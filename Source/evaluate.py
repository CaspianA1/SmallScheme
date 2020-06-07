# evaluate.py

from copy import deepcopy
from Source import syntax, parse
import os

def sub(*nums):
	result = nums[0]
	for i in range(1, len(nums)):
		result -= nums[i]
	return result

def mult(*nums):
	result = 1
	for num in nums:
		result *= num
	return result

def div(*nums):
	result = nums[0]
	for i in range(1, len(nums)):
		result /= nums[i]
	return result

def define(symbol_name, var_value):
	global symbol_table
	symbol_table[symbol_name] = var_value

def write_file(file_name, data):
	with open(file_name, "w") as file:
		file.write(data)
		return 0
	return -1

def append_file(file_name, data):
	with open(file_name, "a") as file:
		file.write(data)
		return 0
	return -1

def read_file(file_name, data):
	with open(file_name, "r") as file:
		return file.read()
	return -1

def display(data):
	data = str(data)
	if data.startswith("'"):
		print(data[1:])
	else:
		print(data)

def list_funcs(str_lst, arg_type, add_onto = None):
	new_lst = []

	for index, character in enumerate(str_lst):
		if character == "\"":
			next_apostrophe = str_lst[index:].find("\"")
			between_result = str_lst[index:next_apostrophe]
			new_lst.append(between_result)
			go_ahead_amt = next_apostrophe - index
			index += go_ahead_amt
			continue
		elif character in " ,":
			continue
		else:
			new_lst.append(parse.atom(character))

	if arg_type == "car":
		return new_lst[0]
	elif arg_type == "cdr":
		return new_lst[1:]
	elif arg_type == "cons":
		base = [add_onto]
		base.append(new_lst)
		return base

symbol_table = {}

ENVIRONMENT = {
	"+": lambda *nums: sum(nums),
	"-": sub,
	"*": mult,
	"/": div,
	"<": lambda arg_one, arg_two: True if arg_one < arg_two else False,
	">": lambda arg_one, arg_two: True if arg_one > arg_two else False,
	"define": define,
	"display": display,
	"if": lambda condition, stmt_1, stmt_2: stmt_1 if condition else stmt_2,
	"eq?": lambda thing_1, thing_2: thing_1 is thing_2,
	"eqv?": lambda thing_1, thing_2: thing_2 == thing_2,
	"equal?": lambda thing_1, thing_2: thing_2 == thing_2,
	"abs": abs,
	"write-file!": write_file,
	"append-file!": append_file,
	"read-file!": read_file,
	"shell!": lambda command: os.popen(command).read(),
	# "car": lambda str_lst: list_funcs(str_lst, "car"),
	# "cdr": lambda str_lst: list_funcs(str_lst, "cdr"),
	# "cons": lambda str_lst: list_funcs(str_lst, "cons"),

	"check": lambda: print(symbol_table)
	

	# add map, reduce, filter
	# but need symbols first
	# also, recursion does not work
	# add car, cdr and cons now

}

# (define factorial (lambda (x) (if (< x 2) 1 (* x (factorial (- x 1))))))

def find_var_value(var, type_check = False, parameters = None, arguments = None):
	if type_check is True:
		if type(var) not in (str, int, float, list, dict):
			raise ValueError(f"Undefined variable {var}")
	if var in ENVIRONMENT:
		return ENVIRONMENT[var]
	elif var in symbol_table:
		return symbol_table[var]
	elif parameters is not None and var in parameters:
		return arguments[parameters.index(var)]
	else:
		return var

class Lambda:
	def __init__(self, body):
		self.parameters = body[0]
		self.expression = body[1]
		if len(body) > 2:
			raise AttributeError(f"Incorrect number of arguments to lambda expression {body}")

	def __call__(self, *arguments, expr = None):
		if expr is None: expr = deepcopy(self.expression)

		if isinstance(expr, list):
			for index, item in enumerate(expr):
				expr[index] = self.__call__(*arguments, expr = item)
			    return evaluate(expr)  # unindented before

		    return find_var_value(expr, True, self.parameters, arguments)  # unindented before

	def __str__(self):
		return f"{self.parameters} {self.expression}"

def is_a_lambda(lambda_func):
  LAMBDA = lambda:0
  return isinstance(lambda_func, type(LAMBDA)) and lambda_func.__name__ == LAMBDA.__name__

def evaluate(parsed_code):
	if not isinstance(parsed_code, list): return parsed_code

	procedure_name, arguments = parsed_code[0], parsed_code[1:]

	if procedure_name == "lambda": return Lambda(arguments)

	if not is_a_lambda(procedure_name) and not callable(procedure_name):

		procedure = find_var_value(procedure_name)

		if procedure == procedure_name:

			print("Error", type(procedure), procedure, type(arguments), arguments)
			if isinstance(arguments, list):  # checking for (car (cdr (lst))), for example
				print("Arguments:", arguments)  # FIX THE BUG - MAYBE MAKE ALL LISTS TAKEN CARE OF HERE STRINGS
			else:
				raise UnboundLocalError(f"Undefined procedure \"{procedure_name}\"")

	else: procedure = procedure_name

	for index, argument in enumerate(arguments):
		if isinstance(argument, str) and argument.startswith("'") and argument != "'":
			# guaranteed to be a non-list
			arguments[index] = syntax.Symbol(argument)
		elif argument == "'":
			if type(arguments[index + 1]) == list:
			# factors indicate that the argument is a list
				list_contents = str(arguments[index + 1]).strip("[").strip("]")
				return procedure(arguments[index - 1], list_contents)  # bug location

		try:
			if (var_value := symbol_table.get(argument)) is not None:
				arguments[index] = var_value
		except TypeError:
			arguments[index] = evaluate(argument)

	return procedure(*[evaluate(arg) for arg in arguments])
