import sys

def defineAst(outDir, baseName, types):
    path = outDir + "/" + baseName + ".py"
    

def main():
    if(len(sys.argv) != 2):
        print("Usage: GenerateAST <directory name>")
    else:
        outputDir = sys.argv[1]

main()
