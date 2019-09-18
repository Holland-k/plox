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
			self.addToken(TokenType(1))
		elif(c == ')'):
			self.addToken(TokenType(2))
		elif(c == '{'):
			self.addToken(TokenType(3))
		elif(c == '}'):
			self.addToken(TokenType(4))
		elif(c == ','):
			self.addToken(TokenType(5))
		elif(c == '.'):
			self.addToken(TokenType(6))
		elif(c == '-'):
			self.addToken(TokenType(7))
		elif(c == '+'):
			self.addToken(TokenType(8))
		elif(c == ';'):
			self.addToken(TokenType(9))
		elif(c == '*'):
			self.addToken(TokenType(11))
                elif(c == '!'):
                        if(self.match('=')):
                                self.addToken(TokenType(13))
                        else:
                                self.addToken(TokenType(12))
                elif(c == '='):
                        if(self.match('=')):
                                self.addToken(TokenType(15))
                        else:
                                self.addToken(TokenType(14))
                elif(c == '<'):
                        if(self.match('=')):
                                self.addToken(TokenType(19))
                        else:
                                self.addToken(TokenType(18))
                elif(c == '>'):
                        if(self.match('=')):
                                self.addToken(TokenType(17))
                        else:
                                self.addToken(TokenType(16))
                elif(c == '/'):
                        if(self.match('/')):
                                while((self.peek() != '\n') and (not self.isAtEnd())):
                                        self.advance()
                        else:
                                self.addToken(TokenType(10))
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
                self.addToken(TokenType(21), value)

        def isDigit(self, c):
                return c >= '0' and c <= '9'

        def number(self):
                while(isDigit(self.peek())):
                        advance()
                if(self.peek() == '.' and isDigit(self.peekNext())):
                        advance()
                        while(isDigit(self.peek())):
                                advance()
                self.addToken(TokenType(22), float(self.source[self.start,self.current]))
