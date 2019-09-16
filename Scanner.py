from TokenType import TokenType
from Token import Token

class Scanner:
	current = 0
	start = 0
	line = 1
        tokens = []
        
	def __init__(self, source):
		self.source = source

	def scanTokens(self):
		while(not self.isAtEnd()):
			self.start = self.current
			self.scanToken()
		self.tokens.append(Token(TokenType.EOF, "", None, self.line))

	def scanToken(self):
		c = self.advance();
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
                elif(c == '"'):
                        string()
                elif(self.isDigit(c)):
                        number()
                else:
			##plox.error(line, "Unexpected character")
                        pass

        def match(self, c):
                if(self.isAtEnd()):
                        return False
                if(self.source[self.current] != c):
                        return False
                self.current += 1
                return True
        
	def advance(self):
		self.current += 1
		return self.source[1:]

        def peek(self):
                if(isAtEnd()):
                        return '\0'
                return this.source[self.current]

        def peekNext(self):
                if(self.current +1 >= len(self.source)):
                        return '\0'
                return self.source[self.current+1]

	def addToken(self, type, literal=None):
		text = self.source[start:current]
		tokens.append(Token(type, text, literal, line))

	def isAtEnd(self):
		return self.current >= len(self.source)

        def string(self):
                while((peek() != '"') and (not isAtEnd())):
                        if(peek() == '\n'):
                                self.line += 1
                        advance()
                if(isAtEnd()):
                        plox.error(self.line, "Unterminated string.")
                        return
                advance()
                value = self.source[(start+1):(current+1)]
                addToken(STRING, value)

        def isDigit(self, c):
                return c >= '0' and c <= '9'

        def number(self):
                while(isDigit(peek())):
                        advance()
                if(peek() == '.' and isDigit(peekNext())):
                        advance()
                        while(isDigit(peek())):
                                advance()
                addToken(Number, float(self.source[self.start,self.current]))
