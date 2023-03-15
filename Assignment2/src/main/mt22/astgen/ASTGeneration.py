from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *


class ASTGeneration(MT22Visitor):
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        decls = []
        for decl in ctx.decl():
            decls.extend(self.visit(decl))
        return Program(decls)


    def visitDecl(self, ctx: MT22Parser.DeclContext):
        return self.visit(ctx.getChild(0))


    def visitVardecl(self, ctx: MT22Parser.VardeclContext):
        return self.visit(ctx.getChild(0))


    def visitNoassign(self, ctx: MT22Parser.NoassignContext):
        idlst = self.visit(ctx.idlst())
        primitivetype = self.visit(ctx.primitivetype())
        return [VarDecl(str(id), primitivetype) for id in idlst]


    def visitMultipleassign(self, ctx: MT22Parser.MultipleassignContext):
        id = [ctx.ID().getText()]
        extid, primitivetype, extexpr = self.visit(ctx.extassign())
        expr = [self.visit(ctx.expr())]
        id.extend(extid)
        expr.extend(extexpr)
        list(expr) 
        expr.reverse()
        return [VarDecl(str(id), primitivetype, expr) for id, expr in zip(id, expr)]


    def visitExtassign(self, ctx: MT22Parser.ExtassignContext):
        if ctx.extassign():
            id, expr = [ctx.ID().getText()], [self.visit(ctx.expr())]
            primitivetype = None
            extid, primitivetype, extexpr = self.visit(ctx.extassign())
            id += extid
            expr += extexpr
            return id, primitivetype, expr
        else:
            primitivetype = self.visit(ctx.primitivetype())
            return [], primitivetype, []


    def visitPrimitivetype(self, ctx: MT22Parser.PrimitivetypeContext):
        if ctx.INTEGER():
            return IntegerType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.STRING():
            return StringType()
        elif ctx.BOOLEAN():
            return BooleanType()
        elif ctx.VOID():
            return VoidType()
        elif ctx.AUTO():
            return AutoType()
        elif ctx.arrayType():
            return self.visit(ctx.arrayType())


    def visitArrayType(self, ctx: MT22Parser.ArrayTypeContext):
        return ArrayType(self.visit(ctx.dimension()), self.visit(ctx.primitivetype()))


    def visitDimension(self, ctx: MT22Parser.DimensionContext):
        return [index.getText() for index in ctx.INTL()]

    def visitIdlst(self, ctx: MT22Parser.IdlstContext):
        return [id.getText() for id in ctx.ID()]


    def visitExpr(self, ctx: MT22Parser.ExprContext):

        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        return BinExpr(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))


    def visitExpr1(self, ctx: MT22Parser.Expr1Context):
        if ctx.getChildCount() == 3:
            return BinExpr(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
        return self.visit(ctx.getChild(0))        


    def visitExpr2(self, ctx: MT22Parser.Expr2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        return BinExpr(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))


    def visitExpr3(self, ctx: MT22Parser.Expr3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        return BinExpr(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))


    def visitExpr4(self, ctx: MT22Parser.Expr4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        return BinExpr(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
    

    def visitExpr5(self, ctx: MT22Parser.Expr5Context):
        if ctx.getChildCount() == 2:
            return UnExpr(ctx.getChild(0).getText(), self.visit(ctx.getChild(1)))
        return self.visit(ctx.getChild(0))
        
    
    def visitExpr6(self, ctx: MT22Parser.Expr6Context):
        if ctx.getChildCount() == 2:
            return UnExpr(ctx.getChild(0).getText(), self.visit(ctx.getChild(1)))
        return self.visit(ctx.getChild(0))
        
    
    def visitExpr7(self, ctx: MT22Parser.Expr7Context):
        if ctx.getChildCount() == 4:
            return ArrayCell(self.visit(ctx.expr7()), self.visit(ctx.exprlst()))
        return self.visit(ctx.getChild(0))
        

    def visitExpr8(self, ctx: MT22Parser.Expr8Context):
        if ctx.getChildCount() == 3:
            return self.visit(ctx.expr())
        return self.visit(ctx.getChild(0))
        
    def visitExprlst(self, ctx: MT22Parser.ExprlstContext):
        return [self.visit(ex) for ex in ctx.expr()]
        
    def visitOperands(self, ctx: MT22Parser.OperandsContext):
        if ctx.INTL():
            return IntegerLit(ctx.INTL().getText())
        elif ctx.FLOATL():
            return FloatLit(ctx.FLOATL().getText())
        elif ctx.STRINGL():
            return StringLit(ctx.STRINGL().getText())
        elif ctx.BOOLL():
            return BooleanLit(ctx.BOOLL().getText())
        elif ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.arrayL():
            return self.visit(ctx.arrayL())
        elif ctx.funccall():
            return

    def visitArrayL(self, ctx: MT22Parser.ArrayLContext):
        return ArrayLit(self.visit(ctx.exprlst()))