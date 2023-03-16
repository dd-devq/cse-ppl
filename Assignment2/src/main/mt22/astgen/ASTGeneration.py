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

    def visitFuncdecl(self, ctx: MT22Parser.FuncdeclContext):
        inherit = None
        id = ctx.ID().getText()
        if ctx.funcinherit():
            inherit = self.visit(ctx.funcinherit())
        return [FuncDecl(id, self.visit(ctx.functype()), self.visit(ctx.paramlist()), inherit, self.visit(ctx.body()))]

    def visitFunctype(self, ctx: MT22Parser.FunctypeContext):
        return self.visit(ctx.primitivetype())

    def visitFuncinherit(self, ctx: MT22Parser.FuncinheritContext):
        return ctx.ID().getText()

    def visitBody(self, ctx: MT22Parser.BodyContext):
        return self.visit(ctx.blockstmt())

    def visitParamlist(self, ctx: MT22Parser.ParamlistContext):
        return [self.visit(param) for param in ctx.param()]

    def visitParam(self, ctx: MT22Parser.ParamContext):
        out = ctx.OUT()
        inherit = ctx.INHERIT()
        return ParamDecl(ctx.ID().getText(), self.visit(ctx.primitivetype()), out, inherit)

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

    def visitExprlst(self, ctx: MT22Parser.ExprlstContext):
        return [self.visit(ex) for ex in ctx.expr()]

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
            return self.visit(ctx.funccall())

    def visitArrayL(self, ctx: MT22Parser.ArrayLContext):
        return ArrayLit(self.visit(ctx.exprlst()))

    def visitFunccall(self, ctx: MT22Parser.FunccallContext):
        id = ctx.ID().getText()
        if ctx.exprlst():
            expr = []
            for exprlst in ctx.exprlst():
                expr.extend(self.visit(exprlst))
            return FuncCall(id, expr)
        return FuncCall(id, [])

    def visitStmt(self, ctx: MT22Parser.StmtContext):
        if ctx.assignstmt():
            return self.visit(ctx.assignstmt())
        if ctx.vardecl():
            return self.visit(ctx.vardecl())
        if ctx.forstmt():
            return self.visit(ctx.forstmt())
        if ctx.ifstmt():
            return self.visit(ctx.ifstmt())
        if ctx.returnstmt():
            return self.visit(ctx.returnstmt())
        if ctx.callstmt():
            return self.visit(ctx.callstmt())
        if ctx.breakstmt():
            return self.visit(ctx.breakstmt())
        if ctx.continuestmt():
            return self.visit(ctx.continuestmt())
        if ctx.whilestmt():
            return self.visit(ctx.whilestmt())
        if ctx.dowhilestmt():
            return self.visit(ctx.dowhilestmt())
        return self.visit(ctx.blockstmt())

    def visitAssignstmt(self, ctx: MT22Parser.AssignstmtContext):
        if ctx.ID():
            return AssignStmt(ctx.Id().getText(), self.visit(ctx.expr()))
        return AssignStmt(self.visit(ctx.getChild(0)), self.visit(ctx.expr()))

    def visitForstmt(self, ctx: MT22Parser.ForstmtContext):
        stmt = AssignStmt(ctx.ID().getText(), self.visit(ctx.expr(0)))

        return ForStmt(stmt, self.visit(ctx.expr(1)), self.visit(ctx.expr(2)), self.visit(ctx.stmt()))

    def visitIfstmt(self, ctx: MT22Parser.IfstmtContext):
        if ctx.falsestmt():
            return IfStmt(self.visit(ctx.expr()), self.visit(ctx.truestmt()), None)
        else:
            return IfStmt(self.visit(ctx.expr()), self.visit(ctx.truestmt()), self.visit(ctx.falsestmt()))

    def visitTruestmt(self, ctx: MT22Parser.TruestmtContext):
        return self.visit(ctx.stmt())

    def visitFalsestmt(self, ctx: MT22Parser.FalsestmtContext):
        return self.visit(ctx.stmt())

    def visitReturnstmt(self, ctx: MT22Parser.ReturnstmtContext):
        if ctx.expr():
            return ReturnStmt(self.visit(ctx.expr()))
        return ReturnStmt(None)

    def visitCallstmt(self, ctx: MT22Parser.CallstmtContext):
        if ctx.exprlst():
            return CallStmt(ctx.ID().getText(), self.visit(ctx.exprlst()))
        return CallStmt(ctx.ID().getText(), [])

    def visitBreakstmt(self, ctx: MT22Parser.BreakstmtContext):
        return BreakStmt()

    def visitContinuestmt(self, ctx: MT22Parser.ContinuestmtContext):
        return ContinueStmt()

    def visitWhilestmt(self, ctx: MT22Parser.WhilestmtContext):
        if ctx.getChildCount() == 5:
            return WhileStmt(self.visit(ctx.expr()), self.visit(ctx.stmt(0)))
        else:
            return

    def visitDowhilestmt(self, ctx: MT22Parser.DowhilestmtContext):
        return DoWhileStmt(self.visit(ctx.expr()), self.visit(ctx.blockstmt()))

    def visitBlockstmt(self, ctx: MT22Parser.BlockstmtContext):
        stmts = flatten([self.visit(stmt) for stmt in ctx.stmt()])
        return BlockStmt(stmts)


def flatten(list_of_lists):
    if len(list_of_lists) == 0:
        return list_of_lists
    if isinstance(list_of_lists[0], list):
        return flatten(list_of_lists[0]) + flatten(list_of_lists[1:])
    return list_of_lists[:1] + flatten(list_of_lists[1:])
