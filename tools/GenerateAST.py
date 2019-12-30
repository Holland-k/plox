import sys

def defineType(fn, baseName, className, fieldList):
    #class Binary(Expr):0
    fn.write("class " + className + "(" + baseName + "):\n")

    #def Binary(Expr left, Token operator, Expr right):
    fn.write("    def " + className + "(" + fieldList + "):\n")
    fields = fieldList.split(", ")
    for f in fields:
        name = f.split(" ")[1]
        #    self.left = left
        fn.write("        self." + name + " = " + name + "\n")
    fn.write("\n")
    
def defineAST(outDir, baseName, types):
    path = outDir + "/" + baseName + ".py"
    writeFile = open(path, "a")

    writeFile.write("from abc import ABC\n\n")
    writeFile.write("class " + baseName + ":\n\n")

    defineVisitor(writeFile, baseName, types)

    for t in types:
        className = t.split(":")[0].strip()
        fields = t.split(":")[1].strip()
        defineType(writeFile, baseName, className, fields)
        writeFile.write("\n")
        writeFile.write("    def accept(Visitor visitor):\n")
        writeFile.write("        return visitor.visit" +
                        className + baseName + "(self)\n\n")
       
    writeFile.close()

def defineVisitor(writeFile, baseName, types):
    writeFile.write("class Visitor(ABC):\n\n")
    for t in types:
        typeName = t.split(":")[0].strip()
        writeFile.write("   def visit" + typeName + baseName + "(" + typeName + " " + baseName.lower() + "):\n")
        writeFile.write("      pass\n\n")

def main():
    if(len(sys.argv) != 2):
        print("Usage: GenerateAST <directory name>")
    else:
        outputDir = sys.argv[1]
        defineAST(outputDir, "Expr", [
            "Binary   : Expr left, Token operator, Expr right",
            "Grouping : Expr expression",
            "Literal  : Object value",
            "Unary    : Token operator, Expr right"
            ])
2
main()
