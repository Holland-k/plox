import sys
import Scanner

hadError = False

def scanner(source):
	scanner = Scanner.Scanner(source)
	tokens = scanner.scanTokens()
	for i in tokens:
		print(i.toString())

def runSource(source):
	totalString = "".join(source)
	print("running " + totalString)
	scanner(source)

def error(lineNum, message):
	report(lineNum, "", message)

def report(lineNum, location, message):
	global hadError

	print("[Line " + String(lineNum) + "] Error" + where + ": " + message)
	hadError = True

def runFile(fname):
	print("running a script called " + fname)
	f = open(fname, 'r')
	runSource(f.readlines())
	if(hadError):
		sys.exit(65)

def runPrompt():
	print("entering the repl")
	while(True):
		print("> ")
		runSource(input())

def main():
	if(len(sys.argv) > 2):
		print("Usage: plox <script>")
	elif(len(sys.argv) == 2):
		runFile(sys.argv[1])
	else:
		runPrompt()

main()

