# parse.py

import Source.syntax as syntax

def tokenize(chars: str) -> list:
	return chars.replace('(', ' ( ').replace(')', ' ) ').split()

def parse(program: str) -> list:
	return read_from_tokens(tokenize(program))

def read_from_tokens(tokens: list) -> syntax.Expression:
	if len(tokens) == 0:
		return
		# raise SyntaxError("Unexpected end of file")

	current_token = tokens.pop(0)

	if current_token == "(":
		sub_expr = []

		while tokens[0] != ")":
			sub_expr.append(read_from_tokens(tokens))

		tokens.pop(0)  # remove last ")"
		return sub_expr

	elif current_token == ")":
		raise SyntaxError("Unexpected \")\"")

	else:
		return atom(current_token)

def atom(token: str) -> syntax.Atom:
	try:
		return int(token)
	except ValueError:
		try:
			return float(token)
		except ValueError:
			return syntax.Symbol(token)

if __name__ == "__main__":
	program = """
	(define factorial (lambda (n)
                (if (< n 2)
                n
                (* n (factorial (- n 1))))))
    """
	parsed_program = parse(program)
	print(parsed_program)
