#!/usr/bin/env python3

import os, sys
from Source import parse as p
from Source.evaluate import evaluate

BLINK = "\x1b[5m{}\x1b[25m "

wrapped_eval = lambda program: evaluate(p.parse(program))

def repl():
	expression = ""
	spacing = BLINK.format(">")
	times_indented = 0
	while True:
		partial_expression = input(spacing)
		expression += f" {partial_expression}"
		left_parens = expression.count("(")
		right_parens = expression.count(")")
		if left_parens == right_parens or right_parens > left_parens:
			result = wrapped_eval(expression)
			if result is not None:
				print(result)
			spacing = BLINK.format(">")
			expression = ""
			times_indented = 0
		else:
			times_indented += 1
			if times_indented == 1:
				spacing = "   "
			else:
				spacing = "  " + spacing

def read_from_file(file_name):
	expression = ""
	for row in [i.strip() for i in open(file_name).readlines() if i != "\n"]:
		expression += f" {row}"
		if expression.count("(") == expression.count(")"):
			wrapped_eval(expression)
			expression = ""

if __name__ == "__main__":
	start_up_screen = """ _______________________________________________
| SmallScheme - a minimalist version of Scheme |
|      github.com/CaspianA1/SmallScheme        |
|_ By Caspian Ahlberg, licensed under the GPL _|
 \____________________________________________/
	"""

	if len(sys.argv) == 1:
		print(start_up_screen)
		try:
			repl()
		except KeyboardInterrupt:
			print("\033[2K\r", end = ""); sys.exit()
	elif len(sys.argv) == 2:
		read_from_file(sys.argv[1])
	elif len(sys.argv) == 3:
		print(start_up_screen)
		if sys.argv[1] == "-l":
			read_from_file(sys.argv[2])
			try:
				repl()
			except KeyboardInterrupt:
				print("\033[2K\r", end = ""); sys.exit()
