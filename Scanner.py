import TokenType

class Scanner:
	current = 0
	start = 0
	line = 1
	def Scanner(source):
		self.source = source

	def scanTokens():
		while(not isAtEnd()):
			self.start = self.current
			scanToken()
		tokens.append(Token(EOF, "", None, line))

	def scanToken():
		c = advance();
		if(c == '('):
			addToken(LEFT_PAREN)
		elif(c == ')'):
			addToken(RIGHT_PAREN)
		elif(c == '{'):
			addToken(LEFT_BRACE)
		elif(c == '}'):
			addToken(RIGHT_BRACE)
		elif(c == ','):
			addToken(COMMA)
		elif(c == '.'):
			addToken(DOT)
		elif(c == '-'):
			addToken(MINUS)
		elif(c == '+'):
			addToken(PLUS)
		elif(c == ';'):
			addToken(SEMICOLON)
		elif(c == '*'):
			addToken(STAR)
		else:
			plox.error(line, "Unexpected character")

	def advance():
		current += 1
		return self.source[1:]

	def addToken(type, literal=None):
		text = self.source[start:current]
		tokens.append(Token(type, text, literal, line))

	def isAtEnd():
		return current >= len(self.source)