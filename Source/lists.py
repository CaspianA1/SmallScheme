# lists.py

class SchemeList:
	def __init__(self, num_list):
		self.num_list = num_list

	def __getitem__(self, start = 0, stop = None, step = 1):
		if stop is None: stop = len(self.num_list)
		return self.num_list[start:stop:step]

	def __len__(self):
		return len(self.num_list)

	def __str__(self):
		string_repr = "("

		for item in self.num_list:
			string_repr += f"{item} "

		return string_repr.rstrip() + ")"

	car = lambda self: self.num_list[0]
	cdr = lambda self: self.num_list[1:]
	cons = lambda self, item: self.num_list.insert(0, item)

if __name__ == "__main__":
	l = SchemeList([1, 2, 3, 4, 5])

	l.cons(5)

	print(l)

	# working with this class should be much easier