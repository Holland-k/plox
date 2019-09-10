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
                elif(c == '!'):
                        if(match('=')):
                                addToken(BANG_EQUAL)
                        else:
                                addToken(BANG)
                elif(c == '='):
                        if(match('=')):
                                addToken(EQUAL_EQUAL)
                        else:
                                addToken(EQUAL)
                elif(c == '<'):
                        if(match('=')):
                                addToken(LESS_EQUAL)
                        else:
                                addToken(LESS)
                elif(c == '>'):
                        if(match('=')):
                                addToken(GREATER_EQUAL)
                        else:
                                addToken(GREATER)
                elif(c == '/'):
                        if(match('/')):
                                while((peek() != '\n') and (not isAtEnd())):
                                      advance()
                        else:
                                addToken(SLASH)
                elif(c == ' '):
                        pass
                elif(c == '\r'):
                        pass
                elif(c == '\t'):
                        pass
                elif(c == '\n'):
                        self.line += 1
                else:
			plox.error(line, "Unexpected character")

        def match(c):
                if(isAteEnd()):
                        return False
                if(self.source[self.current] != c):
                        return False
                self.current += 1
                return True
        
	def advance():
		current += 1
		return self.source[1:]

        def peek():
                if(isAtEnd()):
                        return '\0'
                return this.source[this.current]

	def addToken(type, literal=None):
		text = self.source[start:current]
		tokens.append(Token(type, text, literal, line))

	def isAtEnd():
		return current >= len(self.source)
