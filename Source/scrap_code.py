# tree.py
  
EXPRESSION = "2 * 7 + 3"

class BinaryOperator:
        def __init__(self, operator, left, right):  # assumed length of two
                self.operator = operator
                self.left = left
                self.right = right

class Add(BinaryOperator):
        def __init__(self, left, right):
                super().__init__("+", left, right)

# eval.py

def eval_(parsed_program):
	procedure = parsed_program[0]
	arguments = parsed_program[1:]
	print(procedure, "\n", arguments)
	for argument in arguments:
		eval_(parsed_program)

if __name__ == "__main__":
	import parse

	program = """
	(define factorial (lambda (n)
                (if (< n 2)
                n
                (* n (factorial (- n 1))))))
    """
	parsed_program = parse.parse(program)
	eval_(parsed_program)


# symbol_table.py


import syntax, math, operator as op


def standard_environment() -> syntax.Environment:
	std_env = syntax.Environment()

	std_env.update(vars(math))

	std_env.update(
		{
		"abs": abs,
		"append": op.add,
		"apply": lambda func, args: procedure(*args)

		}
		)

	'''
	for key, value in std_env.items():
		print(key, value, sep = " | ")
	'''

# my std lib:
'''
+
-
*
/
car
cdr
cons
eq?
expt
equal?
length
list?
map
max
min
not
null?
number?
procedure?
round
symbol?


'''


if __name__ == "__main__":
	standard_environment()







	"""
# OH MY GOD FIX THE BUGS IT'S A MESS

prev_prod_name, its_definition = "", ""

def evaluate(parsed_code):
	global prev_prod_name, its_definition

	if not isinstance(parsed_code, list):
		return parsed_code

	procedure_name, arguments = parsed_code[0], parsed_code[1:]

	

	print(f"Previous procedure name: {prev_prod_name}")
	print(f"Current procedure name: {procedure_name}")

	if procedure_name == "lambda":
		print("Case 1")
		procedure = Lambda(arguments)

		if prev_prod_name == "define":
			print("Defining procedure")
			define(its_definition, procedure)
			return
	else:
		print("Case 2")

		for index, argument in enumerate(arguments):
			try:
				if (variable_value := symbol_table.get(argument)) is not None:
					arguments[index] = variable_value
			except TypeError:
				arguments[index] = evaluate(argument)

		procedure = None
		try:
			procedure = ENVIRONMENT[procedure_name]
		except KeyError:
			try:
				procedure = symbol_table[procedure_name]
			except KeyError:
				raise UnboundLocalError(f"Undefined procedure \"{procedure_name}\"")

		try: prev_prod_name, its_definition = procedure_name, arguments[0]
		except IndexError: prev_prod_name, its_definition = "", ""
		print(f"Redefined previous procedure name to {prev_prod_name}")
		print(f"Redefined previous variable name to {its_definition}")
		return procedure(*[evaluate(arg) for arg in arguments])

	"""


	"""
	if not isinstance(parsed_code, list):
		return parsed_code

	procedure_name = parsed_code[0]
	arguments = parsed_code[1:]

	print(f"Procedure name: {procedure_name}")

	if procedure_name == "lambda":
		# define(procedure_name, Lambda(arguments))
		# return symbol_table[procedure_name]
		print("Procedure name is lambda")
		print(f"Arguments: {arguments}")

		procedure = Lambda(arguments)

		if previous_procedure_name == "define":
			define(procedure_name, procedure)
			return

	for index, argument in enumerate(arguments):
		try:
			if (variable_value := symbol_table.get(argument)) is not None:  # variable found in symbol table
				arguments[index] = variable_value
		except TypeError:  # unhashable type, list (for nested s-expressions)
			arguments[index] = evaluate(argument)


			#####ELSE
	procedure = None
	try:
		procedure = ENVIRONMENT[procedure_name]
	except KeyError:
		try:
			procedure = symbol_table[procedure_name]
		except KeyError:
			raise UnboundLocalError(f"Undefined procedure \"{procedure_name}\"")

	#####
	global previous_procedure_name
	previous_procedure_name = procedure_name
	#####

	return procedure(*[evaluate(arg) for arg in arguments])
	"""

# define procedures next
# then lists after that
# note: 'var is like var.__repr__





		"""
		argument_map = dict(zip(self.parameters, arguments))
		print(argument_map)

		expr_copy = deepcopy(self.expression)
		for index, term in enumerate(expr_copy):
			mapped_value = argument_map[term]
			expr_copy[index] = mapped_value
		"""









		# print(self, self.parameters, self.expression)


		"""
		argument_map = dict(zip(self.parameters, arguments))
		print(argument_map)

		copy_expression = deepcopy(self.expression)
		print(copy_expression)

		for i, a in argument_map.items():
			copy_expression[i] = a

		print(copy_expression)
		"""

		# (define incr (lambda (x) (+ x 1)))


		"""
		argument_map = dict(zip(self.parameters, arguments))
		copy_expression = deepcopy(self.expression)
		for index, symbolic_var_name in argument_map.items():
			try:
				copy_expression[index] = argument_map[symbolic_var_name]
			except KeyError:
				raise AttributeError(f"Incorrect argument {symbolic_var_name}")
		print("At end of call method")
		return evaluate(copy_expression)
		"""







		"""
		argument_map = dict(zip(self.parameters, arguments))
		expr_copy = deepcopy(self.expression)
		for index, term in enumerate(expr_copy):
			try:
				if isinstance(term, list):
					term = evaluate()
				expr_copy[index] = argument_map[term]
			except KeyError:
				pass
		"""


		"""
			a = expr_copy[index]
			print(f"A: {a}")

			print(f"Argument map: {argument_map}")
			print(f"Term: {term}")
		return
			# expr_copy[index] = argument_map[term]

		print("Done")

		print("Expr copy: ", expr_copy)
		"""

		"""
			try:
				expr_copy[index] = argument_map[term]
			except KeyError:
				print("Error", index, term)
				expr_copy[index] = symbol_table[term]
		"""


		"""
			try:
				print("Argument map:", argument_map)
				print("Term:", term)
				print("Expression copy:", expr_copy)
				print("Index:", index)
				expr_copy[index] = argument_map[term]
			except KeyError:
				try: expr_copy[index] = ENVIRONMENT[term]
				except KeyError:
					try: expr_copy[index] = symbol_table[term]
					except KeyError:
						raise AttributeError(f"Incorrect argument {expr_copy[index]}")

			except TypeError:
				print("Type error")
		"""
		"""
			except TypeError:
				expr_copy[index] = argument_map[evaluate(term)]
		"""

		"""
			(define incr (lambda (x) (+ x 1)))
			(define double (lambda (x) (incr (incr x))))
		"""

#####


		"""
		argument_mapping = dict(zip(self.parameters, arguments))

		current_expression = deepcopy(self.expression)

		# will not work
		while isinstance(current_expression, list):
			for out_index, sub_expression in enumerate(current_expression):
				for in_index, token in enumerate(sub_expression):
					try:
						# x would get replaced by 5, for example
						current_expression[out_index][in_index] = argument_mapping[token]
					except KeyError:
						pass

		return evaluate(current_expression)
		"""

		"""
		if isinstance(current_expression, list):
			for sub_expr in current_expression:
				return arguments.find(sub_expr)
		else:
			pass
		"""

##########

# call.py

incr = lambda num: num + 1
x = 5

expression = [incr, [incr, 5]]

def evaluate(expr):
	if isinstance(expr, list):
		for index, item in expr:
			expr[index] = evaluate(item)
	else:
		return expr()


##########


		"""
		def onionize(expr):
			if not isinstance(expr, list):  # x maps to 5
				try: return argument_mapping[expr]
				except KeyError: pass
			for item in expr:
				return onionize(item)

		modified_expr = list(onionize(main_expr))

		return modified_expr
		"""

##################

		"""
		else:
			if type(expr) not in (str, int, float, list, dict):
				raise ValueError(f"Undefined variable {expr}")
			elif expr in ENVIRONMENT: return ENVIRONMENT[expr]
			elif expr in symbol_table: return symbol_table[expr]
			elif expr in self.parameters:
				expr_spot = self.parameters.index(expr)
				var_value = arguments[expr_spot]
				return var_value
			else:
				return expr
		"""


##################

		"""
		procedure = None

		try:
			procedure = ENVIRONMENT[procedure_name]
			print("Got it")
		except KeyError:
			try:
				procedure = symbol_table[procedure_name]
				print("Got it second time")
			except KeyError:
				raise UnboundLocalError(f"Undefined procedure \"{procedure_name}\"")
		"""