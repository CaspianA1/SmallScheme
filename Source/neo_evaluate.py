# neo_evaluate.py

from Source.standard_library import ENVIRONMENT
from Source.special_types import *
from copy import deepcopy

symbol_table = {}

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
				break
			else:
				arguments[i] = Symbol(*arguments[i + 1:])
				del arguments[i + 1:]
				break

	if procedure_name == "define":
		symbol_table[arguments[0]] = evaluate(arguments[1])
		return

	elif procedure_name == "lambda":
		return Procedure(arguments[0], arguments[1])

	elif procedure_name == "check":
		for var, value in symbol_table.items():
			print(var, "::", value)	
		return

	procedure = find_var(procedure_name)

	return procedure(*[evaluate(arg) for arg in arguments])
