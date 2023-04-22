from Visitor import Visitor
from AST import *
from StaticError import *


class FType:
    # Parameter and return type of a function
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype


class Symbol:
    # Class function but have to use symbol
    def __init__(self, name, ftype, value=None):
        self.name = name
        self.ftype = ftype
        self.value = value


class GetEnv(Visitor):

    def __init__(self):
        self.globalEnv = {}

    def visitProgram(self, ctx: Program, o: object):
        o = self.globalEnv
        o['program'] = {}
        for x in ctx.decls:
            self.visit(x, o['program'])
        print("\n", o)
        return o

    def visitVarDecl(self, ctx: VarDecl, o: object):
        env = o
        name = ctx.name
        if env.get(name) is not None:
            raise Redeclared(Variable(), name)
        env[name] = ('mutable', self.visit(ctx.typ, env))
        # return (self.visit(ctx.varType, env))

    def visitParamDecl(self, ctx: ParamDecl, o: object):
        env = o
        name = ctx.name
        if env.get(name) is not None:
            raise Redeclared(Parameter(), name)
        env[name] = ('param', self.visit(ctx.typ, env))

    # Con sai TH FuncDecl foo; VarDecl a; VarDecl a ma body foo bi loi
    def visitFuncDecl(self, ctx: FuncDecl, o: object):
        if o.get(ctx.name) is not None:
            raise Redeclared(Function(), ctx.name)
        params = ctx.params
        if ctx.return_type is not None:
            param = list(map(lambda x: self.visit(x, {}), params))
            o[ctx.name] = ('function', self.visit(ctx.return_type, o), param)
        else:
            param = list(map(lambda x: self.visit(x, {}), params))
            o[ctx.name] = ('function', None, param)

    def visitIntegerType(self, ast, param):
        return IntegerType()

    def visitFloatType(self, ast, param):
        return FloatType()

    def visitBooleanType(self, ast, param):
        return BooleanType()

    def visitStringType(self, ast, param):
        return StringType()

    def visitVoidType(self, ast, param):
        return VoidType()

    def visitAutoType(self, ast, param):
        return AutoType()

    def visitArrayType(self, ast, param):
        # ast = (dimensions, typ)
        return ast


class ExpUtils:
    @ staticmethod
    def isNaNType(expType):
        return type(expType) not in [IntegerType, FloatType]

    @ staticmethod
    def isNotConst(expType):
        return type(expType) in [ArrayCell, ArrayType]

    @ staticmethod
    def isNotAccess(expType):
        return type(expType) not in [CallStmt]


class StaticChecker(Visitor):

    global_env = [
        Symbol("readInteger", FType([], IntegerType())),
        Symbol("printInteger", FType(IntegerType(), VoidType())),
        Symbol("readFloat", FType([], FloatType())),
        Symbol("writeFloat", FType(FloatType(), VoidType())),
        Symbol("readBoolean", FType([], BooleanType())),
        Symbol("printBoolean", FType(BooleanType(), VoidType())),
        Symbol("readString", FType([], StringType())),
        Symbol("printString", FType(StringType(), VoidType())),
        Symbol("super", FType(List[Type], Type())),
        Symbol("preventDefault", FType([], VoidType()))
    ]

    def __init__(self, ast):
        self.ast = ast

    def check(self):
        return self.visit(self.ast, StaticChecker.global_env)

    # Prototype flag
    i = 0

    def visitProgram(self, ctx: Program, o):
        # Prototype env
        env = GetEnv().visit(ctx, None)

        # Class Program env
        env1 = {}
        env1['current'] = 'program'
        env1['global'] = env
        prog = [self.visit(x, env1) for x in ctx.decls]

        # Check No Entry
        if "main" not in env:
            raise NoEntryPoint()
        if env["main"][0] != 'function' or type(env["main"][1]) is not VoidType:
            raise NoEntryPoint()

        return prog

    def set(self, name, typ, o):
        for tuple in o:
            if name in tuple:
                try:
                    o[-1][name]["return"] = typ
                except:
                    tuple[name] = typ
                return

    def visitVarDecl(self, ctx: VarDecl, o):
        env = o
        name = ctx.name
        typeOfVar = self.visit(ctx.typ, env)

        # Check init assign
        if ctx.init is not None:
            value = self.visit(ctx.init, env)
            typeInit = value[1]
            if value[0] == 'mutable' or value[0] == 'immutable' or value[0] == 'function':
                if ExpUtils.isNotAccess(ctx.init):
                    raise Undeclared(Function(), ctx.init.name)
            if type(typeOfVar) is VoidType:
                raise TypeMismatchInVarDecl(ctx)
            if type(typeOfVar) is ArrayType and type(typeInit) is ArrayType:
                if typeOfVar.size != typeInit.size:
                    raise TypeMismatchInVarDecl(ctx)
                if type(typeOfVar.eleType) is not type(typeInit.eleType):
                    if not (type(typeOfVar.eleType) is FloatType and type(typeInit.eleType) is IntegerType):
                        raise TypeMismatchInVarDecl(ctx)
            if not ((type(typeOfVar) is type(typeInit)) or (type(typeOfVar) is FloatType and type(typeInit) is IntegerType)):
                raise TypeMismatchInVarDecl(ctx)
        elif type(typeOfVar) is AutoType:
            raise Invalid(Variable(), name)

        # None when vardecl in static scope
        if env.get('local') is not None:
            if env['local'][0].get(name) is not None:
                raise Redeclared(Variable(), name)
            env['local'][0][name] = ('var', typeOfVar, None)

    def visitParamDecl(self, ctx: ParamDecl, o):
        kind, env = o
        name = ctx.name
        typeOfVar = self.visit(ctx.typ, env)

        # None when vardecl in static scope
        if env.get('local') is not None:
            if env['local'][0].get(name) is not None:
                raise Redeclared(kind, name)
            env['local'][0][name] = ('param', typeOfVar, None)

    def visitFuncDecl(self, ctx: FuncDecl, o):
        env = {}
        env['global'] = o['global']
        env['local'] = [{}]
        env['current'] = o['current']
        if o.get('parent') is not None:
            env['parent'] = o['parent']  # Inherit
        [self.visit(param, (Parameter(), env))
         for param in ctx.params]

        lines = ctx.body.body
        for line in lines:
            if type(line) is VarDecl:
                self.visit(line, env)
            # line is statement
            if type(line) is not ReturnStmt:
                self.visit(line, (False, env))
            else:
                ftype = self.visit(ctx.return_type, o)
                return self.visit(line, (ftype, env))
                # Gap return la out khoi ham luon

    def visitBlockStmt(self, ctx: BlockStmt, o):
        inLoop, env1 = o
        env = {}
        env['global'] = env1['global']
        env['local'] = [{}]+env1['local']
        env['current'] = env1['current']
        env['parent'] = env1['parent']
        lines = ctx.body
        for line in lines:
            if type(line) is VarDecl:
                self.visit(line, env)
            else:
                self.visit(line, (inLoop, env))

    def visitReturnStmt(self, ctx: ReturnStmt, o):
        ftype, env = o
        rtype = self.visit(ctx.expr, o)
        if rtype[0] == 'mutable' or rtype[0] == 'immutable' or rtype[0] == 'function':
            if ExpUtils.isNotAccess(ctx.expr):
                raise Undeclared(Function(), ctx.expr.name)
        if type(ftype) is not type(rtype[1]):
            if not (type(ftype) is FloatType and type(rtype[1]) is IntegerType):
                raise TypeMismatchInStatement(ctx)

    def visitId(self, ctx, o):
        if type(o) is tuple:
            checkConst, env = o
        else:
            env = o
        if env.get('local') is not None:
            for local in env['local']:
                if ctx.name in local:
                    return local[ctx.name]
        # Check inherit
        if ctx.name in env['global'][env['current']]:
            return env['global'][env['current']][ctx.name]
        if env['parent'] is not None:
            if ctx.name in env['global'][env['parent']]:
                return env['global'][env['parent']][ctx.name]
        raise Undeclared(Identifier(), ctx.name)

    def visitIfStmt(self, ctx: IfStmt, o):
        inLoop, env = o
        condType = self.visit(ctx.cond, env)
        if condType[0] == 'mutable' or condType[0] == 'immutable' or condType[0] == 'function':
            if ExpUtils.isNotAccess(ctx.cond):
                raise Undeclared(Identifier(), ctx.cond.name)
        if type(condType[1]) is not BooleanType:
            raise TypeMismatchInStatement(ctx)
        # check if both stmt return the same type
        self.visit(ctx.tstmt, (inLoop, env))
        self.visit(ctx.fstmt, (inLoop, env))

    def visitAssignStmt(self, ctx, o):
        inLoop, env = o
        lhs = self.visit(ctx.lhs, env)
        exp = self.visit(ctx.rhs, env)

        typeLhs = lhs[1]
        typeExp = exp[1]
        if lhs[0] == 'mutable' or lhs[0] == 'immutable' or lhs[0] == 'function':
            if ExpUtils.isNotAccess(ctx.lhs):
                raise Undeclared(Identifier(), ctx.lhs.name)
        if exp[0] == 'mutable' or exp[0] == 'immutable' or exp[0] == 'function':
            if ExpUtils.isNotAccess(ctx.rhs):
                raise Undeclared(Identifier(), ctx.exp.name)
        if type(typeLhs) is VoidType:
            raise TypeMismatchInStatement(ctx)
        if type(typeLhs) is ArrayType and type(typeExp) is ArrayType:
            if typeLhs.size != typeExp.size:
                raise TypeMismatchInStatement(ctx)
            if type(typeLhs.eleType) is not type(typeExp.eleType):
                if not (type(typeLhs.eleType) is FloatType and type(typeExp.eleType) is IntegerType):
                    raise TypeMismatchInStatement(ctx)
        if not ((type(typeLhs) is type(typeExp)) or (type(typeLhs) is FloatType and type(typeExp) is IntegerType)):
            raise TypeMismatchInStatement(ctx)

    def visitForStmt(self, ctx: ForStmt, o):
        inLoop, env = o

        idType = self.visit(ctx.init.lhs, env)

        # Check Type Expression
        initType = self.visit(ctx.init.rhs, env)
        condType = self.visit(ctx.cond, env)
        updType = self.visit(ctx.upd, env)

        if idType[0] == 'mutable' or idType[0] == 'immutable' or idType[0] == 'function':
            if ExpUtils.isNotAccess(ctx.init.lhs):
                raise Undeclared(Identifier(), ctx.init.lhs.name)
        if initType[0] == 'mutable' or initType[0] == 'immutable' or initType[0] == 'function':
            if ExpUtils.isNotAccess(ctx.init.rhs):
                raise Undeclared(Identifier(), ctx.init.rhs.name)
        if condType[0] == 'mutable' or condType[0] == 'immutable' or condType[0] == 'function':
            if ExpUtils.isNotAccess(ctx.cond):
                raise Undeclared(Identifier(), ctx.cond.name)
        if False in [type(x) is IntegerType for x in [initType[1], idType[1]]]:
            raise TypeMismatchInStatement(ctx)
        if ExpUtils.isNaNType(idType[1]):
            raise TypeMismatchInStatement(ctx)
        if False in [type(x) is BooleanType for x in [condType[1]]]:
            raise TypeMismatchInStatement(ctx)

        # Visit statements
        self.visit(ctx.stmt, (True, env))

    def visitContinueStmt(self, ctx, o):
        inLoop, env = o
        if not inLoop:
            raise MustInLoop(ctx)

    def visitBreakStmt(self, ctx, o):
        inLoop, env = o
        if not inLoop:
            raise MustInLoop(ctx)

    def visitDoWhileStmt(self, ctx: DoWhileStmt, o):
        inLoop, env = o

        # Check Type Expression
        condType = self.visit(ctx.cond, env)

        if condType[0] == 'mutable' or condType[0] == 'immutable' or condType[0] == 'function':
            if ExpUtils.isNotAccess(ctx.cond):
                raise Undeclared(Identifier(), ctx.cond.name)
        if False in [type(x) is BooleanType for x in [condType[1]]]:
            raise TypeMismatchInStatement(ctx)

        # Visit statements
        self.visit(ctx.stmt, (True, env))

    def visitWhileStmt(self, ctx: WhileStmt, o):
        inLoop, env = o

        # Check Type Expression
        condType = self.visit(ctx.cond, env)

        if condType[0] == 'mutable' or condType[0] == 'immutable' or condType[0] == 'function':
            if ExpUtils.isNotAccess(ctx.cond):
                raise Undeclared(Identifier(), ctx.cond.name)
        if False in [type(x) is BooleanType for x in [condType[1]]]:
            raise TypeMismatchInStatement(ctx)

        # Visit statements
        self.visit(ctx.stmt, (True, env))

    def visitCallStmt(self, ctx, o):
        inLoop, env = o
        if type(ctx.obj) is SelfLiteral:
            method = self.handleAccess(
                ctx.method, (Method(), o, env['current']))
            if method[2] == 'static':
                raise IllegalMemberAccess(ctx)
            paramCall = list(map(lambda x: self.visit(x, env), ctx.param))
        else:
            try:
                nameClass = self.visit(ctx.obj,  env)
            except:
                if ctx.obj.name in env['global']:
                    nameClass = ctx.obj.name
                else:
                    raise Undeclared(Class(), ctx.obj.name)
            if type(nameClass) is tuple:
                if type(nameClass[1]) is not ClassType:
                    raise TypeMismatchInStatement(ctx)
                method = self.handleAccess(
                    ctx.method, (Method(), env, nameClass[1].classname.name))
                if method[2] == 'static':
                    raise IllegalMemberAccess(ctx)
                if type(method[1]) is not VoidType:
                    raise TypeMismatchInStatement(ctx)
                if method[0] != 'method':
                    raise TypeMismatchInStatement(ctx)
            if type(nameClass) is str:
                method = self.handleAccess(
                    ctx.method, (Method(), env, nameClass))
                if method[2] == 'instance':
                    raise IllegalMemberAccess(ctx)
                if type(method[1]) is not VoidType:
                    raise TypeMismatchInStatement(ctx)
                if method[0] != 'method':
                    raise TypeMismatchInStatement(ctx)
            paramCall = list(map(lambda x: self.visit(x, env), ctx.param))
            if len(paramCall) != len(method[3]):
                raise TypeMismatchInStatement(ctx)
            for i in range(len(paramCall)):
                if type(paramCall[i][1]) is not type(method[3][i][1]):
                    if not (type(method[3][i][1]) is FloatType and type(paramCall[i][1]) is IntType):
                        raise TypeMismatchInStatement(ctx)

    def visitCallStmt(self, ctx: CallStmt, o):
        # function name always in the last ele of o
        if ctx.name in o[-1]:
            param_lst = o[-1][ctx.name]["param"]
            # o[0][ctx.name] is a list
            if len(param_lst) != len(ctx.args):
                raise TypeMismatchInStatement(ctx)
            else:
                # Check types in the args case-by-case
                for i in range(len(param_lst)):
                    typ = self.visit(ctx.args[i], o)
                    # Infer type for parameter
                    if param_lst[i] == 5 and typ != 5:
                        o[0][ctx.name][i] = typ
                    elif param_lst[i] != 5 and typ == 5:
                        self.set(ctx.args[i].name, param_lst[i], o)
                    elif param_lst[i] == 5 and typ == 5:
                        # Won't happen
                        raise TypeCannotBeInferred(ctx)
                    elif param_lst[i] != typ:
                        # Can use int for input for float but not reverse
                        if param_lst[i] == 2 and typ == 1:
                            continue
                        raise TypeMismatchInStatement(ctx)
                if o[-1][ctx.name]["return"] == 5:
                    o[-1][ctx.name]["return"] = 6  # If auto + stmcall => void
        else:
            raise Undeclared(Function(), ctx.name)

    def visitFuncCall(self, ctx: FuncCall, o):
        # function name always in the last ele of o
        if ctx.name in o[-1]:
            param_lst = o[-1][ctx.name]["param"]
            # o[0][ctx.name] is a list
            if len(param_lst) != len(ctx.args):
                raise TypeMismatchInStatement(ctx)
            else:
                # Check types in the args case-by-case
                for i in range(len(param_lst)):
                    typ = self.visit(ctx.args[i], o)
                    # Infer type for parameter
                    if (param_lst[i] == 0 or param_lst[i] == 5) and typ != 0:
                        o[0][ctx.name]['param'][i] = typ
                    elif param_lst[i] != 0 and typ == 0:
                        self.set(ctx.args[i].name, param_lst[i], o)
                    elif param_lst[i] == 0 and typ == 0:
                        # Won't happen
                        raise TypeCannotBeInferred(ctx)
                    elif param_lst[i] != typ:
                        # Can use int for input for float but not reverse
                        if param_lst[i] == 2 and typ == 1:
                            continue
                        raise TypeMismatchInStatement(ctx)

                return o[-1][ctx.name]["return"]
        else:
            if self.i:
                raise Undeclared(Function(), ctx.name)

    def visitIntegerLit(self, ctx: IntegerLit, o):
        return (None, IntegerType(), None)

    def visitFloatLit(self, ctx: FloatLit, o):
        return (None, FloatType(), None)

    def visitBooleanLit(self, ctx: BooleanLit, o):
        return (None, BooleanType(), None)

    def visitStringLit(self, ctx: StringLit, o):
        return (None, StringType(), None)

    def visitArrayLit(self, ctx: ArrayLit, o):
        temp = list(map(lambda x: self.visit(x, o), ctx.explist))
        default = temp[0][1]
        for typeOfElement in temp:
            if type(typeOfElement[1]) is not type(default):
                raise IllegalArrayLiteral(ctx)
        return (None,  ArrayType(len(temp), default), None)

    def visitArrayCell(self, ctx: ArrayCell, o):
        arrType = self.visit(ctx.name, o)
        indicesType = list(map(lambda x: self.visit(x, o), ctx.cell))
        if type(arrType[1]) is not ArrayType:
            raise TypeMismatchInExpression(ctx)
        for indiceType in indicesType:
            if type(indiceType[1]) is not IntegerType:
                raise TypeMismatchInExpression(ctx)
        return (None, arrType[1], None)

    def visitArrayType(self, ctx: ArrayType, o):
        return ctx

    def visitBinExpr(self, ctx: BinExpr, o):
        if type(o) is tuple:
            if ExpUtils.isNotConst(ctx.left):
                raise IllegalConstantExpression(ctx)
            if ExpUtils.isNotConst(ctx.right):
                raise IllegalConstantExpression(ctx)
            # left, right is arraytype/lit
            lType = self.visit(ctx.left, o)
            rType = self.visit(ctx.right, o)
            if lType[0] == 'var' or lType[0] == 'mutable':
                raise IllegalConstantExpression(ctx)
            if rType[0] == 'var' or rType[0] == 'mutable':
                raise IllegalConstantExpression(ctx)
        else:
            lType = self.visit(ctx.left, o)
            rType = self.visit(ctx.right, o)
        if lType[0] == 'mutable' or lType[0] == 'immutable' or lType[0] == 'function':
            if ExpUtils.isNotAccess(ctx.left):
                raise Undeclared(Identifier(), ctx.left.name)
        if rType[0] == 'mutable' or rType[0] == 'immutable' or rType[0] == 'function':
            if ExpUtils.isNotAccess(ctx.right):
                raise Undeclared(Identifier(), ctx.right.name)
        op = ctx.op

        # Check Operator
        if type(lType[1]) is VoidType or type(rType[1]) is VoidType:
            raise TypeMismatchInExpression(ctx)
        if op in ["+", "-", "*", "/"]:
            if ExpUtils.isNaNType(lType[1]) or ExpUtils.isNaNType(rType[1]):
                raise TypeMismatchInExpression(ctx)
            if type(lType[1]) is FloatType or type(rType[1]) is FloatType:
                return (None, FloatType(), None)
            return (None, IntegerType(), None)
        if op in ["%"]:
            if not (type(lType[1]) is IntegerType) or not (type(rType[1]) is IntegerType):
                raise TypeMismatchInExpression(ctx)
            return (None, IntegerType(), None)
        if op in ["==", "!="]:
            if type(lType[1]) is type(rType[1]):
                if (type(lType[1]) is IntegerType) or (type(rType[1]) is BooleanType):
                    return (None, BooleanType(), None)
            raise TypeMismatchInExpression(ctx)
        if op in [">", "<", ">=", "<="]:
            if ExpUtils.isNaNType(lType[1]) or ExpUtils.isNaNType(rType[1]):
                raise TypeMismatchInExpression(ctx)
            return (None, BooleanType(), None)
        if op in ["&&", "||"]:
            if type(lType[1]) is type(rType[1]):
                if type(lType[1]) is BooleanType:
                    return (None, BooleanType(), None)
            raise TypeMismatchInExpression(ctx)
        if op in ["::"]:
            if type(lType[1]) is type(rType[1]):
                if type(lType[1]) is StringType:
                    return (None, StringType(), None)
            raise TypeMismatchInExpression(ctx)

    def visitUnExpr(self, ctx: UnExpr, o):
        if type(o) is tuple:
            if ExpUtils.isNotConst(ctx.body):
                raise IllegalConstantExpression(ctx.body)
            expType = self.visit(ctx.body, o)
            if expType[0] == 'var' or expType[0] == "mutable":
                raise IllegalConstantExpression(ctx.body)
        else:
            expType = self.visit(ctx.body, o)

        if expType[0] == 'mutable' or expType[0] == 'immutable' or expType[0] == 'function':
            if ExpUtils.isNotAccess(ctx.body):
                raise Undeclared(Identifier(), ctx.body.name)
        op = str(ctx.op)

        # Check Operator
        if (op == '-' and ExpUtils.isNaNType(expType[1])) or (op == '!' and type(expType[1]) is not BooleanType):
            raise TypeMismatchInExpression(ctx)
        return (None, expType[1], None)

    def visitIntegerType(self, ctx: IntegerType, o):
        return IntegerType()

    def visitFloatType(self, ctx: FloatType, o):
        return FloatType()

    def visitBooleanType(self, ctx: BooleanType, o):
        return BooleanType()

    def visitStringType(self, ctx: StringType, o):
        return StringType()

    def visitAutoType(self, ctx: AutoType, o):
        return AutoType()

    def visitVoidType(self, ctx: VoidType, o):
        return VoidType()

    def visitFieldAccess(self, ctx, o):
        if type(o) is tuple:
            checkConst, env = o
        else:
            env = o
        if type(ctx.obj) is SelfLiteral:
            fieldname = self.handleAccess(
                ctx.fieldname, (Attribute(), env, env['current']))
            if fieldname[2] == 'static':
                raise IllegalMemberAccess(ctx)
        else:
            try:
                nameClass = self.visit(ctx.obj,  env)
            except:
                if ctx.obj.name in env['global']:
                    nameClass = ctx.obj.name
                else:
                    raise Undeclared(Class(), ctx.obj.name)
            if type(nameClass) is tuple:
                if type(nameClass[1]) is not ClassType:
                    raise TypeMismatchInExpression(ctx)
                fieldname = self.handleAccess(
                    ctx.fieldname, (Attribute(), env, nameClass[1].classname.name))
                if fieldname[2] == 'static':
                    raise IllegalMemberAccess(ctx)
                if fieldname[0] == 'method':
                    raise TypeMismatchInExpression(ctx)
            if type(nameClass) is str:
                fieldname = self.handleAccess(
                    ctx.fieldname, (Attribute(), env, nameClass))

                if fieldname[2] == 'instance':
                    raise IllegalMemberAccess(ctx)
                if fieldname[0] == 'method':
                    raise TypeMismatchInExpression(ctx)
        return (fieldname[0], fieldname[1], None)
