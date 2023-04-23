import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    # def test_no_entry(self):
    #     input = """x, y, z: integer;"""
    #     expect = """No entry point"""
    #     self.assertTrue(TestChecker.test(input, expect, 401))

    # def test_no_entry(self):
    #     input = Program(
    #         [VarDecl("a", IntegerType(), IntegerLit(5)), VarDecl("c", AutoType())])
    #     expect = """No entry point"""
    #     self.assertTrue(TestChecker.test(input, expect, 405))

    # def test_full_program_0(self):
    #     input = """main: function void() {

    #     }"""
    #     expect = """[None]"""
    #     self.assertTrue(TestChecker.test(input, expect, 402))

    # def test_full_program_1(self):
    #     input = """
    #     x: integer = 0.5;
    #     main: function void() {

    #     }"""
    #     expect = """Type mismatch in Variable Declaration: VarDecl(x, IntegerType, FloatLit(0.5))"""
    #     self.assertTrue(TestChecker.test(input, expect, 403))

    # def test_full_program_2(self):
    #     input = """
    #     main: function void() {

    #     }

    #     foo: function integer(a: integer, a: integer) {

    #     }
    #     """
    #     expect = """Redeclared Parameter: a"""
    #     self.assertTrue(TestChecker.test(input, expect, 404))

    # def test_full_program_3(self):
    #     input = """
    #     x: integer = 1;
    #     main: function void() {
    #         x = foo(1, 10.0);
    #     }
    #     foo: function integer(a:integer, b : float) {
    #         return a;
    #     }"""

    #     expect = """[None, None, None]"""
    #     self.assertTrue(TestChecker.test(input, expect, 405))

    # def test_full_program_4(self):
    #     input = """
    #     x: float = 1;
    #     a: float = 1.5;
    #     main: function void() {
    #         x = a + foo(1, 2.0);
    #     }
    #     foo: function integer(a:integer, b : float) {
    #         return a;
    #     }"""

    #     expect = """[None, None, None, None]"""
    #     self.assertTrue(TestChecker.test(input, expect, 406))

    # def test_full_program_5(self):
    #     input = """
    #     x: float = 1;
    #     main: function void() {
    #         do {
    #             x = x + 1;
    #             foo(1, 0.5);
    #             t: boolean = (x > 10) || (x < 20);
    #             break;
    #             break;
    #         } while( (x > 10) || (x < 20));
    #     }
    #     foo: function integer(a:integer, b : float) {
    #         return a;
    #     }"""

    #     expect = """[None, None, None]"""
    #     self.assertTrue(TestChecker.test(input, expect, 407))

    # def test_full_program_6(self):
    #     input = """
    #     x: float = 1;
    #     main: function void() {
    #         x:boolean = false;
    #         {
    #             a: boolean = x;
    #         }
    #         x = -true;
    #     }
    #     foo: function integer(a:integer, b : float) {
    #         return a;
    #     }"""

    #     expect = """Type mismatch in expression: UnExpr(-, BooleanLit(True))"""
    #     self.assertTrue(TestChecker.test(input, expect, 408))

    # def test_full_program_7(self):
    #     input = """
    #     main: function void() {
    #         i: float;
    #         for (i = 1, i < 10, i + 1) {
    #             foo(i, 1.0);
    #         }
    #     }
    #     foo: function integer(a:integer, b : float) {
    #         return a;
    #     }"""

    #     expect = """Type mismatch in statement: ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(foo, Id(i), FloatLit(1.0))]))"""
    #     self.assertTrue(TestChecker.test(input, expect, 409))

    # def test_full_program_8(self):
    #     input = """
    #     main: function void() {
    #         a: array [2,2,2] of integer = { {{1,2}, {1,2}}, {{1,2}, {1,2}}};
    #         a[1,1,1] = 2.0;
    #     }
    #     foo: function integer(a:integer, b : float) {
    #         return a;
    #     }"""

    #     expect = """Type mismatch in statement: AssignStmt(ArrayCell(a, [IntegerLit(1), IntegerLit(1), IntegerLit(1)]), FloatLit(2.0))"""
    #     self.assertTrue(TestChecker.test(input, expect, 410))

    # def test_full_program_9(self):
    #     input = """
    #     main: function void() {
    #         a: auto = foo(1, 2.0);
    #         a = 2.0;
    #     }
    #     foo: function integer(a:integer, b : float) {
    #         return a;
    #     }"""

    #     expect = """Type mismatch in statement: AssignStmt(Id(a), FloatLit(2.0))"""
    #     self.assertTrue(TestChecker.test(input, expect, 411))

    # def test_full_program_10(self):
    #     input = """
    #     main: function void() {
    #         a: array [2,2,2] of integer = { {{1,2}, {1,2}}, {{1,2}, {1,2}}};
    #         a[1.0,1,1] = 2.0;
    #     }
    #     foo: function integer(a:integer, b : float) {
    #         return a;
    #     }"""

    #     expect = """Type mismatch in expression: ArrayCell(a, [FloatLit(1.0), IntegerLit(1), IntegerLit(1)])"""
    #     self.assertTrue(TestChecker.test(input, expect, 412))

    def test_full_program_11(self):
        input = """
        main: function void() {
            i: integer; 
            i = foo(1,2.0) + 1;
        }
        foo: function auto(a:integer, b : float) {
            return a;
        }"""

        expect = """[None, None]"""
        self.assertTrue(TestChecker.test(input, expect, 413))
