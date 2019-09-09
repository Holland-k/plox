
class Token:

	def Token(type, lexeme, literal, line):
		self.type = type
		self.lexeme = lexeme
		self.literal = literal
		self.line = line

	toString():
		st = self.type + " " + self.lexeme + " " + self.literal
		return st