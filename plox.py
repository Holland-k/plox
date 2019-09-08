import sys

def scanner():
	return 0

def runSource(source):
	totalString = "".join(source)
	print("running " + totalString)
	

def runFile(fname):
	print("running a script called " + fname)
	f = open(fname, 'r')
	runSource(f.readlines())
	return 0

def runPrompt():
	print("entering the repl")
	while(True):
		print("> ")
		runSource(input())
	return 0

def main():
	if(len(sys.argv) > 2):
		print("Usage: plox <script>")
	elif(len(sys.argv) == 2):
		runFile(sys.argv[1])
	else:
		runPrompt()

main()

