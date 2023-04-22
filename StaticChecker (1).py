from AST import *
from Visitor import *
from Utils import *
from StaticError import *
from main.mt22.utils.AST import IntegerType

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value


class StaticChecker(Visitor):
    global_env = [
        Symbol("readInteger", MType([],IntegerType())),
        Symbol("printInteger", MType(IntegerType(),VoidType())),
        Symbol("readFloat", MType([], FloatType())),
        Symbol("writeFloat", MType(FloatType(), VoidType())),
        Symbol("readBoolean", MType([], BooleanType())),
        Symbol("printBoolean", MType(BooleanType(), VoidType())),
        Symbol("readString", MType([], StringType())),
        Symbol("printString", MType(StringType(), VoidType())),
        #super
        Symbol("preventDefault", MType([], VoidType())),
    ]
    def __init__(self, ctx):
        self.ctx = ctx

    # helpfunction
    def check(self):
        return self.visit(self.ctx,StaticChecker.global_env)
    def redeclSymbol(name, sl):
        for symbol in sl:
            if name == symbol.name:
                return True
            else:
                return False

    # Program
    def visitProgram(self, ctx, o):
        #check for entry point
        entry_point = False
        for decl_ctx in ctx.decls:
            if isinstance(decl_ctx, FuncDecl):
                if (decl_ctx.name == 'main'):
                    entry_point = True
                    break
        if not entry_point: raise NoEntryPoint()
        
        self.func_list = []
        program_env = o

        for decl_ctx in ctx.decls:
            if isinstance(decl_ctx, VarDecl):
                #add vardecl into global_env
                program_env.append(self.visitVarDecl(decl_ctx, program_env))
            elif isinstance(decl_ctx, FuncDecl):
                # #check redeclared function
                # if decl_ctx.name in program_env:
                #     raise Redeclared(Function(), decl_ctx.name)
                # #update global environmentr and unused function list
                # return_type = self.visit(decl_ctx.return_type, program_env)
                # param_type=[self.visit(param.typ, None) for param in decl_ctx.params]
                # function = Symbol(decl_ctx.name, MType(param_type, return_type))
                # if function.name != 'main': self.func_list.append(function)
                # program_env.append(function)
                program_env.append(self.visitFuncDecl(decl_ctx, program_env))

    # Declare
    def visitVarDecl(self, ctx, o): 
        # if self.lookup(ctx.variable, o, lambda x: x.name) is None:
        #     varType= self.visit(ctx.varType,o)
        #     return Symbol(ctx.variable,varType)
        # else:
        #     raise Redeclared(Variable(),ctx.variable)
        for symbol in o:
            if ctx.name == symbol.name:
                raise Redeclared(Variable(), ctx.name)
        return Symbol(ctx.name, ctx.typ)

    
    def visitFuncDecl(self, ctx, o): 
        local_env = []
        #check redeclared parameter
        for param in ctx.params:
            if StaticChecker.redeclSymbol(param.name, local_env):
                raise Redeclared(Parameter(), param.name)
            else:
                local_env.append(self.visit(param,[]))
        
    def visitParamDecl(self, ctx, o): 
        return Symbol(ctx.name, ctx.type)

    # Statement

    def visitAssignStmt(self, ctx, o): pass

    def visitBlockStmt(self, ctx, o): pass

    def visitIfStmt(self, ctx, o): pass

    def visitForStmt(self, ctx, o): pass

    def visitWhileStmt(self, ctx, o): pass

    def visitDoWhileStmt(self, ctx, o): pass

    def visitBreakStmt(self, ctx, o): pass

    def visitContinueStmt(self, ctx, o): pass

    def visitReturnStmt(self, ctx, o): pass

    def visitCallStmt(self, ctx, o): pass

    # Expression

    def visitBinExpr(self, ctx, o): pass

    def visitUnExpr(self, ctx, o): pass

    def visitId(self, ctx, o): pass

    def visitArrayCell(self, ctx, o): pass

    def visitIntegerLit(self, ctx, o): 
        return IntegerType()

    def visitFloatLit(self, ctx, o): 
        return FloatType()

    def visitStringLit(self, ctx, o): 
        return StringType()

    def visitBooleanLit(self, ctx, o): 
        return BooleanType()

    def visitArrayLit(self, ctx, o):
        return ArrayType()

    def visitFuncCall(self, ctx, o): pass

    # Type

    def visitIntegerType(self, ctx, o): 
        return IntegerType()

    def visitFloatType(self, ctx, o): 
        return FloatType()

    def visitBooleanType(self, ctx, o): 
        return BooleanType()

    def visitStringType(self, ctx, o): 
        return StringType()
    
    def visitArrayType(self, ctx, o): 
        return ArrayType()

    def visitAutoType(self, ctx, o): 
        return AutoType()

    def visitVoidType(self, ctx, o): 
        return VoidType()


