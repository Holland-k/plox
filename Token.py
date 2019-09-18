
class Token:

	def __init__(self, ttype, lexeme, literal, line):
		self.ttype = ttype
		self.lexeme = lexeme
		self.literal = literal
		self.line = line

	def toString(self):
		st = str(self.ttype) + " " + str(self.lexeme) + " " + str(self.literal)
		return st
