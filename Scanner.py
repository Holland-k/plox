from TokenType import *
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
                return self.tokens

	def scanToken(self):
		c = self.advance()
                print(c)
		if(c == '('):
			self.addToken(LEFT_PAREN)
		elif(c == ')'):
			self.addToken(RIGHT_PAREN)
		elif(c == '{'):
			self.addToken(LEFT_BRACE)
		elif(c == '}'):
			self.addToken(RIGHT_BRACE)
		elif(c == ','):
			self.addToken(COMMA)
		elif(c == '.'):
			self.addToken(DOT)
		elif(c == '-'):
			self.addToken(MINUS)
		elif(c == '+'):
			self.addToken(PLUS)
		elif(c == ';'):
			self.addToken(SEMICOLON)
		elif(c == '*'):
			self.addToken(STAR)
                elif(c == '!'):
                        if(self.match('=')):
                                self.addToken(BANG_EQUAL)
                        else:
                                self.addToken(TokenType(12))
                elif(c == '='):
                        if(self.match('=')):
                                self.addToken(EQUAL_EQUAL)
                        else:
                                self.addToken(EQUAL)
                elif(c == '<'):
                        if(self.match('=')):
                                self.addToken(LESS_EQUAL)
                        else:
                                self.addToken(LESS)
                elif(c == '>'):
                        if(self.match('=')):
                                self.addToken(GREATER_EQUAL)
                        else:
                                self.addToken(GREATER)
                elif(c == '/'):
                        if(self.match('/')):
                                while((self.peek() != '\n') and (not self.isAtEnd())):
                                        self.advance()
                        else:
                                self.addToken(SLASH)
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
		return self.source[self.current-1]

        def peek(self):
                if(self.isAtEnd()):
                        return '\0'
                return self.source[self.current]

        def peekNext(self):
                if(self.current +1 >= len(self.source)):
                        return '\0'
                return self.source[self.current+1]

	def addToken(self, ttype, literal=None):
		text = self.source[self.start:self.current]
                print("adding token " + text)
		self.tokens.append(Token(ttype, text, literal, self.line))

	def isAtEnd(self):
		return self.current >= len(self.source)

        def string(self):
                while((self.peek() != '"') and (not self.isAtEnd())):
                        if(self.peek() == '\n'):
                                self.line += 1
                        advance()
                if(self.isAtEnd()):
                        plox.error(self.line, "Unterminated string.")
                        return
                advance()
                value = self.source[(start+1):(current+1)]
                self.addToken(STRING, value)

        def isDigit(self, c):
                return c >= '0' and c <= '9'

        def number(self):
                while(isDigit(self.peek())):
                        advance()
                if(self.peek() == '.' and isDigit(self.peekNext())):
                        advance()
                        while(isDigit(self.peek())):
                                advance()
                self.addToken(Number, float(self.source[self.start,self.current]))
