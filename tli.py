import operator as oper; from functools import reduce

num_op = lambda op, nums: reduce(lambda x, y: op(x, y), nums)

env = {"+": lambda *nums: sum(nums), "-": lambda *nums: num_op(oper.sub, nums), "*": lambda *nums: num_op(oper.mul, nums),
       "/": lambda *nums: num_op(oper.truediv, nums), "=": lambda *nums: num_op(oper.eq, nums),">": lambda n1, n2: n1 > n2,
       "<": lambda n1, n2: n1 < n2, "define": lambda name, val: env.update({name: val}), "display": lambda var: print(find_val(var))}

def parse(tokens):
    if not tokens: return
    curr = tokens.pop(0)
    if curr == "(":
        ast = []
        while tokens[0] != ")":
            ast.append(parse(tokens))
        tokens.pop(0); return ast
    elif curr == ")":
        print("SyntaxError: Unexpected \")\"")
    else:
        try: return int(curr)
        except ValueError:
            try: return float(curr)
            except ValueError: return str(curr)

find_val = lambda var: env[var] if var in env else var
eval_ = lambda code: find_val(code[0])(*[eval_(arg) for arg in code[1:]]) if isinstance(code, list) else find_val(code)

while True: eval_(parse(input("> ").replace("(", " ( ").replace(")", " ) ").split()))
