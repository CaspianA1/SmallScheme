# standard_library.py

import os
from functools import reduce
from Source.special_types import *
from Source.parse import atom

def write_op(file_name, data, mode):
	with open(file_name, mode) as file:
		file.write(data)
		return True
	return False

def read_file(file_name):
	with open(file_name, "r") as file:
		return file.read()

def car(lst_obj):
	if not isinstance(lst_obj, SchemeList):
		raise ValueError(f"'{lst_obj}' is not a list.")
	first_elem = lst_obj.num_list[0]
	if isinstance(first_elem, SchemeList):
		return SchemeList(first_elem)
	else:
		return atom(first_elem)

def cdr(lst_obj):
	if not isinstance(lst_obj, SchemeList):
		raise ValueError(f"'{lst_obj}' is not a list.")
	return SchemeList(lst_obj.num_list[1:])

def cons(var, lst_obj):
	if not isinstance(lst_obj, SchemeList):
		raise ValueError(f"'{lst_obj}' is not a list.")
	lst_obj.num_list.insert(0, var)
	return lst_obj

# test this

"""
def cond(*condition_set, eval_func):
	print("Condition set:", condition_set)
	else_conditition = condition_set[-1].pop()
	print("Else condition:", else_conditition)
	for condition_body in condition_set[0]:
		condition, stmt = condition_body
		print("Condition and statement:", condition, stmt)
		if eval_func(condition):  # evaluate condition
			print("Condition is true:", condition)
			print("Returning stmt", stmt)
			return stmt
	print("Returning else condition", else_condition)
	return else_condition
"""

# test this
def quote(anything):  # quoting symbols
    if isinstance(anything, list):
        return SchemeList(anything)
    else:
        return Symbol(anything)
# (not related to this function) just make it so that only the first argument of the symbol is evaluated

def eq_proc(num_1, num_2):
	for unsupported in (str, bool):
		if unsupported in map(lambda n: type(n), (num_1, num_2)):
			raise ValueError("= can only be used for numbers")
		return num_1 == num_2

"""
def eqv(t1, t2):
	print("t1:", t1, "and t2:", t2)
	return t1 == t2
"""

ENVIRONMENT = {
	"+": lambda *nums: sum(nums),
	"-": lambda *nums: reduce(lambda x, y: x - y, nums),
	"*": lambda *nums: reduce(lambda x, y: x * y, nums),
	"/": lambda *nums: reduce(lambda x, y: x / y, nums),
	"<": lambda arg_one, arg_two: True if arg_one < arg_two else False,
	">": lambda arg_one, arg_two: True if arg_one > arg_two else False,
	"display": lambda data: print(data),
	"if": lambda condition, stmt_1, stmt_2: stmt_1 if condition else stmt_2,
	# "cond": cond,  # fix this after if
	"eq?": lambda thing_1, thing_2: thing_1 is thing_2,
	"eqv?": lambda t1, t2: t1 == t2,
	"equal?": lambda t1, t2: t1 == t2,
	"abs": abs,
	"write-file": lambda file_name, data: write_op(file_name, data, "w"),
	"append-file": lambda file_name, data: write_op(file_name, data, "a"),
	"read-file": read_file,
	"shell!": lambda command: os.popen(command).read(),  # support strings as commands
	"car": car,
	"cdr": cdr,
	"cons": cons,
	"read": input,
	"list-ref": lambda list_obj, index: list_obj.num_list[index],
	"map": lambda procedure, list_obj: SchemeList(map(procedure, list_obj.num_list)),
	"filter": lambda procedure, list_obj: SchemeList(filter(procedure, list_obj.num_list)),
	# reduce isn't working
	"reduce:": lambda procedure, list_obj: SchemeList(functools.reduce(procedure, list_obj.num_list)),
    "quote": quote,  # test and research
    "type": type, # lambda var: type(var), # str(type(var)).lstrip("<class '").rstrip("'>"),
    "=": lambda n1, n2: eq_proc(n1, n2)

    # make null?

	# add a include keyword to import a file - or maybe require
	# map, reduce, and filter - map and filter are done, reduce is being worked on
	# user input
    # add "cond" function
    # fix strings
    # add a "list" function
    # make symbols passable to arguments
}	


"""
To test:
- cond
- quote
- reduce
- null?
- include
- list
- pass symbols to to arguments
- pattern matching
- type
"""
