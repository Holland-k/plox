import unittest
import Scanner
class TestLox(unittest.TestCase):
    def test_scanner(self):
        s = Scanner.Scanner("(")
        self.assertEqual(s.scanTokens()[0].toString(), "TokenType.LEFT_PAREN ( None") 
        s.source = ")"
        s.current = 0
        s.start = 0
        s.line = 1
        s.tokens = []
        self.assertEqual(s.scanTokens()[0].toString(), "TokenType.RIGHT_PAREN ) None")
        s = Scanner.Scanner("{")
        s.source = "{"
        s.current = 0
        s.start = 0
        s.line = 1
        s.tokens = []
        self.assertEqual(s.scanTokens()[0].toString(), "TokenType.LEFT_BRACE { None")
        s = Scanner.Scanner("}")
        s.source = "}"
        s.current = 0
        s.start = 0
        s.line = 1
        s.tokens = []
        self.assertEqual(s.scanTokens()[0].toString(), "TokenType.RIGHT_BRACE } None")
        s = Scanner.Scanner(",")
        s.source = ","
        s.current = 0
        s.start = 0
        s.line = 1
        s.tokens = []
        self.assertEqual(s.scanTokens()[0].toString(), "TokenType.COMMA , None")
        s = Scanner.Scanner(".")
        s.source = "."
        s.current = 0
        s.start = 0
        s.line = 1
        s.tokens = []
        self.assertEqual(s.scanTokens()[0].toString(), "TokenType.DOT . None")
        s = Scanner.Scanner("-")
        s.source = "-"
        s.current = 0
        s.start = 0
        s.line = 1
        s.tokens = []
        self.assertEqual(s.scanTokens()[0].toString(), "TokenType.MINUS - None")
        s = Scanner.Scanner("+")
        s.source = "+"
        s.current = 0
        s.start = 0
        s.line = 1
        s.tokens = []
        self.assertEqual(s.scanTokens()[0].toString(), "TokenType.PLUS + None")
        s = Scanner.Scanner(";")
        s.source = ";"
        s.current = 0
        s.start = 0
        s.line = 1
        s.tokens = []
        self.assertEqual(s.scanTokens()[0].toString(), "TokenType.SEMICOLON ; None")
        s = Scanner.Scanner("*")
        s.source = "*"
        s.current = 0
        s.start = 0
        s.line = 1
        s.tokens = []
        self.assertEqual(s.scanTokens()[0].toString(), "TokenType.STAR * None")
        s = Scanner.Scanner("!")
        s.source = "!"
        s.current = 0
        s.start = 0
        s.line = 1
        s.tokens = []
        self.assertEqual(s.scanTokens()[0].toString(), "TokenType.BANG ! None")
        s = Scanner.Scanner("!=")
        s.source = "!="
        s.current = 0
        s.start = 0
        s.line = 1
        s.tokens = []
        self.assertEqual(s.scanTokens()[0].toString(), "TokenType.BANG_EQUAL != None")
        s = Scanner.Scanner("==")
        s.source = "=="
        s.current = 0
        s.start = 0
        s.line = 1
        s.tokens = []
        self.assertEqual(s.scanTokens()[0].toString(), "TokenType.EQUAL_EQUAL == None")
        s = Scanner.Scanner("=")
        s.source = "="
        s.current = 0
        s.start = 0
        s.line = 1
        s.tokens = []
        self.assertEqual(s.scanTokens()[0].toString(), "TokenType.EQUAL = None")
        s = Scanner.Scanner("<=")
        s.source = "<="
        s.current = 0
        s.start = 0
        s.line = 1
        s.tokens = []
        self.assertEqual(s.scanTokens()[0].toString(), "TokenType.LESS_EQUAL <= None")
        s = Scanner.Scanner("<")
        s.source = "<"
        s.current = 0
        s.start = 0
        s.line = 1
        s.tokens = []
        self.assertEqual(s.scanTokens()[0].toString(), "TokenType.LESS < None")
        s = Scanner.Scanner(">=")
        s.source = ">="
        s.current = 0
        s.start = 0
        s.line = 1
        s.tokens = []
        self.assertEqual(s.scanTokens()[0].toString(), "TokenType.GREATER_EQUAL >= None")
        s = Scanner.Scanner(">")
        s.source = ">"
        s.current = 0
        s.start = 0
        s.line = 1
        s.tokens = []
        self.assertEqual(s.scanTokens()[0].toString(), "TokenType.GREATER > None")
        s = Scanner.Scanner("/")
        s.source = "/"
        s.current = 0
        s.start = 0
        s.line = 1
        s.tokens = []
        self.assertEqual(s.scanTokens()[0].toString(), "TokenType.SLASH / None")
        s = Scanner.Scanner("//test")
        s.source = "//test"
        s.current = 0
        s.start = 0
        s.line = 1
        s.tokens = []
        self.assertEqual(s.scanTokens()[0].toString(), "TokenType.EOF  None")
        s = Scanner.Scanner(" ")
        s.source = " "
        s.current = 0
        s.start = 0
        s.line = 1
        s.tokens = []
        self.assertEqual(s.scanTokens()[0].toString(), "TokenType.EOF  None")
        s = Scanner.Scanner("\r")
        s.source = "\r"
        s.current = 0
        s.start = 0
        s.line = 1
        s.tokens = []
        self.assertEqual(s.scanTokens()[0].toString(), "TokenType.EOF  None")
        s = Scanner.Scanner("\n")
        s.source = "\n"
        s.current = 0
        s.start = 0
        s.line = 1
        s.tokens = []
        self.assertEqual(s.scanTokens()[0].toString(), "TokenType.EOF  None")
        s = Scanner.Scanner("\"test\"")
        s.source = "\"test\""
        s.current = 0
        s.start = 0
        s.line = 1
        s.tokens = []
        self.assertEqual(s.scanTokens()[0].toString(), "TokenType.STRING \"test\" test\"")
        s = Scanner.Scanner("12")
        s.source = "12"
        s.current = 0
        s.start = 0
        s.line = 1
        s.tokens = []
        self.assertEqual(s.scanTokens()[0].toString(), "TokenType.NUMBER 12 12.0")
        s = Scanner.Scanner("12.0")
        s.source = "12.0"
        s.current = 0
        s.start = 0
        s.line = 1
        s.tokens = []
        self.assertEqual(s.scanTokens()[0].toString(), "TokenType.NUMBER 12.0 12.0")
        
        
if __name__ == '__main__':
    unittest.main()
