# main.py


from Source import parse as p
# from Source.evaluate import evaluate
from Source.neo_evaluate import evaluate

BLINK = "\x1b[5m{}\x1b[25m "

def repl():
	wrapped_eval = lambda program: evaluate(p.parse(program))

	wrapped_eval("(define pi '(3 1 4 1 5))")

	while True:
		expression = input(BLINK.format(">"))
		result = wrapped_eval(expression)
		if result is not None:
			print(result)


if __name__ == "__main__":
	repl()
