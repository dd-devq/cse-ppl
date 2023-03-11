# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MT22Parser import MT22Parser
else:
    from MT22Parser import MT22Parser

# This class defines a complete generic visitor for a parse tree produced by MT22Parser.

class MT22Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by MT22Parser#program.
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#decl.
    def visitDecl(self, ctx:MT22Parser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vardecl.
    def visitVardecl(self, ctx:MT22Parser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funcdecl.
    def visitFuncdecl(self, ctx:MT22Parser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#idlst.
    def visitIdlst(self, ctx:MT22Parser.IdlstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#primitivetype.
    def visitPrimitivetype(self, ctx:MT22Parser.PrimitivetypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exprlst.
    def visitExprlst(self, ctx:MT22Parser.ExprlstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr.
    def visitExpr(self, ctx:MT22Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr1.
    def visitExpr1(self, ctx:MT22Parser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr2.
    def visitExpr2(self, ctx:MT22Parser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr3.
    def visitExpr3(self, ctx:MT22Parser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr4.
    def visitExpr4(self, ctx:MT22Parser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr5.
    def visitExpr5(self, ctx:MT22Parser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr6.
    def visitExpr6(self, ctx:MT22Parser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr7_index.
    def visitExpr7_index(self, ctx:MT22Parser.Expr7_indexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr8.
    def visitExpr8(self, ctx:MT22Parser.Expr8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#adding.
    def visitAdding(self, ctx:MT22Parser.AddingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#multiplying.
    def visitMultiplying(self, ctx:MT22Parser.MultiplyingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#unary.
    def visitUnary(self, ctx:MT22Parser.UnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#relational.
    def visitRelational(self, ctx:MT22Parser.RelationalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#strconcate.
    def visitStrconcate(self, ctx:MT22Parser.StrconcateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#unarylogical.
    def visitUnarylogical(self, ctx:MT22Parser.UnarylogicalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#binarylogical.
    def visitBinarylogical(self, ctx:MT22Parser.BinarylogicalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#sign.
    def visitSign(self, ctx:MT22Parser.SignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#operands.
    def visitOperands(self, ctx:MT22Parser.OperandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arrayType.
    def visitArrayType(self, ctx:MT22Parser.ArrayTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dimensions.
    def visitDimensions(self, ctx:MT22Parser.DimensionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dimension.
    def visitDimension(self, ctx:MT22Parser.DimensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arrayl.
    def visitArrayl(self, ctx:MT22Parser.ArraylContext):
        return self.visitChildren(ctx)



del MT22Parser