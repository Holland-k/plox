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
			self.addToken(TokenType.LEFT_PAREN)
		elif(c == ')'):
			self.addToken(TokenType.RIGHT_PAREN)
		elif(c == '{'):
			self.addToken(TokenType.LEFT_BRACE)
		elif(c == '}'):
			self.addToken(TokenType.RIGHT_BRACE)
		elif(c == ','):
			self.addToken(TokenType.COMMA)
		elif(c == '.'):
			self.addToken(TokenType.DOT)
		elif(c == '-'):
			self.addToken(TokenType.MINUS)
		elif(c == '+'):
			self.addToken(TokenType.PLUS)
		elif(c == ';'):
			self.addToken(TokenType.SEMICOLON)
		elif(c == '*'):
			self.addToken(TokenType.STAR)
                elif(c == '!'):
                        if(self.match('=')):
                                self.addToken(TokenType.BANG_EQUAL)
                        else:
                                self.addToken(TokenType.BANG)
                elif(c == '='):
                        if(self.match('=')):
                                self.addToken(TokenType.EQUAL_EQUAL)
                        else:
                                self.addToken(TokenType.EQUAL)
                elif(c == '<'):
                        if(self.match('=')):
                                self.addToken(TokenType.LESS_EQUAL)
                        else:
                                self.addToken(TokenType.LESS)
                elif(c == '>'):
                        if(self.match('=')):
                                self.addToken(TokenType.GREATER_EQUAL)
                        else:
                                self.addToken(TokenType.GREATER)
                elif(c == '/'):
                        if(self.match('/')):
                                while((self.peek() != '\n') and (not self.isAtEnd())):
                                        self.advance()
                        else:
                                self.addToken(TokenType.SLASH)
                elif(c == ' '):
                        pass
                elif(c == '\r'):
                        pass
                elif(c == '\t'):
                        pass
                elif(c == '\n'):
                        self.line += 1
                elif(c == '"'):
                        self.string()
                elif(self.isDigit(c)):
                        self.number()
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
                        self.advance()
                if(self.isAtEnd()):
                        plox.error(self.line, "Unterminated string.")
                        return
                self.advance()
                value = self.source[(self.start+1):(self.current+1)]
                self.addToken(TokenType.STRING, value)

        def isDigit(self, c):
                return c >= '0' and c <= '9'

        def number(self):
                while(self.isDigit(self.peek())):
                        self.advance()
                if(self.peek() == '.' and self.isDigit(self.peekNext())):
                        self.advance()
                        while(self.isDigit(self.peek())):
                                self.advance()
                self.addToken(TokenType.NUMBER, float(self.source[self.start:self.current]))
