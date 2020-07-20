# parse.py

import Source.syntax as syntax

def tokenize(chars: str) -> list:
	tokens = chars.replace('(', ' ( ').replace(')', ' ) ')  # .split()
	token_buffer = [""]

	# package strings correctly
	string_find_started = False 
	str_buffer = ""
	for char in tokens:
		if char == "\"":
			if string_find_started:
				str_buffer += char
				token_buffer.append(str_buffer)
				str_buffer = ""
				string_find_started = False
				continue
			else:
				string_find_started = True
		if string_find_started:
			str_buffer += char
		else:
			if char == " ":
				token_buffer.append(char)
			else:
				token_buffer[-1] += char

	token_buffer = [a for a in [a.strip() for a in token_buffer] if a != ""]

	# non-list symbol support
	for index, token in enumerate(token_buffer):	
		if token != "'" and token.startswith("'"):
			tokens[index] = "'"
			tokens.insert(index + 1, token[1:])

	return token_buffer


def parse(program: str) -> list:
	return read_from_tokens(tokenize(program))

def read_from_tokens(tokens: list) -> syntax.Expression:
	# raise SyntaxError("Unexpected end of file")
	if len(tokens) == 0: return

	current_token = tokens.pop(0)
	if current_token == "(":
		sub_expr = []

		while tokens[0] != ")":
			sub_expr.append(read_from_tokens(tokens))

		tokens.pop(0)  # remove last ")"
		return sub_expr

	elif current_token == ")": raise SyntaxError("Unexpected \")\"")

	else: return atom(current_token)

def atom(token: str) -> syntax.Atom:
	if token[0] == "\"" and token.endswith("\""):
		return token[1:-1]
	try:
		return int(token)
	except ValueError:
		try:
			return float(token)
		except ValueError:
                        return str(token)
			# return syntax.Symbol(token)
