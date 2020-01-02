import Expr

def AstPrinter(Visitor):
    def print(exp):
        return exp.accept(self)

    def visitBinaryExpr(exp):
        return parenthesize(exp.operator.lexeme, exp.left, exp.right)

    def visitGroupingExpr(exp):
        return parenthesize("group", exp.expression)
    
    def visitLiteralExpr(exp):
        if(exp.value == None):
            return None
        return str(exp.value)
    
    def visitUnaryExpr(exp):
        return parenthesize(exp.operator.lexeme, exp.right)

    def parenthesize(name, exp):
        st = "(" + name
        for e in exp:
            st = st + " "
            st = st + e.accept(self)
        st = st + ")"

        return st

def run_main():
    exp = Expr.Binary(
        Expr.Unary(
            Token(TokenType.MINUS, "-", null, 1),
            Expr.Litaral(123)),
        Toke(TokenType.Star, "*", null, 1),
        Expr.Grouping(
            Expr.Literal(45.67)))

    print(AstPrinter.print(exp))

run_main()
