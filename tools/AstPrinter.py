
def AstPrinter(Expr.Visitor):
    def print(Expr exp):
        return exp.accept(self)

    def visitBinaryExpr(Expr.Binary exp):
        return parenthesize(exp.operator.lexeme, exp.left, exp.right)

    def visitGroupingExpr(Expr.Binary exp):
        return parenthesize("group", exp.expression)
    
    def visitLiteralExpr(Expr.Binary exp):
        if(exp.value == None):
            return None
        return str(exp.value)
    
    def visitUnaryExpr(Expr.Binary exp):
        return parenthesize(exp.operator.lexeme, exp.right)

    def parenthesize(name, exp):
        st = "(" + name
        for e in exp:
            st = st + " "
            st = st + e.accept(self)
        st = st + ")"

        return st

def main():
    exp = Expr.Binary(
        Expr.Unary(
            Token(TokenType.MINUS, "-", null, 1),
            Expr.Litaral(123)),
        Toke(TokenType.Star, "*", null, 1),
        Expr.Grouping(
            Expr.Literal(45.67)))

    print(AstPrinter.print(exp)


main()
