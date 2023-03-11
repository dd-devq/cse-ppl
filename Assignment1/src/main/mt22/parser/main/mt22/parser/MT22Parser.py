# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,59,212,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,1,0,1,0,1,0,1,1,1,1,3,1,64,8,1,1,2,1,2,1,2,1,
        2,1,2,3,2,71,8,2,1,2,1,2,1,2,1,3,1,3,1,4,1,4,1,4,5,4,81,8,4,10,4,
        12,4,84,9,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,93,8,5,1,6,1,6,1,6,1,
        6,1,7,1,7,1,7,1,7,5,7,103,8,7,10,7,12,7,106,9,7,1,8,1,8,1,8,1,8,
        3,8,112,8,8,1,9,1,9,1,9,1,9,5,9,118,8,9,10,9,12,9,121,9,9,1,10,1,
        10,1,10,1,10,5,10,127,8,10,10,10,12,10,130,9,10,1,11,1,11,1,11,1,
        11,5,11,136,8,11,10,11,12,11,139,9,11,1,12,3,12,142,8,12,1,12,1,
        12,1,13,3,13,147,8,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,5,14,156,
        8,14,10,14,12,14,159,9,14,1,15,1,15,1,15,1,15,1,15,3,15,166,8,15,
        1,16,1,16,1,17,1,17,1,18,1,18,1,19,1,19,1,20,1,20,1,21,1,21,1,22,
        1,22,1,23,1,23,1,24,1,24,1,24,1,24,1,24,1,24,3,24,190,8,24,1,25,
        1,25,1,25,1,25,1,25,1,25,1,25,1,26,1,26,1,26,1,27,1,27,1,27,1,27,
        3,27,206,8,27,1,28,1,28,1,28,1,28,1,28,0,0,29,0,2,4,6,8,10,12,14,
        16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,0,
        4,2,0,31,31,33,33,2,0,32,32,34,35,1,0,22,27,1,0,28,29,206,0,58,1,
        0,0,0,2,63,1,0,0,0,4,65,1,0,0,0,6,75,1,0,0,0,8,77,1,0,0,0,10,92,
        1,0,0,0,12,94,1,0,0,0,14,98,1,0,0,0,16,107,1,0,0,0,18,113,1,0,0,
        0,20,122,1,0,0,0,22,131,1,0,0,0,24,141,1,0,0,0,26,146,1,0,0,0,28,
        150,1,0,0,0,30,165,1,0,0,0,32,167,1,0,0,0,34,169,1,0,0,0,36,171,
        1,0,0,0,38,173,1,0,0,0,40,175,1,0,0,0,42,177,1,0,0,0,44,179,1,0,
        0,0,46,181,1,0,0,0,48,189,1,0,0,0,50,191,1,0,0,0,52,198,1,0,0,0,
        54,205,1,0,0,0,56,207,1,0,0,0,58,59,3,2,1,0,59,60,5,0,0,1,60,1,1,
        0,0,0,61,64,3,4,2,0,62,64,3,6,3,0,63,61,1,0,0,0,63,62,1,0,0,0,64,
        3,1,0,0,0,65,66,3,8,4,0,66,67,5,47,0,0,67,70,3,10,5,0,68,69,5,36,
        0,0,69,71,3,12,6,0,70,68,1,0,0,0,70,71,1,0,0,0,71,72,1,0,0,0,72,
        73,5,45,0,0,73,74,6,2,-1,0,74,5,1,0,0,0,75,76,1,0,0,0,76,7,1,0,0,
        0,77,82,5,53,0,0,78,79,5,44,0,0,79,81,5,53,0,0,80,78,1,0,0,0,81,
        84,1,0,0,0,82,80,1,0,0,0,82,83,1,0,0,0,83,9,1,0,0,0,84,82,1,0,0,
        0,85,93,5,18,0,0,86,93,5,17,0,0,87,93,5,19,0,0,88,93,5,15,0,0,89,
        93,5,16,0,0,90,93,5,6,0,0,91,93,3,50,25,0,92,85,1,0,0,0,92,86,1,
        0,0,0,92,87,1,0,0,0,92,88,1,0,0,0,92,89,1,0,0,0,92,90,1,0,0,0,92,
        91,1,0,0,0,93,11,1,0,0,0,94,95,3,14,7,0,95,96,5,44,0,0,96,97,3,14,
        7,0,97,13,1,0,0,0,98,104,3,16,8,0,99,100,3,40,20,0,100,101,3,16,
        8,0,101,103,1,0,0,0,102,99,1,0,0,0,103,106,1,0,0,0,104,102,1,0,0,
        0,104,105,1,0,0,0,105,15,1,0,0,0,106,104,1,0,0,0,107,111,3,18,9,
        0,108,109,3,38,19,0,109,110,3,18,9,0,110,112,1,0,0,0,111,108,1,0,
        0,0,111,112,1,0,0,0,112,17,1,0,0,0,113,119,3,20,10,0,114,115,3,44,
        22,0,115,116,3,20,10,0,116,118,1,0,0,0,117,114,1,0,0,0,118,121,1,
        0,0,0,119,117,1,0,0,0,119,120,1,0,0,0,120,19,1,0,0,0,121,119,1,0,
        0,0,122,128,3,22,11,0,123,124,3,32,16,0,124,125,3,22,11,0,125,127,
        1,0,0,0,126,123,1,0,0,0,127,130,1,0,0,0,128,126,1,0,0,0,128,129,
        1,0,0,0,129,21,1,0,0,0,130,128,1,0,0,0,131,137,3,24,12,0,132,133,
        3,34,17,0,133,134,3,24,12,0,134,136,1,0,0,0,135,132,1,0,0,0,136,
        139,1,0,0,0,137,135,1,0,0,0,137,138,1,0,0,0,138,23,1,0,0,0,139,137,
        1,0,0,0,140,142,3,42,21,0,141,140,1,0,0,0,141,142,1,0,0,0,142,143,
        1,0,0,0,143,144,3,26,13,0,144,25,1,0,0,0,145,147,3,46,23,0,146,145,
        1,0,0,0,146,147,1,0,0,0,147,148,1,0,0,0,148,149,3,28,14,0,149,27,
        1,0,0,0,150,157,3,30,15,0,151,152,5,42,0,0,152,153,3,52,26,0,153,
        154,5,43,0,0,154,156,1,0,0,0,155,151,1,0,0,0,156,159,1,0,0,0,157,
        155,1,0,0,0,157,158,1,0,0,0,158,29,1,0,0,0,159,157,1,0,0,0,160,166,
        3,48,24,0,161,162,5,40,0,0,162,163,3,14,7,0,163,164,5,41,0,0,164,
        166,1,0,0,0,165,160,1,0,0,0,165,161,1,0,0,0,166,31,1,0,0,0,167,168,
        7,0,0,0,168,33,1,0,0,0,169,170,7,1,0,0,170,35,1,0,0,0,171,172,1,
        0,0,0,172,37,1,0,0,0,173,174,7,2,0,0,174,39,1,0,0,0,175,176,5,37,
        0,0,176,41,1,0,0,0,177,178,5,30,0,0,178,43,1,0,0,0,179,180,7,3,0,
        0,180,45,1,0,0,0,181,182,5,33,0,0,182,47,1,0,0,0,183,190,5,49,0,
        0,184,190,5,50,0,0,185,190,5,52,0,0,186,190,5,51,0,0,187,190,5,53,
        0,0,188,190,3,56,28,0,189,183,1,0,0,0,189,184,1,0,0,0,189,185,1,
        0,0,0,189,186,1,0,0,0,189,187,1,0,0,0,189,188,1,0,0,0,190,49,1,0,
        0,0,191,192,5,14,0,0,192,193,5,42,0,0,193,194,3,52,26,0,194,195,
        5,43,0,0,195,196,5,12,0,0,196,197,3,10,5,0,197,51,1,0,0,0,198,199,
        5,49,0,0,199,200,3,54,27,0,200,53,1,0,0,0,201,202,5,44,0,0,202,203,
        5,49,0,0,203,206,3,54,27,0,204,206,1,0,0,0,205,201,1,0,0,0,205,204,
        1,0,0,0,206,55,1,0,0,0,207,208,5,40,0,0,208,209,3,12,6,0,209,210,
        5,41,0,0,210,57,1,0,0,0,15,63,70,82,92,104,111,119,128,137,141,146,
        157,165,189,205
    ]

class MT22Parser ( Parser ):

    grammarFileName = "MT22.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'do'", "'function'", "'if'", "'else'", 
                     "'continue'", "'auto'", "'break'", "'for'", "'return'", 
                     "'while'", "'out'", "'of'", "'inherit'", "'array'", 
                     "'void'", "'boolean'", "'float'", "'integer'", "'string'", 
                     "'true'", "'false'", "'=='", "'!='", "'>'", "'<'", 
                     "'>='", "'<='", "'&&'", "'||'", "'!'", "'+'", "'/'", 
                     "'-'", "'*'", "'%'", "'='", "'::'", "'('", "')'", "'{'", 
                     "'}'", "'['", "']'", "','", "';'", "'.'", "':'", "'_'" ]

    symbolicNames = [ "<INVALID>", "DO", "FUNCTION", "IF", "ELSE", "CONTINUE", 
                      "AUTO", "BREAK", "FOR", "RETURN", "WHILE", "OUT", 
                      "OF", "INHERIT", "ARRAY", "VOID", "BOOLEAN", "FLOAT", 
                      "INTEGER", "STRING", "TRUE", "FALSE", "EQUAL", "NOTEQUAL", 
                      "GT", "LT", "GET", "LET", "AND", "OR", "NOT", "ADD", 
                      "DIV", "SUB", "MUL", "MOD", "ASSING", "CONCATE", "LB", 
                      "RB", "LCB", "RCB", "LSB", "RSB", "COMA", "SEMI", 
                      "DOT", "COLON", "UNDERSCORE", "INTL", "FLOATL", "BOOLL", 
                      "STRINGL", "ID", "WS", "LINECMT", "BLOCKCMT", "ERROR_CHAR", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_decl = 1
    RULE_vardecl = 2
    RULE_funcdecl = 3
    RULE_idlst = 4
    RULE_primitivetype = 5
    RULE_exprlst = 6
    RULE_expr = 7
    RULE_expr1 = 8
    RULE_expr2 = 9
    RULE_expr3 = 10
    RULE_expr4 = 11
    RULE_expr5 = 12
    RULE_expr6 = 13
    RULE_expr7_index = 14
    RULE_expr8 = 15
    RULE_adding = 16
    RULE_multiplying = 17
    RULE_unary = 18
    RULE_relational = 19
    RULE_strconcate = 20
    RULE_unarylogical = 21
    RULE_binarylogical = 22
    RULE_sign = 23
    RULE_operands = 24
    RULE_arrayType = 25
    RULE_dimensions = 26
    RULE_dimension = 27
    RULE_arrayl = 28

    ruleNames =  [ "program", "decl", "vardecl", "funcdecl", "idlst", "primitivetype", 
                   "exprlst", "expr", "expr1", "expr2", "expr3", "expr4", 
                   "expr5", "expr6", "expr7_index", "expr8", "adding", "multiplying", 
                   "unary", "relational", "strconcate", "unarylogical", 
                   "binarylogical", "sign", "operands", "arrayType", "dimensions", 
                   "dimension", "arrayl" ]

    EOF = Token.EOF
    DO=1
    FUNCTION=2
    IF=3
    ELSE=4
    CONTINUE=5
    AUTO=6
    BREAK=7
    FOR=8
    RETURN=9
    WHILE=10
    OUT=11
    OF=12
    INHERIT=13
    ARRAY=14
    VOID=15
    BOOLEAN=16
    FLOAT=17
    INTEGER=18
    STRING=19
    TRUE=20
    FALSE=21
    EQUAL=22
    NOTEQUAL=23
    GT=24
    LT=25
    GET=26
    LET=27
    AND=28
    OR=29
    NOT=30
    ADD=31
    DIV=32
    SUB=33
    MUL=34
    MOD=35
    ASSING=36
    CONCATE=37
    LB=38
    RB=39
    LCB=40
    RCB=41
    LSB=42
    RSB=43
    COMA=44
    SEMI=45
    DOT=46
    COLON=47
    UNDERSCORE=48
    INTL=49
    FLOATL=50
    BOOLL=51
    STRINGL=52
    ID=53
    WS=54
    LINECMT=55
    BLOCKCMT=56
    ERROR_CHAR=57
    UNCLOSE_STRING=58
    ILLEGAL_ESCAPE=59

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(MT22Parser.DeclContext,0)


        def EOF(self):
            return self.getToken(MT22Parser.EOF, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MT22Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.decl()
            self.state = 59
            self.match(MT22Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(MT22Parser.VardeclContext,0)


        def funcdecl(self):
            return self.getTypedRuleContext(MT22Parser.FuncdeclContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = MT22Parser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl)
        try:
            self.state = 63
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [53]:
                self.enterOuterAlt(localctx, 1)
                self.state = 61
                self.vardecl()
                pass
            elif token in [-1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 62
                self.funcdecl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idlst(self):
            return self.getTypedRuleContext(MT22Parser.IdlstContext,0)


        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def primitivetype(self):
            return self.getTypedRuleContext(MT22Parser.PrimitivetypeContext,0)


        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def ASSING(self):
            return self.getToken(MT22Parser.ASSING, 0)

        def exprlst(self):
            return self.getTypedRuleContext(MT22Parser.ExprlstContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = MT22Parser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_vardecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.idlst()
            self.state = 66
            self.match(MT22Parser.COLON)
            self.state = 67
            self.primitivetype()
            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 68
                self.match(MT22Parser.ASSING)
                self.state = 69
                self.exprlst()


            self.state = 72
            self.match(MT22Parser.SEMI)
             
            if exprlst is not None and len(idlst) != len(exprlst):
                raise RuntimeError("Number of identifiers does not match number of expressions")

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MT22Parser.RULE_funcdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




    def funcdecl(self):

        localctx = MT22Parser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_funcdecl)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdlstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.ID)
            else:
                return self.getToken(MT22Parser.ID, i)

        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMA)
            else:
                return self.getToken(MT22Parser.COMA, i)

        def getRuleIndex(self):
            return MT22Parser.RULE_idlst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdlst" ):
                return visitor.visitIdlst(self)
            else:
                return visitor.visitChildren(self)




    def idlst(self):

        localctx = MT22Parser.IdlstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_idlst)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(MT22Parser.ID)
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==44:
                self.state = 78
                self.match(MT22Parser.COMA)
                self.state = 79
                self.match(MT22Parser.ID)
                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimitivetypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(MT22Parser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(MT22Parser.FLOAT, 0)

        def STRING(self):
            return self.getToken(MT22Parser.STRING, 0)

        def VOID(self):
            return self.getToken(MT22Parser.VOID, 0)

        def BOOLEAN(self):
            return self.getToken(MT22Parser.BOOLEAN, 0)

        def AUTO(self):
            return self.getToken(MT22Parser.AUTO, 0)

        def arrayType(self):
            return self.getTypedRuleContext(MT22Parser.ArrayTypeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_primitivetype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitivetype" ):
                return visitor.visitPrimitivetype(self)
            else:
                return visitor.visitChildren(self)




    def primitivetype(self):

        localctx = MT22Parser.PrimitivetypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_primitivetype)
        try:
            self.state = 92
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 85
                self.match(MT22Parser.INTEGER)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 86
                self.match(MT22Parser.FLOAT)
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 3)
                self.state = 87
                self.match(MT22Parser.STRING)
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 4)
                self.state = 88
                self.match(MT22Parser.VOID)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 5)
                self.state = 89
                self.match(MT22Parser.BOOLEAN)
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 6)
                self.state = 90
                self.match(MT22Parser.AUTO)
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 7)
                self.state = 91
                self.arrayType()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprlstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.ExprContext)
            else:
                return self.getTypedRuleContext(MT22Parser.ExprContext,i)


        def COMA(self):
            return self.getToken(MT22Parser.COMA, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_exprlst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprlst" ):
                return visitor.visitExprlst(self)
            else:
                return visitor.visitChildren(self)




    def exprlst(self):

        localctx = MT22Parser.ExprlstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_exprlst)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.expr()

            self.state = 95
            self.match(MT22Parser.COMA)
            self.state = 96
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Expr1Context)
            else:
                return self.getTypedRuleContext(MT22Parser.Expr1Context,i)


        def strconcate(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.StrconcateContext)
            else:
                return self.getTypedRuleContext(MT22Parser.StrconcateContext,i)


        def getRuleIndex(self):
            return MT22Parser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = MT22Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.expr1()
            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==37:
                self.state = 99
                self.strconcate()
                self.state = 100
                self.expr1()
                self.state = 106
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Expr2Context)
            else:
                return self.getTypedRuleContext(MT22Parser.Expr2Context,i)


        def relational(self):
            return self.getTypedRuleContext(MT22Parser.RelationalContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)




    def expr1(self):

        localctx = MT22Parser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_expr1)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.expr2()
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 264241152) != 0:
                self.state = 108
                self.relational()
                self.state = 109
                self.expr2()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Expr3Context)
            else:
                return self.getTypedRuleContext(MT22Parser.Expr3Context,i)


        def binarylogical(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.BinarylogicalContext)
            else:
                return self.getTypedRuleContext(MT22Parser.BinarylogicalContext,i)


        def getRuleIndex(self):
            return MT22Parser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)




    def expr2(self):

        localctx = MT22Parser.Expr2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_expr2)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.expr3()
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==28 or _la==29:
                self.state = 114
                self.binarylogical()
                self.state = 115
                self.expr3()
                self.state = 121
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Expr4Context)
            else:
                return self.getTypedRuleContext(MT22Parser.Expr4Context,i)


        def adding(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.AddingContext)
            else:
                return self.getTypedRuleContext(MT22Parser.AddingContext,i)


        def getRuleIndex(self):
            return MT22Parser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)




    def expr3(self):

        localctx = MT22Parser.Expr3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_expr3)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.expr4()
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31 or _la==33:
                self.state = 123
                self.adding()
                self.state = 124
                self.expr4()
                self.state = 130
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Expr5Context)
            else:
                return self.getTypedRuleContext(MT22Parser.Expr5Context,i)


        def multiplying(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.MultiplyingContext)
            else:
                return self.getTypedRuleContext(MT22Parser.MultiplyingContext,i)


        def getRuleIndex(self):
            return MT22Parser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)




    def expr4(self):

        localctx = MT22Parser.Expr4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_expr4)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.expr5()
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 55834574848) != 0:
                self.state = 132
                self.multiplying()
                self.state = 133
                self.expr5()
                self.state = 139
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr6(self):
            return self.getTypedRuleContext(MT22Parser.Expr6Context,0)


        def unarylogical(self):
            return self.getTypedRuleContext(MT22Parser.UnarylogicalContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = MT22Parser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_expr5)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 140
                self.unarylogical()


            self.state = 143
            self.expr6()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr7_index(self):
            return self.getTypedRuleContext(MT22Parser.Expr7_indexContext,0)


        def sign(self):
            return self.getTypedRuleContext(MT22Parser.SignContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)




    def expr6(self):

        localctx = MT22Parser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_expr6)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 145
                self.sign()


            self.state = 148
            self.expr7_index()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr7_indexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr8(self):
            return self.getTypedRuleContext(MT22Parser.Expr8Context,0)


        def LSB(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.LSB)
            else:
                return self.getToken(MT22Parser.LSB, i)

        def dimensions(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.DimensionsContext)
            else:
                return self.getTypedRuleContext(MT22Parser.DimensionsContext,i)


        def RSB(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.RSB)
            else:
                return self.getToken(MT22Parser.RSB, i)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr7_index

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7_index" ):
                return visitor.visitExpr7_index(self)
            else:
                return visitor.visitChildren(self)




    def expr7_index(self):

        localctx = MT22Parser.Expr7_indexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_expr7_index)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.expr8()
            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==42:
                self.state = 151
                self.match(MT22Parser.LSB)
                self.state = 152
                self.dimensions()
                self.state = 153
                self.match(MT22Parser.RSB)
                self.state = 159
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operands(self):
            return self.getTypedRuleContext(MT22Parser.OperandsContext,0)


        def LCB(self):
            return self.getToken(MT22Parser.LCB, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def RCB(self):
            return self.getToken(MT22Parser.RCB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr8" ):
                return visitor.visitExpr8(self)
            else:
                return visitor.visitChildren(self)




    def expr8(self):

        localctx = MT22Parser.Expr8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expr8)
        try:
            self.state = 165
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self.operands()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 161
                self.match(MT22Parser.LCB)
                self.state = 162
                self.expr()
                self.state = 163
                self.match(MT22Parser.RCB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB(self):
            return self.getToken(MT22Parser.SUB, 0)

        def ADD(self):
            return self.getToken(MT22Parser.ADD, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_adding

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdding" ):
                return visitor.visitAdding(self)
            else:
                return visitor.visitChildren(self)




    def adding(self):

        localctx = MT22Parser.AddingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_adding)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            _la = self._input.LA(1)
            if not(_la==31 or _la==33):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplyingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIV(self):
            return self.getToken(MT22Parser.DIV, 0)

        def MUL(self):
            return self.getToken(MT22Parser.MUL, 0)

        def MOD(self):
            return self.getToken(MT22Parser.MOD, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_multiplying

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplying" ):
                return visitor.visitMultiplying(self)
            else:
                return visitor.visitChildren(self)




    def multiplying(self):

        localctx = MT22Parser.MultiplyingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_multiplying)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 55834574848) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MT22Parser.RULE_unary

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnary" ):
                return visitor.visitUnary(self)
            else:
                return visitor.visitChildren(self)




    def unary(self):

        localctx = MT22Parser.UnaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_unary)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUAL(self):
            return self.getToken(MT22Parser.EQUAL, 0)

        def NOTEQUAL(self):
            return self.getToken(MT22Parser.NOTEQUAL, 0)

        def LT(self):
            return self.getToken(MT22Parser.LT, 0)

        def GT(self):
            return self.getToken(MT22Parser.GT, 0)

        def LET(self):
            return self.getToken(MT22Parser.LET, 0)

        def GET(self):
            return self.getToken(MT22Parser.GET, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_relational

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational" ):
                return visitor.visitRelational(self)
            else:
                return visitor.visitChildren(self)




    def relational(self):

        localctx = MT22Parser.RelationalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_relational)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 264241152) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StrconcateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONCATE(self):
            return self.getToken(MT22Parser.CONCATE, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_strconcate

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStrconcate" ):
                return visitor.visitStrconcate(self)
            else:
                return visitor.visitChildren(self)




    def strconcate(self):

        localctx = MT22Parser.StrconcateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_strconcate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.match(MT22Parser.CONCATE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnarylogicalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(MT22Parser.NOT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_unarylogical

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnarylogical" ):
                return visitor.visitUnarylogical(self)
            else:
                return visitor.visitChildren(self)




    def unarylogical(self):

        localctx = MT22Parser.UnarylogicalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_unarylogical)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.match(MT22Parser.NOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BinarylogicalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(MT22Parser.AND, 0)

        def OR(self):
            return self.getToken(MT22Parser.OR, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_binarylogical

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinarylogical" ):
                return visitor.visitBinarylogical(self)
            else:
                return visitor.visitChildren(self)




    def binarylogical(self):

        localctx = MT22Parser.BinarylogicalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_binarylogical)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            _la = self._input.LA(1)
            if not(_la==28 or _la==29):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB(self):
            return self.getToken(MT22Parser.SUB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_sign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSign" ):
                return visitor.visitSign(self)
            else:
                return visitor.visitChildren(self)




    def sign(self):

        localctx = MT22Parser.SignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_sign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.match(MT22Parser.SUB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTL(self):
            return self.getToken(MT22Parser.INTL, 0)

        def FLOATL(self):
            return self.getToken(MT22Parser.FLOATL, 0)

        def STRINGL(self):
            return self.getToken(MT22Parser.STRINGL, 0)

        def BOOLL(self):
            return self.getToken(MT22Parser.BOOLL, 0)

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def arrayl(self):
            return self.getTypedRuleContext(MT22Parser.ArraylContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_operands

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperands" ):
                return visitor.visitOperands(self)
            else:
                return visitor.visitChildren(self)




    def operands(self):

        localctx = MT22Parser.OperandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_operands)
        try:
            self.state = 189
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [49]:
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.match(MT22Parser.INTL)
                pass
            elif token in [50]:
                self.enterOuterAlt(localctx, 2)
                self.state = 184
                self.match(MT22Parser.FLOATL)
                pass
            elif token in [52]:
                self.enterOuterAlt(localctx, 3)
                self.state = 185
                self.match(MT22Parser.STRINGL)
                pass
            elif token in [51]:
                self.enterOuterAlt(localctx, 4)
                self.state = 186
                self.match(MT22Parser.BOOLL)
                pass
            elif token in [53]:
                self.enterOuterAlt(localctx, 5)
                self.state = 187
                self.match(MT22Parser.ID)
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 6)
                self.state = 188
                self.arrayl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(MT22Parser.ARRAY, 0)

        def LSB(self):
            return self.getToken(MT22Parser.LSB, 0)

        def dimensions(self):
            return self.getTypedRuleContext(MT22Parser.DimensionsContext,0)


        def RSB(self):
            return self.getToken(MT22Parser.RSB, 0)

        def OF(self):
            return self.getToken(MT22Parser.OF, 0)

        def primitivetype(self):
            return self.getTypedRuleContext(MT22Parser.PrimitivetypeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_arrayType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayType" ):
                return visitor.visitArrayType(self)
            else:
                return visitor.visitChildren(self)




    def arrayType(self):

        localctx = MT22Parser.ArrayTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_arrayType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.match(MT22Parser.ARRAY)
            self.state = 192
            self.match(MT22Parser.LSB)
            self.state = 193
            self.dimensions()
            self.state = 194
            self.match(MT22Parser.RSB)
            self.state = 195
            self.match(MT22Parser.OF)
            self.state = 196
            self.primitivetype()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimensionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTL(self):
            return self.getToken(MT22Parser.INTL, 0)

        def dimension(self):
            return self.getTypedRuleContext(MT22Parser.DimensionContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_dimensions

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimensions" ):
                return visitor.visitDimensions(self)
            else:
                return visitor.visitChildren(self)




    def dimensions(self):

        localctx = MT22Parser.DimensionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_dimensions)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.match(MT22Parser.INTL)
            self.state = 199
            self.dimension()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimensionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(MT22Parser.COMA, 0)

        def INTL(self):
            return self.getToken(MT22Parser.INTL, 0)

        def dimension(self):
            return self.getTypedRuleContext(MT22Parser.DimensionContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_dimension

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimension" ):
                return visitor.visitDimension(self)
            else:
                return visitor.visitChildren(self)




    def dimension(self):

        localctx = MT22Parser.DimensionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_dimension)
        try:
            self.state = 205
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [44]:
                self.enterOuterAlt(localctx, 1)
                self.state = 201
                self.match(MT22Parser.COMA)
                self.state = 202
                self.match(MT22Parser.INTL)
                self.state = 203
                self.dimension()
                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraylContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(MT22Parser.LCB, 0)

        def exprlst(self):
            return self.getTypedRuleContext(MT22Parser.ExprlstContext,0)


        def RCB(self):
            return self.getToken(MT22Parser.RCB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_arrayl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayl" ):
                return visitor.visitArrayl(self)
            else:
                return visitor.visitChildren(self)




    def arrayl(self):

        localctx = MT22Parser.ArraylContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_arrayl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.match(MT22Parser.LCB)
            self.state = 208
            self.exprlst()
            self.state = 209
            self.match(MT22Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





