import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test1(self):
        input = """x: integer;"""
        expect = str(Program([VarDecl("x", IntegerType())]))
        self.assertTrue(TestAST.test(input, expect, 300))

    def test2(self):
        input = """x: auto;"""
        expect = str(Program([VarDecl("x", AutoType())]))
        self.assertTrue(TestAST.test(input, expect, 307))

    def test3(self):
        input = """x: auto = 7;"""
        expect = str(Program([VarDecl("x", AutoType(), IntegerLit(7))]))
        self.assertTrue(TestAST.test(input, expect, 308))

    def test4(self):
        input = """x: auto = 7.0;"""
        expect = str(Program([VarDecl("x", AutoType(), FloatLit(7.0))]))
        self.assertTrue(TestAST.test(input, expect, 309))

    def test5(self):
        input = """x, y, z: integer = 1, 2, 3;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
])"""
        self.assertTrue(TestAST.test(input, expect, 301))

    def test6(self):
        input = """a, b: float; 
        x, y, z: integer = 1_2, 2, 3;"""
        expect = """Program([
	VarDecl(a, FloatType)
	VarDecl(b, FloatType)
	VarDecl(x, IntegerType, IntegerLit(12))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
])"""
        self.assertTrue(TestAST.test(input, expect, 302))

    def test7(self):
        """Simple program"""
        input = """main: function void () {
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 303))

    def test8(self):
        """More complex program"""
        input = """main: function void () {
            printInteger(4);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 304))

    def test9(self):
        input = """x,y,z,a,b,c: array [1,2,3] of integer; a,b,c: array [4,6,7] of float;"""
        expect = """Program([
	VarDecl(x, ArrayType([1, 2, 3], IntegerType))
	VarDecl(y, ArrayType([1, 2, 3], IntegerType))
	VarDecl(z, ArrayType([1, 2, 3], IntegerType))
	VarDecl(a, ArrayType([1, 2, 3], IntegerType))
	VarDecl(b, ArrayType([1, 2, 3], IntegerType))
	VarDecl(c, ArrayType([1, 2, 3], IntegerType))
	VarDecl(a, ArrayType([4, 6, 7], FloatType))
	VarDecl(b, ArrayType([4, 6, 7], FloatType))
	VarDecl(c, ArrayType([4, 6, 7], FloatType))
])"""
        self.assertTrue(TestAST.test(input, expect, 305))

    def test10(self):
        input = """x, y, z: array [1] of integer = {1}, {4}, {5};"""
        expect = """Program([
	VarDecl(x, ArrayType([1], IntegerType), ArrayLit([IntegerLit(1)]))
	VarDecl(y, ArrayType([1], IntegerType), ArrayLit([IntegerLit(4)]))
	VarDecl(z, ArrayType([1], IntegerType), ArrayLit([IntegerLit(5)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 306))

    def test11(self):
        input = """x, y, z: float = 1.2, 3e12, 1_33.33e-23;"""
        expect = """Program([
	VarDecl(x, FloatType, FloatLit(1.2))
	VarDecl(y, FloatType, FloatLit(3000000000000.0))
	VarDecl(z, FloatType, FloatLit(1.3333e-21))
])"""
        self.assertTrue(TestAST.test(input, expect, 310))

    def test12(self):
        input = """x, y : integer = a, b ;"""
        expect = """Program([
	VarDecl(x, IntegerType, Id(a))
	VarDecl(y, IntegerType, Id(b))
])"""
        self.assertTrue(TestAST.test(input, expect, 311))

    def test13(self):
        input = """x : string = "abc" ;"""
        expect = """Program([
	VarDecl(x, StringType, StringLit(abc))
])"""
        self.assertTrue(TestAST.test(input, expect, 312))

    def test14(self):
        input = """x : string = ("abc"::"cde")::"xyz" ;"""
        expect = """Program([
	VarDecl(x, StringType, BinExpr(::, BinExpr(::, StringLit(abc), StringLit(cde)), StringLit(xyz)))
])"""
        self.assertTrue(TestAST.test(input, expect, 313))

    def test15(self):
        input = """x : boolean = (a == 9) > (5 == 8) ;"""
        expect = """Program([
	VarDecl(x, BooleanType, BinExpr(>, BinExpr(==, Id(a), IntegerLit(9)), BinExpr(==, IntegerLit(5), IntegerLit(8))))
])"""
        self.assertTrue(TestAST.test(input, expect, 314))

    def test16(self):
        input = """x, y : integer = arr[0, 1, 2], arr1[4, 5, 6] ;"""
        expect = """Program([
	VarDecl(x, IntegerType, ArrayCell(Id(arr), [IntegerLit(0), IntegerLit(1), IntegerLit(2)]))
	VarDecl(y, IntegerType, ArrayCell(Id(arr1), [IntegerLit(4), IntegerLit(5), IntegerLit(6)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 315))

    def test17(self):
        input = """x, y : integer = func(1,2,3), func();"""
        expect = """Program([
	VarDecl(x, IntegerType, FuncCall(func, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]))
	VarDecl(y, IntegerType, FuncCall(func, []))
])"""
        self.assertTrue(TestAST.test(input, expect, 316))

    def test18(self):
        input = """main: function void () {
            while (a != 5) {}
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(!=, Id(a), IntegerLit(5)), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 317))

    def test19(self):
        input = """main: function void () {            
            for (i = 1, i < 10, i + 1) {
                writeInt(i);
            }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(writeInt, Id(i))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 318))

    def test20(self):
        input = """main: function void () {
            do {
                i = i + 1;
            }
            while (a != 5);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(!=, Id(a), IntegerLit(5)), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 319))

    def test21(self):
        input = """main: function void () {
            arr: array [3] of integer = {1,3,5};
            arr[0] = 9;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(arr, ArrayType([3], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(3), IntegerLit(5)])), AssignStmt(ArrayCell(Id(arr), [IntegerLit(0)]), IntegerLit(9))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 320))

    def test22(self):
        """More complex program"""
        input = """main1 : function array [2,2] of string () {
                return 0;
                return;
                return 1; 
            }"""
        expect = """Program([
	FuncDecl(main1, ArrayType([2, 2], StringType), [], None, BlockStmt([ReturnStmt(IntegerLit(0)), ReturnStmt(), ReturnStmt(IntegerLit(1))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 321))

    def test23(self):
        """More complex program"""
        input = """func1 : function void (c : string, out d : boolean) {
                printInteger(a);
                readInteger();
            }"""
        expect = """Program([
	FuncDecl(func1, VoidType, [Param(c, StringType), OutParam(d, BooleanType)], None, BlockStmt([CallStmt(printInteger, Id(a)), CallStmt(readInteger, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 322))

    def test24(self):
        """More complex program"""
        input = """a: float = 3.1;"""
        expect = """Program([
	VarDecl(a, FloatType, FloatLit(3.1))
])"""
        self.assertTrue(TestAST.test(input, expect, 351))

    def test25(self):
        """Simple program"""
        input = """a: string = "Hey boyyyyy"; main: function void() {}"""
        expect = """Program([
	VarDecl(a, StringType, StringLit(Hey boyyyyy))
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 352))

    def test26(self):
        """Simple program"""
        input = """main: function integer(n: integer, s: string) {
            return s[n];
        }"""
        expect = """Program([
	FuncDecl(main, IntegerType, [Param(n, IntegerType), Param(s, StringType)], None, BlockStmt([ReturnStmt(ArrayCell(Id(s), [Id(n)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 353))

    
    def test27(self):
        """Type test 1"""
        input = """main: function integer(n: array[3,2] of integer, s: string) {
            foo(r);
        }"""
        expect = """Program([
	FuncDecl(main, IntegerType, [Param(n, ArrayType([3, 2], IntegerType)), Param(s, StringType)], None, BlockStmt([CallStmt(foo, Id(r))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 354))

    def test28(self):
        """Program structure 1"""
        input = """r: function integer () {}
        f: string = "For fun"; """
        expect = """Program([
	FuncDecl(r, IntegerType, [], None, BlockStmt([]))
	VarDecl(f, StringType, StringLit(For fun))
])"""
        self.assertTrue(TestAST.test(input, expect, 355))

    def test29(self):
        """Program structure 2"""
        input = """r: function integer () {} _r_1: function void () {} _____rr: function auto(){}"""
        expect = """Program([
	FuncDecl(r, IntegerType, [], None, BlockStmt([]))
	FuncDecl(_r_1, VoidType, [], None, BlockStmt([]))
	FuncDecl(_____rr, AutoType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 356))

    def test30(self):
        """Program structure 3"""
        input = """deez: function float(inherit out nut: integer) {}"""
        expect = """Program([
	FuncDecl(deez, FloatType, [InheritOutParam(nut, IntegerType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 357))

    def test31(self):
        """Function params 1"""
        input = """main: function void(n: integer, arr: array[3,2] of string) {}"""
        expect = """Program([
	FuncDecl(main, VoidType, [Param(n, IntegerType), Param(arr, ArrayType([3, 2], StringType))], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 358))

    def test32(self):
        """Function params 2"""
        input = """main: function void(n: integer, out s: string, inherit f: float, tr: auto) {}"""
        expect = """Program([
	FuncDecl(main, VoidType, [Param(n, IntegerType), OutParam(s, StringType), InheritParam(f, FloatType), Param(tr, AutoType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 359))

    def test33(self):
        """Function params 3"""
        input = """
        x, y, z: integer = 2 + 3, -4 * 5, foo(10);
        t: float = time();
        main: function void(out n: void) {}"""
        expect = """Program([
	VarDecl(x, IntegerType, BinExpr(+, IntegerLit(2), IntegerLit(3)))
	VarDecl(y, IntegerType, BinExpr(*, UnExpr(-, IntegerLit(4)), IntegerLit(5)))
	VarDecl(z, IntegerType, FuncCall(foo, [IntegerLit(10)]))
	VarDecl(t, FloatType, FuncCall(time, []))
	FuncDecl(main, VoidType, [OutParam(n, VoidType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 360))

    def test34(self):
        """Variable dec1"""
        input = """main: function void() {
            x: float = 2.3e2;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, FloatType, FloatLit(230.0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 361))

    def test35(self):
        """Variable dec2"""
        input = """main: function void() {
            x, y: integer = 2, 3;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(2)), VarDecl(y, IntegerType, IntegerLit(3))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 362))

    def test36(self):
        """Variable dec4"""
        input = """main: function void() {
            x, y, z: string = "","","";
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, StringType, StringLit()), VarDecl(y, StringType, StringLit()), VarDecl(z, StringType, StringLit())]))
])"""
        self.assertTrue(TestAST.test(input, expect, 363))

    def test37(self):
        """Variable dec5"""
        input = """main: function void() {
            x, y, z: string;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, StringType), VarDecl(y, StringType), VarDecl(z, StringType)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 364))

    def test38(self):
        """Variable dec6"""
        input = """main: function void() {
            x, y, z: string = toString(a), toString(b), toString(c);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, StringType, FuncCall(toString, [Id(a)])), VarDecl(y, StringType, FuncCall(toString, [Id(b)])), VarDecl(z, StringType, FuncCall(toString, [Id(c)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 365))

    def test39(self):
        """Variable dec7"""
        input = """main: function void() {
            x, y, z: string = int, int, int;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, StringType, Id(int)), VarDecl(y, StringType, Id(int)), VarDecl(z, StringType, Id(int))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 366))

    def test40(self):
        """Variable dec8"""
        input = """main: function void() {
            arr: array[3, 3, 1, 2] of integer;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(arr, ArrayType([3, 3, 1, 2], IntegerType))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 367))

    def test41(self):
        """Variable dec9"""
        input = """main: function void() {
            arr: array[3, 3] of integer = {{2,3,4},{5,6,7},{8,9,10}};
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(arr, ArrayType([3, 3], IntegerType), ArrayLit([ArrayLit([IntegerLit(2), IntegerLit(3), IntegerLit(4)]), ArrayLit([IntegerLit(5), IntegerLit(6), IntegerLit(7)]), ArrayLit([IntegerLit(8), IntegerLit(9), IntegerLit(10)])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 368))

    def test42(self):
        """Variable dec10"""
        input = """x, y, z: array [1] of integer = {1}, {4}, {5};"""
        expect = """Program([
	VarDecl(x, ArrayType([1], IntegerType), ArrayLit([IntegerLit(1)]))
	VarDecl(y, ArrayType([1], IntegerType), ArrayLit([IntegerLit(4)]))
	VarDecl(z, ArrayType([1], IntegerType), ArrayLit([IntegerLit(5)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 323))

    def test43(self):
        """Expression 1"""
        input = """main: function void() {
            a: integer = 3;
            b: integer = 4;
            c: integer = b % a + 4;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(3)), VarDecl(b, IntegerType, IntegerLit(4)), VarDecl(c, IntegerType, BinExpr(+, BinExpr(%, Id(b), Id(a)), IntegerLit(4)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 324))

    def test44(self):
        """Expression 2"""
        input = """main: function void() {
            a: integer = 3;
            b: integer = 4;
            c: integer = {{2,3}}[3];
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(3)), VarDecl(b, IntegerType, IntegerLit(4)), VarDecl(c, IntegerType, ArrayCell(ArrayLit([ArrayLit([IntegerLit(2), IntegerLit(3)])]), [IntegerLit(3)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 325))

    def test45(self):
        """Expression 3"""
        input = """a: float = !true % 5 / 4;"""
        expect = """Program([
	VarDecl(a, FloatType, BinExpr(/, BinExpr(%, UnExpr(!, BooleanLit(True)), IntegerLit(5)), IntegerLit(4)))
])"""
        self.assertTrue(TestAST.test(input, expect, 326))

    def test46(self):
        """Expression 4"""
        input = """a: integer = 4;
        main: function void() {
            a = str(a)::"af";
        }"""
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(4))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(::, FuncCall(str, [Id(a)]), StringLit(af)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 327))

    def test47(self):
        """Expression 5"""
        input = """a: integer = 4;
        main: function void() {
            a = true || false && true;
        }"""
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(4))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(&&, BinExpr(||, BooleanLit(True), BooleanLit(False)), BooleanLit(True)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 328))

    def test48(self):
        """Expression 6"""
        input = """a: integer = 4;
        main: function void() {
            a = true || false && false && false > 1;
        }"""
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(4))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(>, BinExpr(&&, BinExpr(&&, BinExpr(||, BooleanLit(True), BooleanLit(False)), BooleanLit(False)), BooleanLit(False)), IntegerLit(1)))]))
])"""

        self.assertTrue(TestAST.test(input, expect, 329))

    def test49(self):
        """Expression 7"""
        input = """a: integer = 4;
        main: function void() {
            a = arr[b, c, c::"string"];
        }"""
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(4))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), ArrayCell(Id(arr), [Id(b), Id(c), BinExpr(::, Id(c), StringLit(string))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 330))

    def test50(self):
        """Expression 8"""
        input = """a: integer = 4;
        main: function void() {
            a = 1 > 0;
        }"""
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(4))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(>, IntegerLit(1), IntegerLit(0)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 331))

    def test51(self):
        """Expression 9"""
        input = """
        main: function void() {
            a = foo(after(foo(after(foo(endhere)))));
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), FuncCall(foo, [FuncCall(after, [FuncCall(foo, [FuncCall(after, [FuncCall(foo, [Id(endhere)])])])])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 332))

    def test52(self):
        """Expression 10"""
        input = """
        main: function void() {
            a = ((a > 0) + 3) * 10;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(*, BinExpr(+, BinExpr(>, Id(a), IntegerLit(0)), IntegerLit(3)), IntegerLit(10)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 333))

    def test53(self):
        """Expression 11"""
        input = """
        main: function void() {
            a = a > 0 + 3 * 10;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(>, Id(a), BinExpr(+, IntegerLit(0), BinExpr(*, IntegerLit(3), IntegerLit(10)))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 334))

    def test54(self):
        """Array 1"""
        input = """main: function void() {
            a: array[3] of float = {{f,g,h},{"M","J","D"},{1+3,3+4,5+7}}[3];
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([3], FloatType), ArrayCell(ArrayLit([ArrayLit([Id(f), Id(g), Id(h)]), ArrayLit([StringLit(M), StringLit(J), StringLit(D)]), ArrayLit([BinExpr(+, IntegerLit(1), IntegerLit(3)), BinExpr(+, IntegerLit(3), IntegerLit(4)), BinExpr(+, IntegerLit(5), IntegerLit(7))])]), [IntegerLit(3)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 335))

    def test55(self):
        """Array 2"""
        input = """main: function void() {
            a[4] = {"DF",DSDS,__proto__};
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(Id(a), [IntegerLit(4)]), ArrayLit([StringLit(DF), Id(DSDS), Id(__proto__)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 336))

    def test56(self):
        """Array 3"""
        input = """main: function void() {
            a[4, 4 && 5 + 1] = {"DF",DSDS,__proto__};
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(Id(a), [IntegerLit(4), BinExpr(&&, IntegerLit(4), BinExpr(+, IntegerLit(5), IntegerLit(1)))]), ArrayLit([StringLit(DF), Id(DSDS), Id(__proto__)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 337))

    def test57(self):
        """Array 4"""
        input = """
        main: function void(arr: array[2] of float) {
            a: array[1] of integer = {1};
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [Param(arr, ArrayType([2], FloatType))], None, BlockStmt([VarDecl(a, ArrayType([1], IntegerType), ArrayLit([IntegerLit(1)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 338))

    def test58(self):
        """Array 5"""
        input = """
        main: function void() {
            a: array[1] of integer = {"ff" :: "dd"};
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([1], IntegerType), ArrayLit([BinExpr(::, StringLit(ff), StringLit(dd))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 339))
    
    def test59(self):
        """Array 6"""
        input = """
        main: function void() {
            a: array[2,2,2,2,2,2,2,2] of auto = {{{{{23}}}}};
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([2, 2, 2, 2, 2, 2, 2, 2], AutoType), ArrayLit([ArrayLit([ArrayLit([ArrayLit([ArrayLit([IntegerLit(23)])])])])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 340))

    def test60(self):
        """Assignment statement 1"""
        input = """
        main: function void() {
            a, b, c: array[3] of integer = {1,2,3},{1,2,3},{1,2,3};
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([3], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])), VarDecl(b, ArrayType([3], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])), VarDecl(c, ArrayType([3], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 341))

    def test61(self):
        """Assignment statement 3"""
        input = """
        main: function void() {
            a: float = 33.223;
            b: integer = 43_3e4;
            c: float = 123.456e-78;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, FloatType, FloatLit(33.223)), VarDecl(b, IntegerType, FloatLit(4330000.0)), VarDecl(c, FloatType, FloatLit(1.23456e-76))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 342))

    def test62(self):
        """Assignment statement 5"""
        input = """
        main: function void() {
            a = foo(24, bar);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), FuncCall(foo, [IntegerLit(24), Id(bar)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 343))

    def test63(self):
        """Assignment statement 6"""
        input = """
        main: function void() {
            a[4, 5] = bar(b[4], c[5]);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(Id(a), [IntegerLit(4), IntegerLit(5)]), FuncCall(bar, [ArrayCell(Id(b), [IntegerLit(4)]), ArrayCell(Id(c), [IntegerLit(5)])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 344))

    def test64(self):
        """Condition statement 1"""
        input = """
        main: function void() {
            if (true) a = a + 1;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BooleanLit(True), AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 345))

    def test65(self):
        """Condition statement 2"""
        input = """
        main: function void() {
            if (true) a = a + 1;
            else a = a - 1;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BooleanLit(True), AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1))), AssignStmt(Id(a), BinExpr(-, Id(a), IntegerLit(1))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 346))

    def test66(self):
        """Condition statement 3"""
        input = """
        main: function void() {
            if (a == 1) {
                return a == 1;
            }
            else {
                return a == 1;
            }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(1)), BlockStmt([ReturnStmt(BinExpr(==, Id(a), IntegerLit(1)))]), BlockStmt([ReturnStmt(BinExpr(==, Id(a), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 347))

    def test67(self):
        """Condition statement 4"""
        input = """
        main: function void() {
            if (a + 4 == 5) {
                return a + 1;
            }
            else {
                if (a + 1 == 3) {
                    return a + 1;
                }
                return a + 2;
            }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, BinExpr(+, Id(a), IntegerLit(4)), IntegerLit(5)), BlockStmt([ReturnStmt(BinExpr(+, Id(a), IntegerLit(1)))]), BlockStmt([IfStmt(BinExpr(==, BinExpr(+, Id(a), IntegerLit(1)), IntegerLit(3)), BlockStmt([ReturnStmt(BinExpr(+, Id(a), IntegerLit(1)))])), ReturnStmt(BinExpr(+, Id(a), IntegerLit(2)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 348))

    def test68(self):
        """Condition statement 5"""
        input = """
        main: function void() {
            if (a > 4) {
                return a + 1;
            }
            if (a > 3)
                return 12;
            if (a == 1)
                return 5;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), IntegerLit(4)), BlockStmt([ReturnStmt(BinExpr(+, Id(a), IntegerLit(1)))])), IfStmt(BinExpr(>, Id(a), IntegerLit(3)), ReturnStmt(IntegerLit(12))), IfStmt(BinExpr(==, Id(a), IntegerLit(1)), ReturnStmt(IntegerLit(5)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 349))

    def test69(self):
        """Condition statement 6"""
        input = """
        main: function void() {
            if (a == 1) {
                if (a == 1) {
                    if (a == 1) {
                        l = mao;
                    }
                }
            }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(1)), BlockStmt([AssignStmt(Id(l), Id(mao))]))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 350))

    def test70(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 370))
        
    def test71(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 371))
        
    def test72(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 372))

    def test73(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 373))
        
    def test74(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 374))
        
    def test75(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 375))
        
    def test76(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 376))
        
    def test77(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 377))
        
    def test78(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 378))
        
    def test79(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 379))
        
    def test80(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 380))
        
    def test81(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 381))
        
    def test82(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 382))

    def test83(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 383))
        
    def test84(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 384))
        
    def test85(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 385))
        
    def test86(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 386))
        
    def test87(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 387))
        
    def test88(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 388))
        
    def test89(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 389))
        
    def test90(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 390))
        
    def test91(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 391))
        
    def test92(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 392))

    def test93(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 393))
        
    def test94(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 394))
        
    def test95(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 395))
        
    def test96(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 396))
        
    def test97(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 397))
        
    def test98(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 398))
        
    def test99(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 399))
        
    def test100(self):
        """More complex program"""
        input = """main1 : function string () {}"""
        expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([]))
])"""