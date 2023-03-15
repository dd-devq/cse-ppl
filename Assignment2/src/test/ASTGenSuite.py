import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_short_vardecl(self):
        input = """x: integer;"""
        expect = str(Program([VarDecl("x", IntegerType())]))
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_short_vardecl1(self):
        input = """x: auto;"""
        expect = str(Program([VarDecl("x", AutoType())]))
        self.assertTrue(TestAST.test(input, expect, 307))

    def test_short_vardecl2(self):
        input = """x: auto = 7;"""
        expect = str(Program([VarDecl("x", AutoType(), IntegerLit(7))]))
        self.assertTrue(TestAST.test(input, expect, 308))

    def test_short_vardecl3(self):
        input = """x: auto = 7.0;"""
        expect = str(Program([VarDecl("x", AutoType(), FloatLit(7.0))]))
        self.assertTrue(TestAST.test(input, expect, 309))

    def test_full_vardecl(self):
        input = """x, y, z: integer = 1, 2, 3;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
])"""
        self.assertTrue(TestAST.test(input, expect, 301))

    def test_vardecls(self):
        input = """a, b: float; 
        x, y, z: integer = 1_, 2, 3;"""
        expect = """Program([
	VarDecl(a, FloatType)
	VarDecl(b, FloatType)
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
])"""
        self.assertTrue(TestAST.test(input, expect, 302))

    def test_simple_program(self):
        """Simple program"""
        input = """main: function void () {
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_more_complex_program(self):
        """More complex program"""
        input = """main: function void () {
            printInteger(4);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 304))

    def test1(self):
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

    def test2(self):
        input = """x, y, z: array [1] of integer = {1}, {4}, {5};"""
        expect = """Program([
	VarDecl(x, ArrayType([1], IntegerType), ArrayLit([IntegerLit(1)]))
	VarDecl(y, ArrayType([1], IntegerType), ArrayLit([IntegerLit(4)]))
	VarDecl(z, ArrayType([1], IntegerType), ArrayLit([IntegerLit(5)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 306))

    def test3(self):
        input = """x, y, z: float = 1.2, 3e12, 1_33.33e-23;"""
        expect = """Program([
	VarDecl(x, FloatType, FloatLit(1.2))
	VarDecl(y, FloatType, FloatLit(3e12))
	VarDecl(z, FloatType, FloatLit(133.33e-23))
])"""
        self.assertTrue(TestAST.test(input, expect, 310))

    def test4(self):
        input = """x, y : integer = a, b ;"""
        expect = """Program([
	VarDecl(x, IntegerType, Id(a))
	VarDecl(y, IntegerType, Id(b))
])"""
        self.assertTrue(TestAST.test(input, expect, 311))

    def test5(self):
        input = """x : string = "abc" ;"""
        expect = """Program([
	VarDecl(x, StringType, StringLit(abc))
])"""
        self.assertTrue(TestAST.test(input, expect, 312))

    def test6(self):
        input = """x : string = ("abc"::"cde")::"xyz" ;"""
        expect = """Program([
	VarDecl(x, StringType, BinExpr(::, BinExpr(::, StringLit(abc), StringLit(cde)), StringLit(xyz)))
])"""
        self.assertTrue(TestAST.test(input, expect, 313))

    def test7(self):
        input = """x : boolean = (a == 9) > (5 == 8) ;"""
        expect = """Program([
	VarDecl(x, BooleanType, BinExpr(>, BinExpr(==, Id(a), IntegerLit(9)), BinExpr(==, IntegerLit(5), IntegerLit(8))))
])"""
        self.assertTrue(TestAST.test(input, expect, 314))

    def test8(self):
        input = """x, y : integer = arr[0, 1, 2], arr1[4, 5, 6] ;"""
        expect = """Program([
	VarDecl(x, IntegerType, ArrayCell(Id(arr), [IntegerLit(0), IntegerLit(1), IntegerLit(2)]))
	VarDecl(y, IntegerType, ArrayCell(Id(arr1), [IntegerLit(4), IntegerLit(5), IntegerLit(6)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 315))

    def test9(self):
        input = """x, y : integer = func(1,2,3), func();"""
        expect = """Program([
	VarDecl(x, IntegerType, FuncCall(func, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]))
	VarDecl(y, IntegerType, FuncCall(func, []))
])"""
        self.assertTrue(TestAST.test(input, expect, 316))

    def test10(self):
        input = """main: function void () {
            while (a != 5) {}
        }"""
        expect = """Program([
	VarDecl(x, IntegerType, FuncCall(func, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]))
	VarDecl(y, IntegerType, FuncCall(func, []))
])"""
        self.assertTrue(TestAST.test(input, expect, 317))
