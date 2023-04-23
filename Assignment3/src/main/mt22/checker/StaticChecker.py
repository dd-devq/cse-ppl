from Visitor import Visitor
from Utils import Utils
from StaticError import *
from AST import *


class FType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype


class Symbol:
    def __init__(self, name, mtype, value=None):
        self.name = name
        self.mtype = mtype
        self.value = value


class GetEnv(Visitor, Utils):

    def __init__(self):
        self.global_env = {}

    def visitProgram(self, ctx: Program, o: object):
        o = self.global_env
        for decl in ctx.decls:
            self.visit(decl, o)
        return o

    def visitVarDecl(self, ctx: VarDecl, o: object):
        if ctx.name in o:
            raise Redeclared(Variable(), ctx.name)
        o[ctx.name] = ('var', self.visit(ctx.typ, o), ctx.init)

    def visitFuncDecl(self, ctx: FuncDecl, o: object):
        if ctx.name in o:
            raise Redeclared(Function(), ctx.name)
        track = []
        params = [self.visit(param, (track, o)) for param in ctx.params]
        o[ctx.name] = ('function', self.visit(
            ctx.return_type, o), params, ctx.inherit, ctx.body)

    def visitParamDecl(self, ctx: ParamDecl, o):
        track, env = o
        if ctx.name in track:
            raise Redeclared(Parameter(), ctx.name)
        track.append(ctx.name)
        return ('param', self.visit(ctx.typ, o), ctx.name)

    def visitIntegerType(self, ctx, o: object):
        return IntegerType()

    def visitFloatType(self, ctx, o: object):
        return FloatType()

    def visitBooleanType(self, ctx, o: object):
        return BooleanType()

    def visitStringType(self, ctx, o: object):
        return StringType()

    def visitArrayType(self, ctx, o: object):
        return ArrayType()

    def visitAutoType(self, ctx, o: object):
        return AutoType()

    def visitVoidType(self, ctx, o: object):
        return VoidType()


class StaticChecker(Visitor, Utils):
    global_env = {'global': {
        'readInteger': ('function', FType([], IntegerType())),
        'printInteger': ('function', FType(IntegerType(), VoidType())),
        'readFloat': ('function', FType([], FloatType())),
        'writeFloat': ('function', FType(FloatType(), VoidType())),
        'readBoolean': ('function', FType([], BooleanType())),
        'printBoolean': ('function', FType(BooleanType(), VoidType())),
        'readString': ('function', FType([], StringType())),
        'printString': ('function', FType(StringType(), VoidType())),
        'super': ('function', FType(List[Type], Type())),
        'preventDefault': ('function', FType([], VoidType())),
    }
    }

    def __init__(self, ctx):
        self.ctx = ctx

    def check(self):
        return self.visit(self.ctx, StaticChecker.global_env)

    # Program
    def visitProgram(self, ctx: Program, o: object):
        o = GetEnv().visit(ctx, None)
        env = {}
        env['global'] = o
        program = [self.visit(decl, env) for decl in ctx.decls]
        if 'main' not in o:
            raise NoEntryPoint()
        if isinstance(type(o["main"][1]), VoidType) or o["main"][0] != 'function':
            raise NoEntryPoint()
        print(o)
        return program

    # Declare
    def visitVarDecl(self, ctx: VarDecl, o: object):
        env = o
        varType = self.visit(ctx.typ, env)
        if ctx.init is not None:
            init = self.visit(ctx.init, env)
            initType = init[1]
            if (((isinstance(varType, ArrayType) and isinstance(initType, ArrayType)) or (isinstance(varType, FloatType) and isinstance(initType, IntegerType)))):
                varDimentsions = list(map(int, varType.dimensions))
                if varDimentsions != initType.dimensions:
                    raise TypeMismatchInVarDecl(ctx)
            if isinstance(varType, VoidType):
                raise TypeMismatchInVarDecl(ctx)
            if isinstance(varType, AutoType):
                varType = initType
        elif isinstance(varType, AutoType):
            raise Invalid(Variable(), ctx.name)

        if env.get('local') is not None:
            if ctx.name in env['local'][0]:
                raise Redeclared(Variable(), ctx.name)
            env['local'][0][ctx.name] = ('var', varType, None)

    def visitFuncDecl(self, ctx: FuncDecl, o: object):
        env = {}
        env['global'] = o['global']
        env['local'] = [{}]

        for param in ctx.params:
            env['local'][0][param.name] = self.visit(param, env)

        stmts = ctx.body.body
        for stmt in stmts:
            if type(stmt) is VarDecl:
                self.visit(stmt, env)
            elif type(stmt) is not ReturnStmt:
                self.visit(stmt, (False, env))
            else:
                ftype = self.visit(ctx.return_type, o)
                return self.visit(stmt, (ftype, env))

    def visitParamDecl(self, ctx: ParamDecl, o: object):
        # check param type
        return ('param', self.visit(ctx.typ, o), ctx.name, ctx.out, ctx.inherit)

    # Statement
    def visitAssignStmt(self, ctx: AssignStmt, o: object):
        inLoop, env = o
        lhs = self.visit(ctx.lhs, env)
        exp = self.visit(ctx.rhs, env)
        lhsType = lhs[1]
        expType = exp[1]
        if isinstance(lhsType, VoidType):
            raise TypeMismatchInStatement(ctx)

        if isinstance(expType, AutoType):
            param = env['global'][ctx.rhs.name][2]
            inherit = env['global'][ctx.rhs.name][3]
            body = env['global'][ctx.rhs.name][4]
            env['global'][ctx.rhs.name] = (
                'function', lhsType, param, inherit, body)
            expType = lhsType

        if ((isinstance(lhsType, ArrayType) and isinstance(expType, ArrayType)) and (isinstance(lhsType, FloatType) and isinstance(expType, IntegerType))):
            varDimentsions = list(map(int, lhsType.dimensions))
            if varDimentsions != expType.dimensions:
                raise TypeMismatchInVarDecl(ctx)
        if isinstance(lhsType, ArrayType):
            if not ((isinstance(lhsType.typ, type(expType)) or (isinstance(lhsType.typ, FloatType) and isinstance(expType, IntegerType)))):
                raise TypeMismatchInStatement(ctx)
        if not isinstance(lhsType, ArrayType):
            if not (isinstance(lhsType, type(expType)) or (isinstance(lhsType, FloatType) and isinstance(expType, IntegerType))):
                raise TypeMismatchInStatement(ctx)

    def visitBlockStmt(self, ctx, o: object):
        inLoop, temp = o
        env = {}
        env['global'] = temp['global']
        env['local'] = [{}] + temp['local']

        stmts = ctx.body
        for stmt in stmts:
            if type(stmt) is VarDecl:
                self.visit(stmt, env)
            else:
                self.visit(stmt, (inLoop, env))

    def visitIfStmt(self, ctx: IfStmt, o: object):
        inLoop, env = o
        condType = self.visit(ctx.cond, env)
        if type(condType[1]) is not BooleanType:
            raise TypeMismatchInStatement(ctx)
        self.visit(ctx.fstmt, (inLoop, env))
        self.visit(ctx.tstmt, (inLoop, env))

    def visitForStmt(self, ctx: ForStmt, o: object):
        inLoop, env = o

        idType = self.visit(ctx.init.lhs, env)
        initType = self.visit(ctx.init.rhs, env)
        condType = self.visit(ctx.cond, env)
        updType = self.visit(ctx.upd, env)

        if not (isinstance(idType[1], type(initType[1]))):
            raise TypeMismatchInStatement(ctx)
        if not (isinstance(initType[1], IntegerType)):
            raise TypeMismatchInStatement(ctx)
        if not (isinstance(updType[1], IntegerType)):
            raise TypeMismatchInStatement(ctx)
        if not (isinstance(condType[1], BooleanType)):
            raise TypeMismatchInStatement(ctx)

        self.visit(ctx.stmt, (True, env))

    def visitWhileStmt(self, ctx: WhileStmt, o: object):
        inLoop, env = o

        condType = self.visit(ctx.cond, env)
        if False in [type(cond) is BooleanType for cond in [condType[1]]]:
            raise TypeMismatchInStatement(ctx)

        self.visit(ctx.stmt, (True, env))

    def visitDoWhileStmt(self, ctx, o: object):
        inLoop, env = o
        condType = self.visit(ctx.cond, env)
        if False in [type(cond) is BooleanType for cond in [condType[1]]]:
            raise TypeMismatchInStatement(ctx)

        self.visit(ctx.stmt, (True, env))

    def visitBreakStmt(self, ctx, o: object):
        inLoop, env = o
        if not inLoop:
            raise MustInLoop(ctx)

    def visitContinueStmt(self, ctx, o: object):
        inLoop, env = o
        if not inLoop:
            raise MustInLoop(ctx)

    def visitReturnStmt(self, ctx: ReturnStmt, o: object):
        ftype, env = o
        if ctx.expr is None:
            if not isinstance(ftype, VoidType):
                raise TypeMismatchInStatement(ctx)
        else:
            rtype = self.visit(ctx.expr, env)
            if isinstance(ftype, AutoType):
                return
            if not isinstance(ftype, type(rtype[1])) and not (isinstance(ftype, FloatType) and isinstance(rtype[1], IntegerType)):
                raise TypeMismatchInStatement(ctx)

    def visitCallStmt(self, ctx: CallStmt, o: object):
        inLoop, env = o
        if env['global'].get(ctx.name) is not None:
            if len(ctx.args) != len(env['global'][ctx.name][2]):
                raise TypeMismatchInStatement(ctx)
            else:
                params = env['global'][ctx.name][2]
                for i in range(len(params)):
                    typ = self.visit(ctx.args[i], env)
                    if not isinstance(params[i][1], type(typ[1])):
                        raise TypeMismatchInStatement(ctx)
            return
        raise Undeclared(Function(), ctx.name)

    # Expression

    def visitBinExpr(self, ctx: BinExpr, o: object):
        lType = self.visit(ctx.left, o)
        rType = self.visit(ctx.right, o)
        op = ctx.op
        if isinstance(lType[1], VoidType) or isinstance(rType[1], VoidType):
            raise TypeMismatchInExpression(ctx)
        if op in ['+', '-', '*', '/']:
            if not (isinstance(lType[1], FloatType) or isinstance(lType[1], IntegerType)
                    or isinstance(rType[1], FloatType) or isinstance(rType[1], IntegerType)):
                raise TypeMismatchInExpression(ctx)
            if isinstance(lType[1], FloatType) or isinstance(rType[1], FloatType):
                return (None, FloatType(), None)
            print('Hello')
            return (None, IntegerType(), None)
        if op == '%':
            if not (isinstance(lType[1], IntegerType) or isinstance(rType[1], IntegerType)):
                raise TypeMismatchInExpression(ctx)
            return (None, IntegerType(), None)
        if op in ["==", "!="]:
            if isinstance(lType[1], type(rType[1])):
                if isinstance(lType[1], IntegerType) or isinstance(rType[1], BooleanType):
                    return (None, BooleanType(), None)
            raise TypeMismatchInExpression(ctx)
        if op in [">", "<", ">=", "<="]:
            if not (isinstance(lType[1], FloatType) or isinstance(lType[1], IntegerType)
                    or isinstance(rType[1], FloatType) or isinstance(rType[1], IntegerType)):
                raise TypeMismatchInExpression(ctx)
            return (None, BooleanType(), None)
        if op in ["&&", "||"]:
            if isinstance(lType[1], type(rType[1])):
                if type(lType[1]) is BooleanType:
                    return (None, BooleanType(), None)
            raise TypeMismatchInExpression(ctx)
        if op in ["::"]:
            if type(lType[1]) is type(rType[1]):
                if type(lType[1]) is StringType:
                    return (None, StringType(), None)
            raise TypeMismatchInExpression(ctx)

    def visitUnExpr(self, ctx: UnExpr, o: object):
        expType = self.visit(ctx.val, o)
        op = str(ctx.op)
        if (op == '-' and not (isinstance(expType[1], FloatType) or isinstance(expType[1], IntegerType))) or (op == '!' and not isinstance(expType[1], BooleanType)):
            raise TypeMismatchInExpression(ctx)
        return (None, expType[1], None)

    def visitId(self, ctx: Id, o: object):
        if type(o) is tuple:
            inLoop, env = o
        else:
            env = o
        if env.get('local') is not None:
            for local in env['local']:
                if ctx.name in local:
                    return local[ctx.name]
        if env['global'].get(ctx.name) is not None:
            return env['global'][ctx.name]
        else:
            raise Undeclared(Identifier(), ctx.name)

    def visitArrayCell(self, ctx: ArrayCell, o: object):
        arrType = self.visit(Id(ctx.name), o)

        indicesType = list(map(lambda x: self.visit(x, o), ctx.cell))
        if type(arrType[1]) is not ArrayType:
            raise TypeMismatchInExpression(ctx)
        for indiceType in indicesType:
            if type(indiceType[1]) is not IntegerType:
                raise TypeMismatchInExpression(ctx)
        return (None, arrType[1], None)

    def visitIntegerLit(self, ctx: IntegerLit, o: object):
        return (None, IntegerType(), None)

    def visitFloatLit(self, ctx: FloatLit, o: object):
        return (None, FloatType(), None)

    def visitStringLit(self, ctx: StringLit, o: object):
        return (None, StringType(), None)

    def visitBooleanLit(self, ctx: BooleanLit, o: object):
        return (None, BooleanType(), None)

    def visitArrayLit(self, ctx: ArrayLit, o: object):
        def dim(arrayLit):
            if not (isinstance(arrayLit, List)):
                if isinstance(arrayLit, ArrayLit):
                    return dim(arrayLit.explist)
                else:
                    return []
            return [len(arrayLit)] + dim(arrayLit[0])
        dimen = dim(ctx.explist)
        elements = list(map(lambda exp: self.visit(exp, o), ctx.explist))
        arrayType = elements[0][1]
        for element in elements:
            if not isinstance(element[1], type(arrayType)):
                raise IllegalArrayLiteral(ctx)
        return (None,  ArrayType(dimen, arrayType), None)

    def visitFuncCall(self, ctx: FuncCall, o: object):
        if ctx.name in o['global']:
            if len(ctx.args) != len(o['global'][ctx.name][2]):
                raise TypeMismatchInExpression(ctx)
            else:
                params = o['global'][ctx.name][2]
                for i in range(len(params)):
                    typ = self.visit(ctx.args[i], o)
                    if not isinstance(params[i][1], type(typ[1])):
                        raise TypeMismatchInExpression(ctx)
            return o['global'][ctx.name]

        raise Undeclared(Function(), ctx.name)

    # Type

    def visitIntegerType(self, ctx: IntegerType, o: object):
        return IntegerType()

    def visitFloatType(self, ctx: FloatType, o: object):
        return FloatType()

    def visitBooleanType(self, ctx: BooleanType, o: object):
        return BooleanType()

    def visitStringType(self, ctx: StringType, o: object):
        return StringType()

    def visitArrayType(self, ctx: ArrayType, o: object):
        return ctx

    def visitAutoType(self, ctx: AutoType, o: object):
        return AutoType()

    def visitVoidType(self, ctx: VoidType, o: object):
        return VoidType()
