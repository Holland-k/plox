
class Token:

	def __init__(self, type, lexeme, literal, line):
		self.type = type
		self.lexeme = lexeme
		self.literal = literal
		self.line = line

	def toString():
		st = self.type + " " + self.lexeme + " " + self.literal
		return st
