# main.py


from Source import parse as p
# from Source.evaluate import evaluate
from Source.neo_evaluate import evaluate

BLINK = "\x1b[5m{}\x1b[25m "

def repl():
	# wrapped_eval = lambda program: evaluate(p.parse(program))
	wrapped_eval = lambda program: evaluate(p.parse(program))

	"""
	proc_1 = "(define incr (lambda (x) (+ x 1)))"
	proc_2 = "(define double-incr (lambda (x) (incr (incr x))))"
	wrapped_eval(proc_1)
	wrapped_eval(proc_2)

	lst_decl = "(define lst '(1 2 3 4 5))"
	parsed = p.parse(lst_decl)
	print(parsed)
	"""

    	# wrapped_eval("(define lst '(1 2 3 4 5 6))")

	while True:
		expression = input(BLINK.format(">"))
		result = wrapped_eval(expression)
		if result is not None:
			print(result)


if __name__ == "__main__":
	repl()
