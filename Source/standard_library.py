# standard_library.py

import os
from Source.special_types import *

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
	print(data)

def car(lst_obj):
	if not isinstance(lst_obj, SchemeList):
		raise ValueError(f"'{lst_obj}' is not a list.")
	return lst_obj.num_list[0]

def cdr(lst_obj):
	if not isinstance(lst_obj, list):
		raise ValueError(f"'{lst_obj}' is not a list.")
	return lst_obj.num_list[1:]

def cons(var, lst_obj):
	if not isinstance(lst_obj, list):
		raise ValueError(f"'{lst_obj}' is not a list.")
	lst_obj = lst_obj.insert(0, var)
	return lst_obj

ENVIRONMENT = {
	"+": lambda *nums: sum(nums),
	"-": sub,
	"*": mult,
	"/": div,
	"<": lambda arg_one, arg_two: True if arg_one < arg_two else False,
	">": lambda arg_one, arg_two: True if arg_one > arg_two else False,
	"display": display,
	"if": lambda condition, stmt_1, stmt_2: stmt_1 if condition else stmt_2,
	"eq?": lambda thing_1, thing_2: thing_1 is thing_2,
	"eqv?": lambda thing_1, thing_2: thing_2 == thing_2,
	"equal?": lambda thing_1, thing_2: thing_2 == thing_2,
	"abs": abs,
	"write-file!": write_file,
	"append-file!": append_file,
	"read-file!": read_file,
	"shell!": lambda command: os.popen(command).read(),  # support strings as commands
	"car": car,
	"cdr": cdr,
	"cons": cons
	# add a include keyword to import a file
	# map, reduce, and filter
}	

